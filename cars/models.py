from django.db import models


# Create your models here.


class Cars( models.Model ):
    Brand = models.TextField( "Brand", max_length=500 )
    Model = models.CharField( "Model", max_length=500 )
    AccelSec = models.CharField( "AccelSec", max_length=200 )
    TopSpeed_KmH = models.CharField( "TopSpeed_KmH", max_length=200 )
    Range_Km = models.CharField( "Range_Km", max_length=200 )
    Efficiency_WhKm = models.CharField( "Efficiency_WhKm", max_length=250 )
    FastCharge_KmH = models.CharField( "FastCharge_KmH", max_length=250 )
    RapidCharge = models.CharField( "RapidCharge", max_length=255 )
    PowerTrain = models.CharField( "PowerTrain", max_length=500, null=True )
    PlugType = models.CharField( "PlugType", max_length=255 )
    BodyStyle = models.CharField( "BodyStyle", max_length=255 )
    Segment = models.CharField( "Segment", max_length=255 )
    Seats = models.CharField( "Seats", max_length=250 )
    PriceEuro = models.CharField( "PriceEuro", max_length=500 )
