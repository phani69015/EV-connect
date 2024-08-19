from django.shortcuts import render
from .models import CarDetail
from django.http import HttpResponse
import joblib
import numpy as np


#model = joblib.load('')  # Update with the actual path to your model file

def home(request):
    return render(request, 'home.html')

def find_my_ev(request):
    # Default car list is empty
    cars = []
    
    # Fetch brands for the filter
    brands = CarDetail.objects.values_list('brand', flat=True).distinct()
    
    # Extract filter parameters
    brand = request.GET.get('brand')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    range_min = request.GET.get('range_min')
    range_max = request.GET.get('range_max')
    rapid_charge = request.GET.get('rapid_charge')
    top_speed_min = request.GET.get('top_speed_min')
    top_speed_max = request.GET.get('top_speed_max')

    # Check if any filter is applied
    if any([brand, price_min, price_max, range_min, range_max, rapid_charge, top_speed_min, top_speed_max]):
        cars = CarDetail.objects.all()
        
        # Apply filters
        if brand and brand != 'NA':
            cars = cars.filter(brand=brand)
        if price_min:
            cars = cars.filter(price_euro__gte=price_min)
        if price_max:
            cars = cars.filter(price_euro__lte=price_max)
        if range_min:
            cars = cars.filter(range_km__gte=range_min)
        if range_max:
            cars = cars.filter(range_km__lte=range_max)
        if rapid_charge:
            cars = cars.filter(rapid_charge=rapid_charge)
        if top_speed_min:
            cars = cars.filter(top_speed_kmh__gte=top_speed_min)
        if top_speed_max:
            cars = cars.filter(top_speed_kmh__lte=top_speed_max)

    return render(request, 'find_my_ev.html', {'cars': cars, 'brands': brands})

# Load the trained model (ensure the model is saved as 'decision_tree_model.joblib')


# Encoding dictionaries
brand_encoding = {
    'Tesla': 0, 'Volkswagen': 1, 'Polestar': 2, 'BMW': 3, 'Honda': 4,
    'Lucid': 5, 'Peugeot': 6, 'Audi': 7, 'Mercedes': 8, 'Nissan': 9,
    'Hyundai': 10, 'Porsche': 11, 'MG': 12, 'Mini': 13, 'Opel': 14,
    'Skoda': 15, 'Volvo': 16, 'Kia': 17, 'Renault': 18, 'Mazda': 19,
    'Lexus': 20, 'CUPRA': 21, 'SEAT': 22, 'Lightyear': 23, 'Aiways': 24,
    'DS': 25, 'Citroen': 26, 'Jaguar': 27, 'Ford': 28, 'Byton': 29,
    'Sono': 30, 'Smart': 31, 'Fiat': 32
}

rapid_charge_encoding = {'Yes': 1, 'No': 0}

powertrain_encoding = {'AWD': 0, 'RWD': 1, 'FWD': 2}

plug_type_encoding = {
    'Type 2 CCS': 0, 'Type 2 CHAdeMO': 1, 'Type 2': 2, 'Type 1 CHAdeMO': 3
}

body_style_encoding = {
    'Sedan': 0, 'Hatchback': 1, 'Liftback': 2, 'SUV': 3, 'Pickup': 4,
    'MPV': 5, 'Cabrio': 6, 'SPV': 7, 'Station': 8
}

segment_encoding = {
    'D': 0, 'C': 1, 'B': 2, 'F': 3, 'A': 4, 'E': 5, 'N': 6, 'S': 7
}

def predict_my_ev(request):
    brands = CarDetail.objects.values_list('brand', flat=True).distinct()
    predicted_price = None
    model = joblib.load('C:\Projects\EV-connect\evconnect\cars\decision_tree_model.joblib')
    if request.method == 'POST':
        # Extract form data
        brand = request.POST.get('brand')
        accel_sec = float(request.POST.get('accel_sec', 0))
        top_speed_kmh = float(request.POST.get('top_speed_kmh', 0))
        range_km = float(request.POST.get('range_km', 0))
        efficiency_whkm = float(request.POST.get('efficiency_whkm', 0))
        fast_charge_kmh = float(request.POST.get('fast_charge_kmh', 0))
        rapid_charge = request.POST.get('rapid_charge')
        powertrain = request.POST.get('powertrain')
        plug_type = request.POST.get('plug_type')
        body_style = request.POST.get('body_style')
        segment = request.POST.get('segment')
        seats = int(request.POST.get('seats', 0))

        # Manually encode categorical features
        encoded_brand = brand_encoding.get(brand, -1)
        encoded_rapid_charge = rapid_charge_encoding.get(rapid_charge, 0)
        encoded_powertrain = powertrain_encoding.get(powertrain, -1)
        encoded_plug_type = plug_type_encoding.get(plug_type, -1)
        encoded_body_style = body_style_encoding.get(body_style, -1)
        encoded_segment = segment_encoding.get(segment, -1)

        # Prepare input data for prediction
        input_data = [[
            encoded_brand, accel_sec, top_speed_kmh, range_km, efficiency_whkm,
            fast_charge_kmh, encoded_rapid_charge, encoded_powertrain, 
            encoded_plug_type, encoded_body_style, encoded_segment, seats
        ]]
  
        # Predict price
        predicted_price = model.predict(input_data)[0]

    return render(request, 'predict_my_ev.html', {'brands': brands, 'predicted_price': predicted_price})