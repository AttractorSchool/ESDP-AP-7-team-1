import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from education.models import Packet


class SumPackageView(View):
    def post(self, request, *args, **kwargs):
        data = {}
        if request.body:
            package = json.loads(request.body)
            get_package = get_object_or_404(Packet, qty=package.get('package'))
            data['sum'] = get_package.sum
            data['package'] = get_package.name.lower()
        return JsonResponse(data)


