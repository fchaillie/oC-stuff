import pandas as pd
import streamlit as st
import requests
import mlflow
import json
from lime import lime_tabular

def request_prediction(model_uri, data):

    data_json = {'data': data}
    
    response = requests.request(method = 'POST', url = model_uri, json = data_json)

    if response.status_code != 200:
        raise Exception(
            "Request failed with status {}, {}".format(response.status_code, response.text))

    return response.json()


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
        
        # Your list of values
#         # data_list = [EXT_SOURCE_1, EXT_SOURCE_2, EXT_SOURCE_3, PAYMENT_RATE, DAYS_BIRTH, DAYS_EMPLOYED,
#                      DAYS_EMPLOYED_PERC, DAYS_REGISTRATION, DAYS_ID_PUBLISH, AMT_ANNUITY, ANNUITY_INCOME_PERC,
#                      INSTAL_DBD_MEAN, REGION_POPULATION_RELATIVE]
        
        dictio_pred = {'EXT_SOURCE_1': EXT_SOURCE_1, 'EXT_SOURCE_2': EXT_SOURCE_2, 'EXT_SOURCE_3': EXT_SOURCE_3, 
                       'PAYMENT_RATE': PAYMENT_RATE, 'DAYS_BIRTH': DAYS_BIRTH, 'DAYS_EMPLOYED': DAYS_EMPLOYED,
                       'DAYS_EMPLOYED_PERC': DAYS_EMPLOYED_PERC, 'DAYS_REGISTRATION': DAYS_REGISTRATION, 
                       'DAYS_ID_PUBLISH': DAYS_ID_PUBLISH,'AMT_ANNUITY': AMT_ANNUITY, 
                       'ANNUITY_INCOME_PERC': ANNUITY_INCOME_PERC,'INSTAL_DBD_MEAN': INSTAL_DBD_MEAN, 
                       'REGION_POPULATION_RELATIVE': REGION_POPULATION_RELATIVE}
        
        PRED_API_URL = "http://127.0.0.1:5000/prediction/"
        response = requests.get(PRED_API_URL, params = dictio_pred)
        content = json.loads(response.content.decode('utf-8'))
        

        predictions = content[0]
    
        if predictions > 0.15:
            answer = "No loan for you angel"
        else:
            answer = "Loan for you angel"
        
#         # Création de l'explainer
#         explainer = lime_tabular.LimeTabularExplainer(df.values, 
#                                                       feature_names = column_names, 
#                                                       class_names = ['0','1'], 
#                                                       verbose = True, 
#                                                       mode = 'classification')

#         # Choisissez un exemple spécifique à expliquer
#         exp = explainer.explain_instance(np.array(data_list), loaded_model.predict, num_features = 5 )
#         # Afficher l'explication
#         html_output = exp.show_in_notebook(show_table=True, predict_proba=True)._repr_html_()
            
        st.write(answer)
        
#         st.write(html_output, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
