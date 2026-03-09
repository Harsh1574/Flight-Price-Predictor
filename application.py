from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained Lasso model
model = pickle.load(open('flight_price_lasso_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # 1. Extract Date/Time features
        date_dep = request.form["Dep_Time"]
        day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        
        dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

        date_arr = request.form["Arrival_Time"]
        arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)

        # 2. Duration calculation (simplified for the app)
        duration_hour = abs(arrival_hour - dep_hour)
        duration_min = abs(arrival_min - dep_min)

        # 3. Stops
        total_stops = int(request.form["stops"])

        # 4. Initialize all 33 features to 0 (matching your model_training.ipynb)
        # Sequence must match the order in your df.info() output
        features = np.zeros(33)
        
        # Manually map categorical inputs to the correct index in your feature array
        # Example: Airline_IndiGo might be index 3
        airline = request.form['airline']
        if airline == 'IndiGo': features[3] = 1.0
        elif airline == 'Air India': features[1] = 1.0
        # ... repeat for other airlines and sources/destinations based on your df columns
        
        # Map time/date values to the correct indices
        features[23] = day
        features[24] = month
        features[25] = 2019 # Match training year
        features[26] = total_stops
        features[27] = arrival_hour
        features[28] = arrival_min
        features[29] = dep_hour
        features[30] = dep_min
        features[31] = duration_hour
        features[32] = duration_min

        prediction = model.predict([features])
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f"Estimated Flight Price: ₹{output}")

if __name__ == "__main__":
    app.run(debug=True)