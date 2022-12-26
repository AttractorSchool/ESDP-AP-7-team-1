import datetime
from django.core.mail import EmailMessage 
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import tempfile
from django.http import HttpResponse, JsonResponse
from education.models.application import Application


MONTH=[
    "Қантар",
    "Ақпан",
    "Наурыз",
    "Сәуір",
    "Мамыр",
    "Маусым",
    "Шілде",
    "Тамыз",
    "Қыркүйек",
    "Қазан",
    "Қараша",
    "Желтоксан"
]


def render_pdf(request ,pk):
    """Формирование PDF Файла"""
    app = Application.objects.get(pk=pk)
    cur_date = datetime.datetime.now()
    month = MONTH[cur_date.month-1]   
    html_string = render_to_string('education/contract_template.html',
                                   {'app': app, 
                                    'date':cur_date, 
                                    'month': month
                                    }
                                   )
    css = CSS(string=''' @page {size: 220mm 297mm;}''')
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    result = html.write_pdf(stylesheets=[css])
    return result


def open_contract_pdf(request, *args, **kwargs):
    app = Application.objects.get(pk=kwargs.get('pk'))
    contract = render_pdf(request, app.pk)
    response = HttpResponse(contract, content_type='application/pdf')
    response['Content-Disposition'] = 'filename=contract.pdf'
    return response

