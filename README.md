Loan_Project_Dashboard Repository Summary:

This is a project for a loan company that needs to predict the likelyhood that new clients will not reimburse their loan given the information on their loan request. The client information is entered in a dashboard and interacts with an API before returning an answer saying if the loan request is accepted or not. The files in this "main" branch are for the dashboard made with Streamlit on Heroku. The files in the "Models_and_data" branch are related to the models used and the data used for the final model put on the cloud.

Details of the files in this repository:

The main file for the appearance of the dashboard is "dashboard.py". 
The file "Procfile" informs Heroku that it is with Streamlit that the dashboard will be launched.
The file "requirement.txt" lists the packages to install to make this dashboard.
The file "runtime.text" gives the Python version used.
The file "tests" has the tests that will be executed every time I push a file on this branch (Github Actions).
The files "Pipfile", "Pipfile.lock", "setup.sh" and the folder "src" configurate the dashboard according to my system settings.
