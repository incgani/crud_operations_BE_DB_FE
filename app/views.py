from django.shortcuts import render
from app.models import *


# Create your views here.
def Insert_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_t.html',d)
def Insert_WebPage(request):
    LOW=Webpage.objects.all()
    d={'webpage':LOW}
    return render(request,'display_w.html',d)
def Insert_AccessRecord(request):
    LOW=AccessRecord.objects.all()
    d={'access':LOW}
    return render(request,'display_a.html',d)

