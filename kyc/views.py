from django.shortcuts import render, redirect, get_object_or_404
from . models import Customer
from zipfile import ZipFile
from django.core.files import File
import xmltodict

def home(request):
    return render(request, "kyc/home.html")

def upload_xml(request):
    return render(request, "kyc/upload.html")

def upload_xml(request):
    if(request.method == 'POST'):
        if(request.FILES['xml_zip'] and request.POST['share_code']):
            customer = Customer()
            customer.share_code = request.POST['share_code']
            passwd = customer.share_code
            xml_zip = request.FILES['xml_zip']
            with ZipFile(xml_zip, 'r') as zipObj:
                listOfFileNames = zipObj.namelist()
                for fileName in listOfFileNames:
                    if fileName.endswith('.xml'):
                        xml_from_zip = zipObj.extract(fileName, path = 'offline_kyc/xmls/', pwd = passwd.encode())
                        customer.xml = File(open(xml_from_zip, mode='rb'),  name=f'{customer.id}.xml')
                        with open(xml_from_zip) as fd:
                            doc = xmltodict.parse(fd.read())
                            customer.name = str(doc['OfflinePaperlessKyc']['UidData']['Poi']['@name'])
                            customer.dob = str(doc['OfflinePaperlessKyc']['UidData']['Poi']['@dob'])
                            customer.pht = doc['OfflinePaperlessKyc']['UidData']['Pht']
                            customer.address = str(doc['OfflinePaperlessKyc']['UidData']['Poa']['@house']) + str(doc['OfflinePaperlessKyc']['UidData']['Poa']['@po']) + str(doc['OfflinePaperlessKyc']['UidData']['Poa']['@dist'])
            customer.save()
            return redirect('/kyc/' + str(customer.id))

        else:
            return(render(request, 'kyc/upload.html', {'error' : 'Please fill all the fields'}))
    else:
        return(render(request, 'kyc/upload.html'))

def confirm(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, "kyc/confirm.html", {'customer': customer})