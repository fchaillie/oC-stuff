# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import mlflow
from flask import Flask, render_template, jsonify, request
import json
import requests
from lime import lime_tabular
import pickle

app = Flask(__name__)
    

@app.route("/prediction")
def askpersonalfeatures():
    
    
    train_df = pd.read_csv('train_df_less_features.csv')
    feats = ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3", "PAYMENT_RATE", "DAYS_BIRTH", "DAYS_EMPLOYED",
             "DAYS_EMPLOYED_PERC", "DAYS_REGISTRATION", "DAYS_ID_PUBLISH", "AMT_ANNUITY", "ANNUITY_INCOME_PERC",
             "INSTAL_DBD_MEAN", "REGION_POPULATION_RELATIVE"]
    train_df = train_df[feats]
    
#     args = request.args
#     df = pd.DataFrame([args])
#     # Convert all columns to floats
#     df = df.map(lambda x: pd.to_numeric(x, errors='coerce'))
    
   # load the model from disk
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

#     MLFLOW_URI = 'http://127.0.0.1:7500'
#     mlflow.set_tracking_uri(uri = MLFLOW_URI) 
#     logged_model = 'runs:/4af57f379fb148da9a95085ec4621d9b/credit_default_model-2' 
#     loaded_model = mlflow.lightgbm.load_model(logged_model) # à remplacer par pickle .load une fois que j'ai bien le fichier en dur
#     # save the model to disk
#     filename = 'finalized_model.sav'
#     pickle.dump(loaded_model, open(filename, 'wb'))
    # pickle.dump(loaded_model,"happy_file")
    # faire tourner une fois pour crééer le modèle puis supprimer ces lignes pour n'avoir que la ligne pickle
    
    # Création de l'explainer
    explainer = lime_tabular.LimeTabularExplainer(train_df.values, 
                                                  feature_names = feats, 
                                                  class_names = ['0','1'], 
                                                  verbose = True, 
                                                  mode = 'classification',
                                                  discretize_continuous=False)
    
    
    exp = explainer.explain_instance(train_df.values[0],loaded_model.predict_proba, num_features = 12)  
        
    # return pickle.dumps(exp)
    return list(train_df.values[0])

if __name__ == "__main__":
    app.run(debug=True)