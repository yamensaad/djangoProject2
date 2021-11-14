from django.shortcuts import render
from cars import models


# Create your views here.
def index(request):
    return render( request, 'main.html' )


def bar_show(request):
    return render( request, 'index.html' )


def line(request):
    return render( request, 'line.html' )


def line_plot(request):
    body = request.POST['bodies']
    labels = []
    data = []
    query = models.Cars.objects.filter( BodyStyle=body ).all() #choose from the Bodystlye where it's = Body
    for car in query:
        labels.append( car.Brand )  # x axis
        data.append( car.PriceEuro )  # y axis
    return render( request, 'line_plot.html', {
        'labels': labels,
        'data': data,
        'body': body,
    } )


def bar(request):
    power_train = request.POST['cars']
    labels = []
    data = []
    queryset = models.Cars.objects.filter( PowerTrain=power_train ).distinct( 'Brand' ).all()
    for car in queryset:
        labels.append( car.Brand )
        data.append( car.PriceEuro )
    return render( request, 'bar.html', {
        'labels': labels,
        'data': data,
        'power_train': power_train,
    } )


def display(request):
    return render( request, 'display.html' )


def pie_display(request):
    return render( request, 'pie_display.html' )


def pie_chart(request):
    labels = []
    data = []
    price = request.POST['price']
    queryset = models.Cars.objects.filter( PriceEuro__gte=price )
    for car in queryset:
        labels.append( car.Brand )
        data.append( car.PriceEuro )

    return render( request, 'pie.html', {
        'labels': labels,
        'data': data,

    } )


def pie_chart1(request):
    labels = []
    data = []
    queryset = models.Cars.objects.order_by( 'Brand', '-TopSpeed_KmH' ).distinct( 'Brand' )[:10]
    for car in queryset:
        labels.append( car.Brand )
        data.append( car.TopSpeed_KmH )

    return render( request, 'pie1.html', {
        'labels': labels,
        'data': data,

    } )


def line_chart1(request):
    labels = [] #list
    data = []
    queryset = models.Cars.objects.order_by( '-Brand', 'Efficiency_WhKm' ).distinct( 'Brand' )[:10]
    for car in queryset:
        labels.append( car.Brand ) ##add
        data.append( car.Efficiency_WhKm )

    return render( request, 'line_plot1.html', {
        'labels': labels,
        'data': data,

    } )


def bar1(request):
    labels = []
    data = []
    queryset = models.Cars.objects.order_by( '-Brand', 'Efficiency_WhKm' ).distinct( 'Brand' )[:10]
    for car in queryset:
        labels.append(car.Brand )
        data.append(car.Efficiency_WhKm)

    return render( request, 'bar1.html', {
        'labels': labels,
        'data': data,

    } )


