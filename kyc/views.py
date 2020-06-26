from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "kyc/home.html")

def upload_xml(request):
	return render(request, "kyc/upload.html")

def confirm(request):
	# confirm
	return render(request, "kyc/confirm.html")