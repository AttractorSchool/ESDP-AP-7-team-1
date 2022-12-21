from django.shortcuts import get_object_or_404

from education.models import ApplicationStatus, Status


def set_application_status(application, status_name, author):

    status: Status = get_object_or_404(Status, name=status_name)
    last_status: Status = application.application_statuses.last()
    # print('INFO желаемый статус: status', status)
    # print('INFO текущий статус: last_status', last_status)

    if last_status != status:
        application_status = ApplicationStatus(application=application, status=status, author=author)
        application_status.save()
        # print('INFO все статусы:', ApplicationStatus.objects.filter(application=application))
        # print('INFO новый статус:', application.application_statuses.latest())
