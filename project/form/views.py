from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from form.models import form

# Create your views here.

# def form(request):
#     return render(request, 'home.html') 

def formsubmit(request):
    if request.method == 'POST':
        form_name = request.POST.get('name')
        form_email = request.POST.get('email')
        form_number = request.POST.get('number')
        form_select = request.POST.get('select')

        try:
            formm=form(form_name=form_name, form_email=form_email, form_number=form_number, form_select=form_select)
            formm.save()
            return HttpResponse("data successfully inserted")
        
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
    else:
        return HttpResponse("Invalid request method")