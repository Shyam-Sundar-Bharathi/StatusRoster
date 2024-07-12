# StatusRosterApp
App to maintain daily work status of team members.

*Hello*

The two jpg files in the repository are screenshots of presently-maintained excel that need to migrate to the application to be built.  
All details regarding the original proposed design are available in the design word document.  
However, some pivots were made in the proposed architecture - primarily the backend was built entirely in Django and DRF.  
Backend build (including APIs) has been logically closed.  
Frontend can be built using any framework (preferably SAP UI5, if not then React) and simply be plugged to the Django backend.  

*Backend*

Test folder contains a StatusRosterTest dev folder and a venv.  
The venv is fully configured to all the requirements and must simply be activated before running application.   
Dev folder contains code logically separated into API, App (source), Test (config), db, and manage.py (exe).  
Pivot in proposed models can be identified from App/models.py.  
DRF uses App/seralizers.py to create endpoints of the models.  
App/ (admin.py, urls.py, views.py) etc are configured to Django prescriptions.  
App/ (signals.py, middleware) are written to faciliate automatic logging in the application (can be seen on the admil panel).  

*Init run*

Open Dev folder in a terminal (after activating venv).  
Run "python manage.py runserver".  
Open local host with assigned port number and navigate to /admin. Eg: 127.0.0.1:8080/admin.  
APIs can be seen/tested through a postman client at the api endpoint.  

*Next*

Design document even contains proposed wireframes for to-be-built UI.  
Application uses some forms that Django can easily generate with the defined models (to be taken advantage of).  
SAP elements are easily available if UI5 used for UI dev.  
Refer Django docs for connection/plugin of UI to APIs.     
The test application uses an sqlite server. Deployment server should be more robust (reach out to team for allocation of server).  
