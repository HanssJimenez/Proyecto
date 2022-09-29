from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from simple_app import models
# from django.http import HttpResponse

class IndexView(TemplateView):
    template_name =  'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'simple_app/school_detail.html'



#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['ingresa'] = 'ingreso basico'
#         return context

# class CBView(View):
#     def get(sefl,request):
#         return HttpResponse("Vista de clases es increible")
# Create your views here.
#
# def index(request):
#     return render(request,'index.html')
