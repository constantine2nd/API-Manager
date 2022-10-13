from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
"""
Views of customer list app
"""
import datetime
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import FormView,TemplateView, View
from customers.views import CreateView
from obp.api import API, APIError
import csv



class CustomerListView(CreateView, LoginRequiredMixin, FormView ):
    template_name = "customerlist/customerlist.html"
    success_url = '/customers/list'
    def get_banks(self):
                api = API(self.request.session.get('obp'))
                try:
                    urlpath = '/banks'
                    result = api.get(urlpath)
                    if 'banks' in result:
                        return [bank['id'] for bank in sorted(result['banks'], key=lambda d: d['id'])]
                    else:
                        return []
                except APIError as err:
                    messages.error(self.request, err)
                    return []

    def get_customers(self, context):

            api = API(self.request.session.get('obp'))
            try:
                self.bankids = self.get_banks()
                customers_list = []
                #for bank_id in self.bankids:
                urlpath = '/my/customers'
                #urlpath = 'http://127.0.0.1:8080/obp/v4.0.0/my/customers'
                result = api.get(urlpath)
                print(result, "Result is ")
                if 'customers' in result:
                    customers_list.extend(result['customers'])
            except APIError as err:
                messages.error(self.request, err)
                return []
            except Exception as inst:
                messages.error(self.request, "Unknown Error {}".format(type(inst).__name__))
                return []
            print(customers_list[0], "This is a customer list")
            return customers_list
    def get_context_data(self, **kwargs):
            print("Hello from get_context_data")
            context = super(CreateView, self).get_context_data(**kwargs)
            customers_list = self.get_customers(context)
            context.update({
                'customers_list': customers_list,
                'bankids': self.bankids
            })
            print(context, "Bye from get_context_data")
            return context
class ExportCsvView(LoginRequiredMixin, View):
    """View to export the user to csv"""
    def get_banks(self):
        api = API(self.request.session.get('obp'))
        try:
            urlpath = '/banks'
            result = api.get(urlpath)
            if 'banks' in result:
                return [bank['id'] for bank in sorted(result['banks'], key=lambda d: d['id'])]
            else:
                return []
        except APIError as err:
            messages.error(self.request, err)
            return []
    def get(self, request, *args, **kwargs):
       api = API(self.request.session.get('obp'))
       try:
           self.bankids = self.get_banks()
           customers_list = []
           for bank_id in self.bankids:
               urlpath = '/banks/{}/customers'.format(bank_id)
               result = api.get(urlpath)
               #print(result)
               if 'customers' in result:
                   customers_list.extend(result['customers'])
       except APIError as err:
           messages.error(self.request, err)
       except Exception as inst:
           messages.error(self.request, "Unknown Error {}".format(type(inst).__name__))
       response = HttpResponse(content_type = 'text/csv')
       response['Content-Disposition'] = 'attachment;filename= Atms'+ str(datetime.datetime.now())+'.csv'
       writer = csv.writer(response)
       writer.writerow(["bank_id","customer_id","customer_number","legal_name","mobile_phone_number","email","face_image", "url", "date", "date_of_birth","relationship_status", "dependants","dob_of_dependants","employment_status"])
       for user in atms_list:
          writer.writerow([user['bank_id'],user['customer_id'], user['customer_number'], user["legal_name"],
                             user["mobile_phone_number"], user["email"], user["face_image"]['url'], user["face_image"]['date'], user["date_of_birth"], user['relationship_status'], user["dependants"], user["dob_of_dependants"], user['employment_status']])
       return response

       #print(atms_list)

