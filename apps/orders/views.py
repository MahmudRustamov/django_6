from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class CheckoutCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'products/product-checkout.html'

    """
    self.request.session.get('basket') is not None
    order create
    order items create

    basket ni tozalash
    self.request.session['basket'] = None
    """


