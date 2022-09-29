from django.shortcuts import render
from django.views.generic import View, TemplateView
# from django.http import HttpResponse

class IndexView(TemplateView):
    template_name =  'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingresa'] = 'ingreso basico'
        return context
# class CBView(View):
#     def get(sefl,request):
#         return HttpResponse("Vista de clases es increible")
# Create your views here.
#
# def index(request):
#     return render(request,'index.html')
