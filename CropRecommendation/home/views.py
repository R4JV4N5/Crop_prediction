from django.shortcuts import render
import requests
from urllib.request import urlopen
import json
from .forms import weather_form
import numpy as np
import pandas as pd
import sklearn
import pickle
def home(request):
    
# weather 

    weather_api_key = "cad2fdbd5d1f0cc6688857d834a932b2"
    pix_api = '38089315-da5bbad1b7bfa685bbf80625e'
    url = 'http://ipinfo.io/json'
    # weather data 
    weather_response = urlopen(url)
    data = json.load(weather_response)
    city=data['city']
    weather_url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric')
    weather_data = weather_url.json()  
    weather_data = weather_url.json()
    print(weather_data)
    temp = round(weather_data['main']['temp']) 
    humidity = weather_data['main']['humidity'] 
    wind_speed = weather_data['wind']['speed']
    weather_type = weather_data['weather'][0]['main']

  # image requests
    pix_url = requests.get(f'https://pixabay.com/api/?key={pix_api}&q={weather_type}&image_type=photo&pretty=true')
    pix_data= pix_url.json()
    # print(pix_data)

    model = pickle.load(open("C:/Users/rajve/OneDrive/Desktop/code/ds_project/Crop_prediction/CropRecommendation/home/model/nbModel.pkl" , 'rb'))


#  condition request
    if request.method == 'POST':
        form = weather_form(request.POST)
        if form.is_valid():
            N = form.cleaned_data['Nitrogen']
            P = form.cleaned_data['Phosphorous']
            K = form.cleaned_data['Pottasium']
            temp = form.cleaned_data['Temperature']
            humidity = form.cleaned_data['Humidity']
            pH = form.cleaned_data['pH']
            rainfall = form.cleaned_data['Rainfall']

            feature_list = [N , P , K , temp,humidity,pH,rainfall]
            single_pred = np.array(feature_list).reshape(1,-1)

            prediction = model.predict(single_pred)
            crop_dict = {'rice': 1,
             'maize': 2,
             'chickpea': 3,
             'kidneybeans': 4,
             'pigeonpeas': 5,
             'mothbeans': 6,
             'mungbean': 7,
             'blackgram': 8,
             'lentil': 9,
             'pomegranate': 10,
             'banana': 11,
             'mango': 12,
             'grapes': 13,
             'watermelon': 14,
             'muskmelon': 15,
             'apple': 16,
             'orange': 17,
             'papaya': 18,
             'coconut': 19,
             'cotton': 20,
             'jute': 21,
             'coffee': 22}



            if prediction[0] in crop_dict.values():
                value = [i for i in crop_dict if crop_dict[i] == prediction[0]]
                print(value)
                result = f' most suitable crop for provided feature is {value[0]}'
            else:
                result = 'sorry no crop found for provided feature '

            res = {
                    'result' : result
                }


            return render(request , 'home/result.html' , res)
    else:
        form = weather_form()

        context = {
            'form' :form,
        'city':city,
          'temp':temp,
          'humidity' :humidity,
          'wind_speed' :wind_speed
    }

    return render(request, 'home/crop.html' , context )




