from django.views.generic import View, ListView, CreateView, UpdateView
from education.models import Discount
from education.forms.discount_form import DiscountForm
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404


class DiscountListView(ListView):
    template_name = 'education/discounts.html'
    model = Discount
    context_object_name = 'discounts'

    def get_queryset(self, *args, **kwargs):
        return Discount.objects.filter(is_deleted=False).order_by('pk')



class DiscountAddView(CreateView):
    template_name = 'education/package_add.html'
    form_class = DiscountForm
    model = Discount

    def get_success_url(self):
        return reverse('discounts')
