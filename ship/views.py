from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import FW, MDO, Ship


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Ship
    template_name = 'ship/index.html'
    context_object_name = 'ship_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['mdo'] = MDO.objects.all()
        context['fw'] = FW.objects.all()
        return context


class MdoUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    model = MDO
    fields = ['quantity']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('ship:index')


class FwUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    model = FW
    fields = ['quantity']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('ship:index')

