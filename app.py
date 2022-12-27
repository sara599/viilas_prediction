from copyreg import pickle
import re
from flask import Flask,request,render_template
from distutils.log import debug
from Helpers.Dummies import *
import joblib
import pickle


app = Flask(__name__)  #make the curent page flask app
app.debug = True
model = pickle.load(open('models/xgb.pkl' , 'rb')  )
scaler = joblib.load('models/scaler.h5')


# @--> fun decoratot 
@app.route('/' , methods=['GET'] ) #'/' home page  , route-->define url
def home():
    return render_template('index.html')




@app.route('/predict' , methods=['POST'] ) #'/' home page  , route-->define url
def predict():
    
    all_data = request.form
    
    Area = int(all_data['Area'])
    down_payment = int(all_data['down_payment'])
    
    bedrooms = int(all_data['bedrooms'])
    bathrooms = int(all_data['bathrooms'])
    
    country = con_dum[all_data['Country']]
    location = loc_dum[all_data['location']]
    compound = com_dum[all_data['compound']]
    
    payment_option = payment_dum[all_data['payment_option']]
    delivery_term = float(all_data['delivery_term'])
    delivery_date = int(all_data['Delivery_Date'])
    Type = int(all_data['Type'])
    month=int(all_data['month'])
    
    negotiable = int(all_data['negotiable'])
    finished = int(all_data['finished'])
    electricity_meter = int(all_data['electricity_meter'])
    balcony = int(all_data['balcony'])
    water_meter = int(all_data['water_meter'])
    elevator = int(all_data['elevator'])
    security=int(all_data['security'])
    private_garden = int(all_data['private_garden'])
    natural_gas = int(all_data['natural_gas'])
    pool = int(all_data['pool'])
    pets_allowed= int(all_data['Pets_Allowed'])
    landline  = int(all_data['Landline'])
    built_in_kitchen  = int(all_data['Built_in_Kitchen'])
    appliances = int(all_data['Appliances'])
    maids_room = int(all_data['Maids_Room'])
    central_conditioner_heating = int(all_data['Central_conditioner_heating'])
    covered_parking = int(all_data['Covered_Parking'])
    
    x = [ negotiable  , bedrooms , bathrooms , Area , Type , delivery_term , finished , 
         delivery_date , down_payment , month , payment_option , balcony , pets_allowed , private_garden,
         security , electricity_meter , water_meter ,  natural_gas , landline , built_in_kitchen,
         appliances , maids_room ,covered_parking ,central_conditioner_heating , pool ,elevator,
         location ,compound  ,country ]
    
    temp = []
    for item in x:
        if type(item) == list:
            temp.extend(item)
        else:
            temp.append(item)
    x = temp
         
    print(x, len(x), len(scaler.scale_))

    x = scaler.transform([x])
    price = round(model.predict(x)[0])
    
    return render_template('prediction.html', price=price)




if __name__ == '__main__':
    app.run()#run server with my ip , 
    # flask convert this file to web servers