Welcome to the Readme section !

Summary: The 4 notebooks in this "main" branch of the "oC-stuff" repository are linked to a project I did where I put a model on the cloud through the site Heroku using an API. The model predicts the likelyhood that a new client could reimburse a loan given the information on the loan request. The client information is entered in a dashboard (made with Streamlit) that interacts with an API that are both on Heroku.

Notebook "Business metrics":
Here I build a confusion matrix to find the most profitable threshold to be used to determine whether a loan is granted or not to a new client. If the probability of reimbursement for a client is  according the probability. Then next, I look for the best threshold that will optimize the profit of the company with an algorithm.

Notebook "Data drift":
Here I analyze the data drift between the train and test data to see if there is a fundamental change in the data, using the library Evidently.

Notebook "Model balanced classes":
Here I test the Light GBM model with unbalanced classes and I load it on the site ML Flow for tracking purposes. Then I do the same for the model with balanced classes.

Notebook "Model creation ML flow uploading":
Here I am testing the model Light GBM with 798 features then testing the model with only the most important 13 features. Then I upload that lighter model on the ML Flow site.
