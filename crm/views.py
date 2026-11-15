from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from crm.models import Employee
from json import loads

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCreateView(View):

    def get(self,request):

        qs = Employee.objects.all().values()
        #here qs is query set, we have to convert it into PYNT

        response_data=list(qs) #qs=>PYNT

        return JsonResponse(response_data,safe=False) #PYNT=>json

    def post(self,request):

        json_data = request.body

        form_data = loads(json_data)

        Employee.objects.create(
            name=form_data.get("name"),
            email=form_data.get("email"),
            phone=form_data.get("phone"),
            salary=form_data.get("salary"),
            department=form_data.get("department"),
            location=form_data.get("location")
        )

        response_data = {"message":"employee created"}

        return JsonResponse(response_data)



@method_decorator(csrf_exempt,name='dispatch')
class EmployeeRetrieveUpdateDeleteView(View):

    def get(self,request,pk=None):

        qs =Employee.objects.filter(id=pk).values()

        response_data = list(qs)

        return JsonResponse(response_data,safe=False)

    def put(self,request,pk=None):

        json_data = request.body

        form_data = loads(json_data)

        Employee.objects.filter(id=pk).update(**form_data)

        response_data = {"message":"Employee Updated"}

        return JsonResponse(response_data)

    def delete(self,request,pk=None):

        Employee.objects.filter(id=pk).delete()

        response_data = {"message":"Employee Deleted"}

        return JsonResponse(response_data)