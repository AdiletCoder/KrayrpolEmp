from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .forms import CreateEmployeeForm, UpdateEmployeeForm, CreateCompanyForm, UpdateCompanyForm
from .models import Company, Employee


class SearchListView(ListView):
    model = Employee
    template_name = 'search.html'
    context_object_name = 'results'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        queryset = queryset.filter(Q(name__icontains=q) | Q(surname__icontains=q))
        return queryset


class CompanyListView(ListView):
    model = Company
    template_name = 'index.html'
    context_object_name = 'companies'


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'generic.html'
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'


class CompanyCreateView(CreateView):
    model = Company
    template_name = 'createCompany.html'
    form_class = CreateCompanyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_form'] = self.get_form(self.get_form_class())
        return context


class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'updateCompany.html'
    form_class = UpdateCompanyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_form'] = self.get_form(self.get_form_class())
        return context


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees.html'
    context_object_name = 'employees'

    def get_queryset(self):
        queryset = super().get_queryset()
        company = self.kwargs.get('slug')
        queryset = queryset.filter(company__slug=company)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = self.kwargs.get('slug')
        return context


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'detail.html'
    context_object_name = 'employee'
    pk_url_kwarg = 'employee_id'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'createEmployee.html'
    form_class = CreateEmployeeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_form'] = self.get_form(self.get_form_class())
        return context


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'update_employee.html'
    form_class = UpdateEmployeeForm
    pk_url_kwarg = 'employee_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_form'] = self.get_form(self.get_form_class())
        return context


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'deleteEmployee.html'
    pk_url_kwarg = 'employee_id'

    def get_success_url(self):
        from django.urls import reverse
        return reverse('home')

