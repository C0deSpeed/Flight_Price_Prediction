# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:20:54 2022

@author: Godspeed
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st
import datetime

file = open('model.pickle', 'rb')
model = pickle.load(file)

def fare_pred(Duration, Total_Stops, Journey_day, Journey_month,
       Departure_hr, Departure_min, Arrival_hr, Arrival_min,
       Airline_Air_India, Airline_GoAir, Airline_IndiGo,
       Airline_Jet_Airways, Airline_Jet_Airways_Business,
       Airline_Multiple_carriers,
       Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet,
       Airline_Vistara, Airline_Vistara_Premium_economy, Source_Chennai,
       Source_Delhi, Source_Kolkata, Source_Mumbai, Destination_Chennai, Destination_Cochin,
       Destination_Delhi, Destination_Hyderabad, Destination_Kolkata):
    
    prediction = model.predict([[Duration, Total_Stops, Journey_day, Journey_month,
           Departure_hr, Departure_min, Arrival_hr, Arrival_min,
           Airline_Air_India, Airline_GoAir, Airline_IndiGo,
           Airline_Jet_Airways, Airline_Jet_Airways_Business,
           Airline_Multiple_carriers,
           Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet,
           Airline_Vistara, Airline_Vistara_Premium_economy, Source_Chennai,
           Source_Delhi, Source_Kolkata, Source_Mumbai, Destination_Chennai, Destination_Cochin,
           Destination_Delhi, Destination_Hyderabad, Destination_Kolkata]])
    return prediction

def main():
        st.title("Flight Price Predictor")
        html_temp = """
        <h5 style="color:white;text-align:left;">By Rohan Sharma</h2>
        <div style="background-color:darkblue;padding:10px">
        <h3 style="color:white;text-align:center;">Enter Information Below</h2>
        </div>
        """
        st.markdown(html_temp,unsafe_allow_html=True)
        
        #Getting flight info
        
        departure_date = st.date_input('Journey Date', datetime.date.today())
        departure_time = st.time_input('Departure Time', datetime.time(0,0))
        arrival = st.date_input('Arrival Date', datetime.date.today())
        arrival_time = st.time_input('Arrival Time', datetime.time(0,0))
        source = st.selectbox('Source', ('Chennai', 'Delhi', 'Kolkata', 'Mumbai'))
        destination = st.selectbox('Destination',('Chennai', 'Cochin', 'Delhi', 'Hyderabad', 'Kolkata'))
        stops = st.selectbox('Stops', ('non-stop', '2 stops', '1 stop', '3 stops', '4 stops'))
        airline = st.selectbox('Airline', ('Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business', 
                       'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet', 
                       'Vistara', 'Vistara Premium economy'))
        
        #Departure
        
        Journey_day = departure_date.day
        Journey_month = departure_date.month
        Departure_hr = departure_time.hour
        Departure_min = departure_time.minute
        
        #Arrival
        
        Arrival_hr = arrival_time.hour
        Arrival_min = arrival_time.minute
        
        #Duration
        
        Duration = abs(Arrival_hr-Departure_hr)*60 + abs(Arrival_min-Departure_min)
        
        #Total Stops
        
        stops_dict = {'non-stop':0, '1 stop':1, '2 stops':2, '3 stops':3, '4 stops':4}
        Total_Stops = stops_dict[stops]
        
        #Airline
        
        airline_lst = ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business', 
                       'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet', 
                       'Vistara', 'Vistara Premium economy']
        
        Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
        Airline_Jet_Airways, Airline_Jet_Airways_Business, \
        Airline_Multiple_carriers, \
        Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
        Airline_Vistara, Airline_Vistara_Premium_economy = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        
        if airline == airline_lst[0]:
            Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
            Airline_Jet_Airways, Airline_Jet_Airways_Business, \
            Airline_Multiple_carriers, \
            Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
            Airline_Vistara, Airline_Vistara_Premium_economy = 1, 0, 0, 0, 0, 0, 0, 0, 0, 0
            
        if airline == airline_lst[1]:
            Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
            Airline_Jet_Airways, Airline_Jet_Airways_Business, \
            Airline_Multiple_carriers, \
            Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
            Airline_Vistara, Airline_Vistara_Premium_economy = 0, 1, 0, 0, 0, 0, 0, 0, 0, 0
            
        if airline == airline_lst[2]:
            Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
            Airline_Jet_Airways, Airline_Jet_Airways_Business, \
            Airline_Multiple_carriers, \
            Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
            Airline_Vistara, Airline_Vistara_Premium_economy = 0, 0, 1, 0, 0, 0, 0, 0, 0, 0
            
        if airline == airline_lst[3]:
            Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
            Airline_Jet_Airways, Airline_Jet_Airways_Business, \
            Airline_Multiple_carriers, \
            Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
            Airline_Vistara, Airline_Vistara_Premium_economy = 0, 0, 0, 1, 0, 0, 0, 0, 0, 0
            
        if airline == airline_lst[4]:
            Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
            Airline_Jet_Airways, Airline_Jet_Airways_Business, \
            Airline_Multiple_carriers, \
            Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
            Airline_Vistara, Airline_Vistara_Premium_economy = 0, 0, 0, 0, 1, 0, 0, 0, 0, 0
            
        if airline == airline_lst[5]:
            Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
            Airline_Jet_Airways, Airline_Jet_Airways_Business, \
            Airline_Multiple_carriers, \
            Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
            Airline_Vistara, Airline_Vistara_Premium_economy = 0, 0, 0, 0, 0, 1, 0, 0, 0, 0
            
        if airline == airline_lst[6]:
            Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
            Airline_Jet_Airways, Airline_Jet_Airways_Business, \
            Airline_Multiple_carriers, \
            Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
            Airline_Vistara, Airline_Vistara_Premium_economy = 0, 0, 0, 0, 0, 0, 1, 0, 0, 0
            
        if airline == airline_lst[7]:
            Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
            Airline_Jet_Airways, Airline_Jet_Airways_Business, \
            Airline_Multiple_carriers, \
            Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
            Airline_Vistara, Airline_Vistara_Premium_economy = 0, 0, 0, 0, 0, 0, 0, 1, 0, 0
            
        if airline == airline_lst[8]:
            Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
            Airline_Jet_Airways, Airline_Jet_Airways_Business, \
            Airline_Multiple_carriers, \
            Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
            Airline_Vistara, Airline_Vistara_Premium_economy = 0, 0, 0, 0, 0, 0, 0, 0, 1, 0
            
        if airline == airline_lst[9]:
            Airline_Air_India, Airline_GoAir, Airline_IndiGo, \
            Airline_Jet_Airways, Airline_Jet_Airways_Business, \
            Airline_Multiple_carriers, \
            Airline_Multiple_carriers_Premium_economy, Airline_SpiceJet, \
            Airline_Vistara, Airline_Vistara_Premium_economy = 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
            
        #Source
        
        source_lst = ['Chennai', 'Delhi', 'Kolkata', 'Mumbai']
        
        Source_Chennai, \
        Source_Delhi, Source_Kolkata, Source_Mumbai = 0, 0, 0, 0
        
        if source == source_lst[0]:
            Source_Chennai, \
            Source_Delhi, Source_Kolkata, Source_Mumbai = 1, 0, 0, 0
            
        if source == source_lst[1]:
            Source_Chennai, \
            Source_Delhi, Source_Kolkata, Source_Mumbai = 0, 1, 0, 0
            
        if source == source_lst[2]:
            Source_Chennai, \
            Source_Delhi, Source_Kolkata, Source_Mumbai = 0, 0, 1, 0
            
        if source == source_lst[3]:
            Source_Chennai, \
            Source_Delhi, Source_Kolkata, Source_Mumbai = 0, 0, 0, 1
            
        
        #Destination
        
        destination_lst = ['Chennai', 'Cochin', 'Delhi', 'Hyderabad', 'Kolkata']
        
        Destination_Chennai, Destination_Cochin, \
        Destination_Delhi, Destination_Hyderabad, Destination_Kolkata = 0, 0, 0, 0, 0
        
        if destination == destination_lst[0]:
            Destination_Chennai, Destination_Cochin, \
            Destination_Delhi, Destination_Hyderabad, Destination_Kolkata = 1, 0, 0, 0, 0
        
        if destination == destination_lst[1]:
            Destination_Chennai, Destination_Cochin, \
            Destination_Delhi, Destination_Hyderabad, Destination_Kolkata = 0, 1, 0, 0, 0
        
        if destination == destination_lst[2]:
            Destination_Chennai, Destination_Cochin, \
            Destination_Delhi, Destination_Hyderabad, Destination_Kolkata = 0, 0, 1, 0, 0
        
        if destination == destination_lst[3]:
            Destination_Chennai, Destination_Cochin, \
            Destination_Delhi, Destination_Hyderabad, Destination_Kolkata = 0, 0, 0, 1, 0
        
        if destination == destination_lst[4]:
            Destination_Chennai, Destination_Cochin, \
            Destination_Delhi, Destination_Hyderabad, Destination_Kolkata = 0, 0, 0, 0, 1
            
            
        #Prediction
        
        if st.button('Predict'):
                     if Source==Destination:
                            st.write("You can't put same Source and Destination!")
                     else:
                          st.success('The Predicted Price Is:\n')
                          output = fare_pred(Duration, Total_Stops, Journey_day, Journey_month,\
                                             Departure_hr, Departure_min, Arrival_hr, Arrival_min,\
                                                 Airline_Air_India, Airline_GoAir, Airline_IndiGo,\
                                                     Airline_Jet_Airways, Airline_Jet_Airways_Business,\
                                                         Airline_Multiple_carriers,\
                                                             Airline_Multiple_carriers_Premium_economy,\
                                                                 Airline_SpiceJet, Airline_Vistara,\
                                                                     Airline_Vistara_Premium_economy,\
                                                                         Source_Chennai, Source_Delhi, Source_Kolkata,\
                                                                             Source_Mumbai, Destination_Chennai, Destination_Cochin,\
                                                                                 Destination_Delhi, Destination_Hyderabad, Destination_Kolkata)
                            st.write(f'₹{round(output,2)}')

             
            
                
        
        
if __name__ =='__main__':
    main()
