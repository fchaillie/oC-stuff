Welcome to the Readme section !

Summary: The 4 Jupyter notebooks in this branch are linked to a project where I put a model on the cloud through the site Heroku using an API.  
The model predicts the likelyhood that a new client could reimburse a loan given the information on the loan request.

Notebook "Business metrics":
Here I build a confusion matrix for a threshold that I use to determine whether the loan is granted or not. Then next, I look for the best threshold that will optimize the profit of the company with an algorithm.

Notebook "Data drift":
Here I analyze the data drift between the train and test data to see if there is a fundamental change in the data, using the library Evidently.

Notebook "Model balanced classes":
Here I test the model Light GBM with unbalanced classes and load it on the site ML Flow for tracking and then I do the same for the model with balanced classes.

Notebook "Model creation ML flow uploading":
Here I am testing the model Light GBM with 798 features then testing the model with only the most important 13 features. Then I upload that lighter model on the ML Flow site.
