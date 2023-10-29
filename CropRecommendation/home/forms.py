from django import forms


class weather_form(forms.Form):
    Nitrogen = forms.IntegerField(
        min_value=0,
        required=True,
        initial=0)
    Phosphorous = forms.IntegerField(
        min_value=0,
        required=True,
        initial=0)
    Pottasium = forms.IntegerField(
        min_value=0,
        required=True,
        initial=0)
    Temperature = forms.FloatField(
        min_value=0.0,
        required=True,
        initial=0.0)
    Humidity = forms.FloatField(
        min_value=0.0,
        required=True,
        initial=0.0)

    pH = forms.FloatField(
        min_value=0.0,
        required=True,
        initial=0.0)

    Rainfall = forms.FloatField(
        min_value=0.0,
        required=True,
        initial=0.0)
