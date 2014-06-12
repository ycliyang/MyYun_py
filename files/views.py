from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt
import os
from django.template import Template, Context
# Create your views here.

def index(request):
    return render_to_response("files/fileIndex.html");

@csrf_exempt
def uploadFile(request):
    files = request.FILES.getlist('myFiles')
    path = 'F:/temp/';
    for f in files:
        if os.path.exists(path)==False:
            os.mkdir(path)
        destination = open(path + f.name,'wb+')

        try:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                destination.write(chunk)
        finally:
             destination.close( )

        # for chunk in f.chunks():
        #     destination.write(chunk)
        #     destination.close()

    return render_to_response("files/uploadSuccess.html",{"success":True})