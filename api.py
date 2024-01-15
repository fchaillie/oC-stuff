# -*- coding: utf-8 -*-
import pandas as pd
import mlflow
from flask import Flask, render_template, jsonify, request
import json
import requests


app = Flask(__name__)


@app.route('/prediction/')
def askprediction():
    
    args = request.args
    
    print(args)
    
    # Your list of values
    data_list = [0.5, 0.5, 0.5, 0.5, -10000, -300,
             0.10, -100, -10, 1000, 0.10,
             5, 0.2]

    # Column names
    column_names = ['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'PAYMENT_RATE', 'DAYS_BIRTH', 'DAYS_EMPLOYED',
                'DAYS_EMPLOYED_PERC', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH', 'AMT_ANNUITY', 'ANNUITY_INCOME_PERC',
                'INSTAL_DBD_MEAN', 'REGION_POPULATION_RELATIVE']

    # Create a DataFrame
    df = pd.DataFrame([data_list], columns=column_names)


    MLFLOW_URI = 'http://127.0.0.1:7500'
        
    # Set our tracking server uri for logging
    mlflow.set_tracking_uri(uri = MLFLOW_URI)
        
        
    logged_model = 'runs:/7a48f4bbdd3e4b94bad915ee2f208b43/credit_default_model-2'

        
    loaded_model = mlflow.lightgbm.load_model(logged_model)
        
    predictions = loaded_model.predict_proba(df, num_iteration = loaded_model.best_iteration_)[:, 1]
    
    predictions = list(predictions)

#     if predictions > 0.15:
#             answer = "No loan for you angel"
#     else:
#             answer = "Loan for you angel"
            
    return predictions

if __name__ == "__main__":
    app.run(debug=True)