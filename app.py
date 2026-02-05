from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model/car_price_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    km_driven = float(request.form['kms_driven'])
    car_age = float(request.form['car_age'])

    # Fuel encoding
    fuel = request.form['fuel']
    fuel_Diesel = 1 if fuel == "Diesel" else 0
    fuel_Electric = 1 if fuel == "Electric" else 0
    fuel_LPG = 1 if fuel == "LPG" else 0
    fuel_Petrol = 1 if fuel == "Petrol" else 0

    # Seller type encoding
    seller = request.form['seller_type']
    seller_type_Individual = 1 if seller == "Individual" else 0
    seller_type_Trustmark_Dealer = 1 if seller == "Trustmark Dealer" else 0

    # Transmission encoding
    transmission = request.form['transmission']
    transmission_Manual = 1 if transmission == "Manual" else 0

    # Owner encoding
    owner = request.form['owner']
    owner_Fourth_Above = 1 if owner == "Fourth & Above Owner" else 0
    owner_Second = 1 if owner == "Second Owner" else 0
    owner_Test_Drive = 1 if owner == "Test Drive Car" else 0
    owner_Third = 1 if owner == "Third Owner" else 0

    features = [[
        km_driven,
        car_age,
        fuel_Diesel,
        fuel_Electric,
        fuel_LPG,
        fuel_Petrol,
        seller_type_Individual,
        seller_type_Trustmark_Dealer,
        transmission_Manual,
        owner_Fourth_Above,
        owner_Second,
        owner_Test_Drive,
        owner_Third
    ]]

    prediction = model.predict(features)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f"Estimated Selling Price: ₹ {output}")

if __name__ == "__main__":
    app.run(debug=True)