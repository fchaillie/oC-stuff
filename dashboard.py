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
    
    # Defining the buttons

    st.markdown("<h1 style='text-align: center; black: red;'>Loan Details</h1>", unsafe_allow_html=True)

    st.text("")
    
    EXT_SOURCE_1 = st.number_input('External data source 1 score [1-100]', min_value = 0., max_value = 100., step = 1.) / 100

    EXT_SOURCE_2 = st.number_input('External data source 2 score [1-100]', min_value = 0., max_value = 100., step = 1.) / 100

    EXT_SOURCE_3 = st.number_input('External data source 3 score [1-100]', min_value = 0., max_value = 100., step = 1.) / 100

    PAYMENT_RATE = st.number_input('Annual payment rate: [1-100]', min_value = 0., max_value = 100., step = 1.) / 100

    DAYS_BIRTH = int(st.number_input('How old is the client ?', min_value = 0., max_value = 150., step = 1.) * (-365))

    DAYS_EMPLOYED = st.number_input('How many days before the application the person started current employment ?',
                                   min_value = 0., max_value = 1000000., step = 1.) * (-1)

    DAYS_EMPLOYED_PERC = st.number_input('What percentage of his lifetime does the time working at the current job represents ? [1-100]',
                                        min_value = 0., max_value = 100., step = 1.) / 100

    DAYS_REGISTRATION = st.number_input('How many days before the application did client change his registration ?',
                                       min_value = 0., max_value = 1000000., step = 1.) * (-1)
    
    DAYS_ID_PUBLISH = int(st.number_input(f'How many days before the application did client change the identity '
                                          f'document with which he applied for the loan ?', 
                                          min_value = 0., max_value = 1000000., step = 1.) * (-1))
    
    AMT_ANNUITY = st.number_input('Loan annuity', min_value = 0., step = 1.)
    
    ANNUITY_INCOME_PERC = st.number_input('What percentage of the yearly salary does the annuity represents ? [1-100]',
                                         min_value = 0., max_value = 100., step = 1.) / 100
    
    INSTAL_DBD_MEAN = st.number_input(f'How many days before the due date for each instalment on average does '
                                     f'the client usually pay it ?',
                                     min_value = 0., step = 1.)
    
    REGION_POPULATION_RELATIVE = st.number_input('How populated is the region where the client lives ? [1-7]',
                                                min_value = 1., max_value = 7., step = 1.) / 100
    

    # Prediction button definition with the actions that will take place

    predict_btn = st.button('Prediction')
  
    if predict_btn:

        dictio_pred = {'EXT_SOURCE_1': EXT_SOURCE_1, 'EXT_SOURCE_2': EXT_SOURCE_2, 'EXT_SOURCE_3': EXT_SOURCE_3, 
                       'PAYMENT_RATE': PAYMENT_RATE, 'DAYS_BIRTH': DAYS_BIRTH, 'DAYS_EMPLOYED': DAYS_EMPLOYED,
                       'DAYS_EMPLOYED_PERC': DAYS_EMPLOYED_PERC, 'DAYS_REGISTRATION': DAYS_REGISTRATION, 
                       'DAYS_ID_PUBLISH': DAYS_ID_PUBLISH,'AMT_ANNUITY': AMT_ANNUITY, 
                       'ANNUITY_INCOME_PERC': ANNUITY_INCOME_PERC,'INSTAL_DBD_MEAN': INSTAL_DBD_MEAN, 
                       'REGION_POPULATION_RELATIVE': REGION_POPULATION_RELATIVE}
        
        # We are getting from the API the prediction score 
        PERS_FEAT_API_URL = "https://projet7-api-0c8f5c7ce811.herokuapp.com/score/"
        # PERS_FEAT_API_URL = "http://127.0.0.1:5000/score/"
        response = requests.get(PERS_FEAT_API_URL, params = dictio_pred)
        st.title('Answer')
        st.text("")
        
        # The decisiosn for the loan will depends if the prediction score is above the threshold decided
        if float(response.content) > 0.20:
            
            text = "You can not grant a loan to this client because their default risk is above 20%"
            st.markdown(f'<div style="background-color:#FF6347;padding:10px;border-radius:5px;'
                        f'color:white;">{text}</div>',unsafe_allow_html=True)
        else:
            
            text = "You can grant a loan to this client because their default risk is below 20%"
            st.markdown(f'<div style="background-color:#4CAF50;padding:10px;border-radius:5px;'
                        f'color:white;">{text}</div>',unsafe_allow_html=True)
        
        # We are getting from the API the personal features that made the prediction score for that client
        PERS_FEAT_API_URL = "https://projet7-api-0c8f5c7ce811.herokuapp.com/prediction/"
        # PERS_FEAT_API_URL = "http://127.0.0.1:5000/prediction/"
        response1 = requests.get(PERS_FEAT_API_URL, params = dictio_pred)
        exp1 = pickle.loads(response1.content)
        st.title('Personal features for this client')
        st.text("")
        html(exp1.as_html(), width = 1000, height = 250, scrolling = True)
        
        
        # We are getting the table made to compare the client with the 2 groups of customers
        PERS_FEAT_API_URL = "https://projet7-api-0c8f5c7ce811.herokuapp.com/valeur_moyenne/"
        # PERS_FEAT_API_URL = "http://127.0.0.1:5000/valeur_moyenne/"
        response2 = requests.get(PERS_FEAT_API_URL, params = dictio_pred)
        data = response2.json()
        data_json_str = json.dumps(data)  # Convert the dictionary to a JSON string
        resume_deserialized = pd.read_json(data_json_str, orient='split')
        st.title('Comparison with other clients')
        st.text("")
        st.write(resume_deserialized)
        

if __name__ == '__main__':
    main()
