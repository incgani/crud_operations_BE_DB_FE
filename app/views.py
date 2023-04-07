from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length


# Create your views here.
def insert_t(request):
    LOT = Topic.objects.all()
    #LOT = Topic.objects.filter(topic_name='cricket')
    d = {'topics': LOT}
    return render(request, 'display_t.html', d)


def insert_w(request):
    LOW = Webpage.objects.all()
    #LOW=Webpage.objects.get(topic_name='FootBall')        error because its not primary key its returns only one object
    #LOW=Webpage.objects.exclude(topic_name='cricket')     expect cricket eveything will display
    #lOW = Webpage.objects.all()[1:2:]                     perfom slicing to achive no of sequence data
    #LOW = Webpage.objects.all().order_by('name')          Ascii value accending order
    #LOW = Webpage.objects.all().order_by('-name')         Ascii value decending order

    ##TO GET LENGTH IMPORT THE LENGHT UPSIDE IMPORTED
    #LOW = Webpage.objects.all().order_by(Length('name'))    accending in highest Length characters 
                                                     #     if same len of char means by the time of sequence of data its will display

    #LOW = Webpage.objects.all().order_by(Length('name').desc()) decending in highest Length characters 
                                                     #     if same len of char means by the time of sequence of data its will display


    d={'webpage':LOW}
    return render(request,'display_w.html',d)
def insert_a(request):
    LOA=AccessRecord.objects.all()
    #LOA=AccessRecord.objects.filter(date__gt='2022-10-10')
    LOA=AccessRecord.objects.filter(date__gte='1943-01-10')
    #LOA=AccessRecord.objects.filter(date__lt='2022-10-10')
    #LOA=AccessRecord.objects.filter(date__lte='2022-10-10')
    d={'access':LOA}
    return render(request,'display_a.html',d)

