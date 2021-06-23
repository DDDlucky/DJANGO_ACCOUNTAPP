from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, DetailView # DetailViewを追加
from .models import Company, Fstatement
from django.views.generic.list import MultipleObjectMixin # この行を追加


class IndexView(TemplateView):
    template_name = 'finchart/index.html'

    def get_context_data(self, **kwargs):
        fstatement_list = Fstatement.objects.all().order_by('company')
        params = {
            'fstatement_list': fstatement_list,
        }
        return params

class CompanyView(DetailView):
    model = Company
    paginate_by = 4

    def get_context_data(self, **kwargs):
        company_name = kwargs['object'].name
        fstatement_list = Fstatement.objects.filter(company=kwargs['object']).order_by('-fiscal_year')[:4]
        params = {
            'company_name': company_name,
            'fstatement_list': fstatement_list,
        }
        return params

# ========以下をすべて追加========
class FstatementView(DetailView):
    model = Fstatement
