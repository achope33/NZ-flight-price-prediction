from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # Sounds_Air = 0 (not in column)
        airline=request.form['Airline']
        if(airline=='Air New Zealand'):
            Air_New_Zealand = 1
            Jetstar = 0
           

        elif (airline=='Jetstar'):
            Air_New_Zealand = 0
            Jetstar = 1
           

        else:
            Air_New_Zealand = 0
            Jetstar = 0
          

        # print(Air_New_Zealand,
        #     Jetstar)

        # Source
        # Queenstown = 0 (not in column)
        Source = request.form["Source"]
        if (Departure == 'Wellington'):
            Dept_WLG = 1
            Dept_CHC = 0
            Dept_AKL = 0


        elif (Departure == 'Christchurch'):
            Dept_WLG = 0
            Dept_CHC = 1
            Dept_AKL = 0


        elif (Departure == 'Auckland'):
            Dept_WLG = 0
            Dept_CHC = 0
            Dept_AKL = 1



        else:
            Dept_WLG = 0
            Dept_CHC = 0
            Dept_AKL = 0

        # print(Dept_WLG,
        #     Dept_CHC,
        #     Dept_AKL)

        # Destination
        # Wellington = 0 (not in column)
        Destination = request.form["Destination"]
        if (Destination == 'Nelson'):
            Arr_NSN = 1
            Arr_AKL = 0
            Arr_PMR = 0
            Arr_CHC = 0
            Arr_ZQN = 0
            Arr_NPE = 0
            Arr_NPL = 0
            Arr_DUD = 0

        elif (Destination == 'Auckland'):
            Arr_NSN = 0
            Arr_AKL = 1
            Arr_PMR = 0
            Arr_CHC = 0
            Arr_ZQN = 0
            Arr_NPE = 0
            Arr_NPL = 0
            Arr_DUD = 0

        elif (Destination == 'Palmerston_North'):
            Arr_NSN = 0
            Arr_AKL = 0
            Arr_PMR = 1
            Arr_CHC = 0
            Arr_ZQN = 0
            Arr_NPE = 0
            Arr_NPL = 0
            Arr_DUD = 0

        elif (Destination == 'Christchurch'):
            Arr_NSN = 0
            Arr_AKL = 0
            Arr_PMR = 0
            Arr_CHC = 1
            Arr_ZQN = 0
            Arr_NPE = 0
            Arr_NPL = 0
            Arr_DUD = 0

        elif (Destination == 'Queentown'):
            Arr_NSN = 0
            Arr_AKL = 0
            Arr_PMR = 0
            Arr_CHC = 0
            Arr_ZQN = 1
            Arr_NPE = 0
            Arr_NPL = 0
            Arr_DUD = 0

        elif (Destination == 'Hawkes_Bay'):
            Arr_NSN = 0
            Arr_AKL = 0
            Arr_PMR = 0
            Arr_CHC = 0
            Arr_ZQN = 0
            Arr_NPE = 1
            Arr_NPL = 0
            Arr_DUD = 0

        elif (Destination == 'New_Plymonth'):
            Arr_NSN = 0
            Arr_AKL = 0
            Arr_PMR = 0
            Arr_CHC = 0
            Arr_ZQN = 0
            Arr_NPE = 0
            Arr_NPL = 1
            Arr_DUD = 0

        elif (Destination == 'Dunedin'):
            Arr_NSN = 0
            Arr_AKL = 0
            Arr_PMR = 0
            Arr_CHC = 0
            Arr_ZQN = 0
            Arr_NPE = 0
            Arr_NPL = 0
            Arr_DUD = 1

        else:
            Arr_NSN = 0
            Arr_AKL = 0
            Arr_PMR = 0
            Arr_CHC = 0
            Arr_ZQN = 0
            Arr_NPE = 0
            Arr_NPL = 0
            Arr_DUD = 0

        # print(
        #     Arr_NSN,
        #     Arr_AKL,
        #     Arr_PMR,
        #     Arr_CHC,
        #     Arr_ZQN,
        #     Arr_NPE,
        #     Arr_NPL,
        #     Arr_DUD
        # )
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Sounds Air', 'Airline_Jetstar',
    #    'Airline_Air New Zealand', 
    #    'Source_Auckland', 'Source_Christchurch', 'Source_Wellington', 
    #    'Destination_Nelson', 'Destination_Auckland', 'Destination_Palmerston North',
    #    'Destination_Christchurch', 'Destination_Queenstown','Destination_Hawke's Bay',
    #    'Destination_New Plymonth','Destination_Dunedin']
        
        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Sounds_Air,
            Jetstar,
            Air_New_Zealand,
            s_WLG,
            s_CHC,
            s_AKL,
            d_NSN,
            d_AKL,
            d_PMR,
            d_CHC,
            d_ZQN,
            d_NPE,
            d_NPL,
            d_DUD
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is NZD. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
