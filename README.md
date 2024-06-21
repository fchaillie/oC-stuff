Summary:

The files in this branch are linked to a project I did where I put a model on the cloud through the site Heroku using an API.  
The model predicts the likelyhood that a new client could not reimburse a loan given the information on the loan request. The client information entered in the dashboard made by Streamlit.

Details:

All the files in this repository were used only to create the dashboard on Heroku with Streamlit.
The main file for the appearance of the dashboard is "dashboard.py". 
The file "Procfile" informs Heroku that it is with Streamlit that the dashboard will be launched.
The file "requirement.txt" lists the packages to install to make this dashboard.
The file "runtime.text" gives the Python version used.
The file "tests" has the tests that will be executed every time I push a file on this branch (Github Actions).
The files "Pipfile", "Pipfile.lock", "setup.sh" and the folder "src" configurate the dashboard according to my system settings.
