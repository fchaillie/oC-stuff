import pandas as pd
import streamlit as st
from streamlit.components.v1 import html
import requests
import mlflow
import json
import pickle
import gzip
import base64

def main():
    

    st.markdown("<h1 style='text-align: center; black: red;'>Loan Details</h1>", unsafe_allow_html=True)

    st.text("")
    
    EXT_SOURCE_1 = st.number_input('External data source 1 score', min_value = 0., max_value = 1.)

    EXT_SOURCE_2 = st.number_input('External data source 2 score', min_value = 0., max_value = 1.)

    EXT_SOURCE_3 = st.number_input('External data source 3 score', min_value = 0., max_value = 1.)

    PAYMENT_RATE = st.number_input('Payment rate', min_value = 0., max_value = 1.)

    DAYS_BIRTH = int(st.number_input('How old is the client ?', max_value = 0., step = 1.))

    DAYS_EMPLOYED = st.number_input('How many days before the application the person started current employment ?',
                                   max_value = 0., step = 1.)

    DAYS_EMPLOYED_PERC = st.number_input('What percentage of his lifetime does the time working at the current job represents ?',
                                        min_value = 0., max_value = 1.)

    DAYS_REGISTRATION = st.number_input('How many days before the application did client change his registration ?',
                                       max_value = 0., step = 1.)
    
    DAYS_ID_PUBLISH = int(st.number_input(f'How many days before the application did client change the identity '
                                          f'document with which he applied for the loan ?', 
                                          max_value = 0., step = 1.))
    
    AMT_ANNUITY = st.number_input('Loan annuity', min_value = 0., step = 1.)
    
    ANNUITY_INCOME_PERC = st.number_input('What percentage of the monthly salary does the annuity represents ?',
                                         min_value = 0., max_value = 1.)
    
    INSTAL_DBD_MEAN = st.number_input(f'How many days before the due date for each instalment on average does '
                                     f'the client usually pay it ?',
                                     min_value = 0., step = 1.)
    
    REGION_POPULATION_RELATIVE = st.number_input('How populated is the region where the client lives ?',
                                                min_value = 0., max_value = 1.)
    

    predict_btn = st.button('Prediction')
  
    if predict_btn:

        dictio_pred = {'EXT_SOURCE_1': EXT_SOURCE_1, 'EXT_SOURCE_2': EXT_SOURCE_2, 'EXT_SOURCE_3': EXT_SOURCE_3, 
                       'PAYMENT_RATE': PAYMENT_RATE, 'DAYS_BIRTH': DAYS_BIRTH, 'DAYS_EMPLOYED': DAYS_EMPLOYED,
                       'DAYS_EMPLOYED_PERC': DAYS_EMPLOYED_PERC, 'DAYS_REGISTRATION': DAYS_REGISTRATION, 
                       'DAYS_ID_PUBLISH': DAYS_ID_PUBLISH,'AMT_ANNUITY': AMT_ANNUITY, 
                       'ANNUITY_INCOME_PERC': ANNUITY_INCOME_PERC,'INSTAL_DBD_MEAN': INSTAL_DBD_MEAN, 
                       'REGION_POPULATION_RELATIVE': REGION_POPULATION_RELATIVE}
         
        PERS_FEAT_API_URL = "https://projet7-api-0c8f5c7ce811.herokuapp.com/score/"
        response = requests.get(PERS_FEAT_API_URL, params = dictio_pred)
        st.title('Answer')
        st.text("")
        
        if float(response.content) > 0.20:
            
            text = "You can not grant a loan to this client because their default risk is above 20%"
            st.markdown(f'<div style="background-color:#4CAF50;padding:10px;border-radius:5px;'
                        f'color:white;">{text}</div>',unsafe_allow_html=True)
        else:
            
            text = "You can not grant a loan to this client because their default risk is above 20%"
            st.markdown(f'<div style="background-color:#FF6347;padding:10px;border-radius:5px;'
                        f'color:white;">{text}</div>',unsafe_allow_html=True)

        PERS_FEAT_API_URL = "https://projet7-api-0c8f5c7ce811.herokuapp.com/prediction/"
        response1 = requests.get(PERS_FEAT_API_URL, params = dictio_pred)
        exp1 = pickle.loads(response1.content)
        st.title('Personal features for this client')
        st.text("")
        html(exp1.as_html(), width = 1000, height = 250, scrolling = True)
        
        

        PERS_FEAT_API_URL = "https://projet7-api-0c8f5c7ce811.herokuapp.com/valeur_moyenne/"
        response2 = requests.get(PERS_FEAT_API_URL, params = dictio_pred)
        data = response2.json()
        data_json_str = json.dumps(data)  # Convert the dictionary to a JSON string
        resume_deserialized = pd.read_json(data_json_str, orient='split')
        st.title('Comparison with other clients')
        st.text("")
        st.write(resume_deserialized)
        

if __name__ == '__main__':
    main()
