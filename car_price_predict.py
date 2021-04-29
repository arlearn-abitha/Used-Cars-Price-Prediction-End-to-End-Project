from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regressor_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index_new.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Location = request.form['Location']
        if Location == 'Delhi':
            Location = 0
        elif Location == 'Mumbai':
            Location = 1
        elif Location == 'Kolkata':
            Location = 2
        elif Location == 'Chennai':
            Location = 3
        elif Location == 'Jaipur':
            Location = 4
        elif Location == 'Ahmedabad':
            Location = 5
        elif Location == 'Hyderabad':
            Location = 6
        elif Location == 'Coimbatore':
            Location = 7
        elif Location == 'Pune':
            Location = 8
        elif Location == 'Bangalore':
            Location = 9
        elif Location == 'Kochi':
            Location = 10
        else:
            print("Please enter a valid location name.")
        Year = int(request.form['Year'])
        Kilometers_Driven=int(request.form['Kilometers_Driven'])
        Fuel_Type=request.form['Fuel_Type']
        if(Fuel_Type == 'CNG'):
            Fuel_Type = 0
        elif(Fuel_Type == 'LPG'):
            Fuel_Type = 1
        elif(Fuel_Type == 'Petrol'):
            Fuel_Type = 2
        elif(Fuel_Type == 'Diesel'):
            Fuel_Type = 3
        else:
            Fuel_Type = 4
        Transmission=request.form['Transmission']
        if(Transmission =='Manual'):
            Transmission=0
        else:
            Transmission=1
        Year=2021-Year
        Owner_Type=request.form['Owner_Type']
        if(Owner_Type=='First'):
            Owner_Type=0
        elif(Owner_Type=='Second'):
            Owner_Type=1
        elif(Owner_Type=='Third'):
            Owner_Type=2
        else:
            Owner_Type= 3
        Mileage=float(request.form['Mileage'])
        Engine=int(request.form['Engine'])
        Seats = int(request.form['Seats'])

        prediction=model.predict([[Location, Year, Kilometers_Driven, Fuel_Type, Transmission, Owner_Type, Mileage, Engine, Seats]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index_new.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index_new.html',prediction_text="You Can Sell The Car at {} lakhs".format(output))
    else:
        return render_template('index_new.html')

if __name__=="__main__":
    app.run(debug=True)
