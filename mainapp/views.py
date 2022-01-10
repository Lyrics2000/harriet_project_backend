from datetime import date
from django.db import close_old_connections
from django.shortcuts import render
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
import numpy as np


from .statistical_prediction import ad_test
import pandas as pd
from .models import (
    Sliderr,
    ImageOne,
    AboutUs,
    Mushroom,
    OurSerices,
    Backrgoundd,
    MushroomPrediction
)

# Create your views here.
# check if dataset is stationary or not using akaike information criterion


def index(request):
    slider =  Sliderr.objects.all()
    one_img =  ImageOne.objects.first()
    about_us =  AboutUs.objects.first()
    mushroom =  Mushroom.objects.all()
    our_services =  OurSerices.objects.all()
    background =  Backrgoundd.objects.first()
    prediction = MushroomPrediction.objects.all()
    prediction_values =  MushroomPrediction.objects.values()
    prediction_pandas = pd.DataFrame(prediction_values)
    df=prediction_pandas.dropna()
    closing_prices = list(df['closing_price'])
    dates = list(df['mushroom_date_price'])
    print(list(df['closing_price']))
    print(dates)

    dd = ad_test(closing_prices)
    print(str(dd))
    # determining the order of our model
    stepwise_fit = auto_arima(closing_prices, trace=True,suppress_warnings=True)
    print(stepwise_fit)
    # split dataset into training and prediction
    total_data_length = len(closing_prices)/2 - 3
    print(total_data_length)
    train=df.iloc[:-int(total_data_length)]
    test=df.iloc[-int(total_data_length):]
    print(train)


    # final prediction
    dmk = train['closing_price']
    listt = []
    for i in dmk:
        listt.append(float(i))

    print(listt,"listt")

    
    
    model=ARIMA(np.asanyarray(listt),order=(1,1,0))
    model=model.fit()
    pred = model.summary()
    print(str(pred))

    start=len(train)
    end=len(train)+len(test)-1
    preddd=model.predict(start=start,end=end,typ='levels')
    print("predicted price",str(preddd))
    # pred.plot(legend=True)
    # test['AvgTemp'].plot(legend=True)
    


    context = {
        'slider' :  slider,
        'one_img' :  one_img,
        'about_us' :  about_us,
        'mushroom' : mushroom,
        'our_services' :  our_services,
        'background' :  background,
        'prediction' : prediction,
        'clossing_dates' : closing_prices,
        'labels' :  dates,
        'ad_values' :  dd,
        'order' :  stepwise_fit,
        'train' :  train,
        'test' :  test ,
        'model_summary' : str(preddd)
 
    }
    return render(request,'index.html',context)

# def about(request):
#     return render(request,'about.html')


# def health_benefits(request):
#     return render(request,'health_benefit.html')
