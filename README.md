Welcome to the Readme section !

Summary: The 4 notebooks in this "main" branch of the "oC-stuff" repository are linked to a project I did where I put a model on the cloud through the site Heroku using an API. The model predicts the likelyhood that a new client could not reimburse a loan given the information on the loan request. The client information is entered in a dashboard (made with Streamlit) that interacts with an API that are both on Heroku.

Notebook "Business metrics":
Here I build a confusion matrix to find the most profitable threshold to be used by the company to determine whether a loan is granted or not to a new client. If the probability of default given by the model for a client is higher than the threshold then the loan is not granted.

Notebook "Data drift":
Here I analyze the data drift between the train data and the test data to see if there is a fundamental change in the data, using the library Evidently.
If there is a significant data drift then the data needs to be changed so that the train data and test data realign.

Notebook "Model balanced classes":
Here I test the Light GBM model with the 2 unbalanced classes and I load that model on the site ML Flow for tracking purposes. Then I do the same for the model with the 2 classes that are balanced this time.

Notebook "Model creation ML flow uploading":
Here I am testing the Light GBM model with 798 features then testing the model with only the most important 13 features. Then I upload that lighter model on the ML Flow site.
