# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render
#
# # from myapp.models import Product, Contact, BacketProduct, Backet, Rating
# # from myapp.forms import ContactForm, CreateProductForm
#
# from django.contrib import messages
# from django.views.generic import TemplateView
# from django.views import View
# from django.http import HttpResponseRedirect
# from django.contrib.messages.views import SuccessMessageMixin
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.urls import reverse, reverse_lazy


# Create your views here.
# def products_list(request):
#     products = Product.objects.all()
#     context = {
#         "products": products
#     }
#     return render(request, 'product_list.html', context)


from django.shortcuts import render

def admin_dashboard(request):
    # Logic for the admin dashboard
    return render(request, 'adminpanel/dashboard.html')
