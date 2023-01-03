from django.db import models

from accounts.models import Account


LANGUAGE_CHOICES = (
    ('kaz', 'қазақша'),
    ('rus', 'орыс'),
)


class StatusOfGrouping(models.Model):
    """Возможные статусы группы"""
    name = models.CharField(verbose_name='Название', max_length=30, unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Доступный статус группы'
        verbose_name_plural = 'Доступные статусы групп'


class Grouping(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=20, unique=True)
    subject = models.ForeignKey(
        to='education.Subject',
        verbose_name='Название предмета',
        related_name='groupings',
        on_delete=models.CASCADE,
        )
    students = models.ManyToManyField(
        to=Account,
        through='education.StudentGrouping',
        verbose_name='Студенты',
        related_name='study_groupings',
    )
    teachers = models.ManyToManyField(
        to=Account,
        verbose_name='Преподаватели',
        through='education.TeacherGrouping',
        related_name='teach_groupings',
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    max_students = models.PositiveIntegerField(null=True, blank=True)
    min_students = models.PositiveIntegerField(null=True, blank=True)
    language = models.CharField(
        verbose_name='Язык обучения',
        max_length=20,
        choices=LANGUAGE_CHOICES,
        null=True,
        blank=True,
    )
    statuses = models.ManyToManyField(
        to=StatusOfGrouping,
        verbose_name='Статус группы',
        through='education.GroupingStatus',
        related_name='groupings',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа обучения'
        verbose_name_plural = 'Группы обучения'


class GroupingStatus(models.Model):
    """Установленные статусы групп (промежуточная таблица)"""
    grouping = models.ForeignKey(to=Grouping, on_delete=models.CASCADE, related_name='grouping_statuses')
    status = models.ForeignKey(to=StatusOfGrouping, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(verbose_name='Примечание', max_length=150, blank=True)
    author = models.ForeignKey(to='accounts.Account', on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return f'{self.grouping.name} - {self.status.name}'

    class Meta:
        verbose_name = 'Установленный статус группы'
        verbose_name_plural = 'Установленные статусы групп'
        get_latest_by = 'created_at'


class StudentGrouping(models.Model):
    """Привязка студента к группе"""
    grouping = models.ForeignKey(to=Grouping, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    enrolled_at = models.DateField(verbose_name='Дата зачисления', blank=True, null=True)
    expelled_at = models.DateField(verbose_name='Дата отчисления', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='Студент в группе', default=True)

    def __str__(self):
        return f'{self.grouping} - {self.student}'

    class Meta:
        verbose_name = 'Студент в группе'
        verbose_name_plural = 'Студенты в группе'


class ActiveModelQuerySet(models.QuerySet):

    def not_active(self, *args, **kwargs):
        return self.filter(is_active=False, *args, **kwargs)

    def active(self, *args, **kwargs):
        return self.filter(is_active=True, *args, **kwargs)

    def last(self):
        return self.active().latest('created_at')


class TeacherGrouping(models.Model):
    """Привязка преподавателя к группе"""
    grouping = models.ForeignKey(to=Grouping, on_delete=models.CASCADE, related_name='teacher_groupings')
    teacher = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name='teacher_groupings')
    started_at = models.DateField(verbose_name='Начал преподавать', blank=True, null=True)
    finished_at = models.DateField(verbose_name='Закончил преподавать', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)

    objects = ActiveModelQuerySet().as_manager()

    def __str__(self):
        return f'Группа: {self.grouping} - Преподаватель: {self.teacher}'

    class Meta:
        verbose_name = 'Преподаватель группы'
        verbose_name_plural = 'Преподаватели групп'
