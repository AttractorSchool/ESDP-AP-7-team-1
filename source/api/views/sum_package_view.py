import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from education.models import Packet, Discount


class SumPackageView(View):
    def post(self, request, *args, **kwargs):
        data = {}
        if request.body:
            package = json.loads(request.body)
            get_package = get_object_or_404(Packet, qty=package.get('package'))
            data['sum'] = get_package.sum
            data['package'] = get_package.name.lower()
        return JsonResponse(data)


class SumDiscountView(View):
    def post(self, request, *args, **kwargs):
        data = {}
        if request.body:
            ajax_data = json.loads(request.body)
            get_package = get_object_or_404(Packet, qty=ajax_data.get('subject'))
            get_discount = get_object_or_404(Discount, pk=ajax_data.get('discount'))
            total = int(get_package.sum) - ((int(get_package.sum) * int(get_discount.discount_amount)) / 100)
            data['total'] = total
            data['discount'] = get_discount.discount_amount
        return JsonResponse(data)
