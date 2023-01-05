from django.shortcuts import get_object_or_404

from accounts.models import Account

from applications.models import Application, ApplicationStatus, Status


def set_application_status(application: Application, status_name: str, author: Account):

    new_status: Status = get_object_or_404(Status, name=status_name)
    current_status: Status = application.application_statuses.last().status

    if current_status != new_status:
        ApplicationStatus.objects.create(application=application, status=new_status, author=author)


def get_button_status(application: Application) -> dict[str, str]:
    last_status_name: str = application.application_statuses.last().status.name

    button_contract = 'disabled'
    button_payed = 'disabled'
    button_user = 'disabled'

    if last_status_name == 'Подписание договора':
        button_contract = ''
    if last_status_name == 'Ожидание оплаты':
        button_contract = ''
        button_payed = ''
    if last_status_name == 'Оплачена':
        button_contract = ''
        button_payed = ''
        button_user = ''

    button_status = {}
    button_status['button_contract'] = button_contract
    button_status['button_payed'] = button_payed
    button_status['button_user'] = button_user

    return button_status
