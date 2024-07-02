Summary: 

The 4 notebooks in this "main" branch of the "oC-stuff" repository are linked to a project I did where I put a model on the cloud through the site Heroku using an API. The model predicts the likelyhood that a new client could not reimburse a loan given the information on the loan request. The client information is entered in a dashboard (made with Streamlit) that interacts with an API that are both on Heroku. Those 4 notebooks here are not related with the building of the dashboard or the API. They are related to the data used for the model and the model used for the default prediction of new clients.

Details:

Notebook "Business_metrics":
Here I build a confusion matrix to find the most profitable default threshold to be used by the company to determine whether a loan is granted or not to a new client. If the probability of default given by the model for a client is higher than the threshold then the loan is not granted.

Notebook "Data_Drift":
Here I analyze the data drift between the train data and the test data to see if there is a fundamental change in the data, using the library Evidently.
If there is a significant difference between the 2 sets then the data needs to be changed so that the train data and test data look similar statistically speaking.

Notebook "Model_Balanced_Classes":
Here I test the Light GBM model with the 2 unbalanced classes and I load that model on the site ML Flow (mlflow.org) for tracking purposes. Then I do the same for the model with the 2 classes that are balanced this time.

Notebook "Model_creation_ML_Flow_uploading":
Here I am testing the Light GBM model with 798 features then testing the model with only the most important 13 features. Then I upload that lighter model on ML Flow.
