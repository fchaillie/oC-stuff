import pandas as pd
import streamlit as st
from streamlit.components.v1 import html
import requests
import mlflow
import json
import pickle
import gzip


def main():
    
    
    st.title('You will get your loan or not, cano ?')

    EXT_SOURCE_1 = st.number_input('EXT_SOURCE_1', min_value = 0., max_value = 1.)

    EXT_SOURCE_2 = st.number_input('EXT_SOURCE_2', min_value = 0., max_value = 1.)

    EXT_SOURCE_3 = st.number_input('EXT_SOURCE_3', min_value = 0., max_value = 1.)

    PAYMENT_RATE = st.number_input('PAYMENT_RATE', min_value = 0., max_value = 1.)

    DAYS_BIRTH = int(st.number_input('DAYS_BIRTH', max_value = 0., step = 1.))

    DAYS_EMPLOYED = st.number_input('DAYS_EMPLOYED', max_value = 0., step = 1.)

    DAYS_EMPLOYED_PERC = st.number_input('DAYS_EMPLOYED_PERC', min_value = 0., max_value = 1.)

    DAYS_REGISTRATION = st.number_input('DAYS_REGISTRATION', max_value = 0., step = 1.)
    
    DAYS_ID_PUBLISH = int(st.number_input('DAYS_ID_PUBLISH', max_value = 0., step = 1.))
    
    AMT_ANNUITY = st.number_input('AMT_ANNUITY', min_value = 0., step = 1.)
    
    ANNUITY_INCOME_PERC = st.number_input('ANNUITY_INCOME_PERC', min_value = 0., max_value = 1.)
    
    INSTAL_DBD_MEAN = st.number_input('INSTAL_DBD_MEAN', min_value = 0., step = 1.)
    
    REGION_POPULATION_RELATIVE = st.number_input('REGION_POPULATION_RELATIVE', min_value = 0., max_value = 1.)
    

    predict_btn = st.button('Prédire')
    
    pred = None
    answer = None
    
  
    
    if predict_btn:
        
   
        
        dictio_pred = {'EXT_SOURCE_1': EXT_SOURCE_1, 'EXT_SOURCE_2': EXT_SOURCE_2, 'EXT_SOURCE_3': EXT_SOURCE_3, 
                       'PAYMENT_RATE': PAYMENT_RATE, 'DAYS_BIRTH': DAYS_BIRTH, 'DAYS_EMPLOYED': DAYS_EMPLOYED,
                       'DAYS_EMPLOYED_PERC': DAYS_EMPLOYED_PERC, 'DAYS_REGISTRATION': DAYS_REGISTRATION, 
                       'DAYS_ID_PUBLISH': DAYS_ID_PUBLISH,'AMT_ANNUITY': AMT_ANNUITY, 
                       'ANNUITY_INCOME_PERC': ANNUITY_INCOME_PERC,'INSTAL_DBD_MEAN': INSTAL_DBD_MEAN, 
                       'REGION_POPULATION_RELATIVE': REGION_POPULATION_RELATIVE}
         
        PERS_FEAT_API_URL = "http://127.0.0.1:5000/score/"
        response = requests.get(PERS_FEAT_API_URL, params = dictio_pred)
        st.write(float(response.content))
        
        
        PERS_FEAT_API_URL = "http://127.0.0.1:5000/prediction/"
        response1 = requests.get(PERS_FEAT_API_URL, params = dictio_pred)
     
        exp1 = pickle.loads(response1.content)

        html(exp1.as_html(), width = 1000, height = 800, scrolling = True)



if __name__ == '__main__':
    main()
