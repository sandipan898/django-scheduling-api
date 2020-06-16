# Django Scheduling API

### making a Scheduling API by Django REST Framework

### To run the program:
    * Clone the repository.
    * activate the virtual environment by 'source env/bin/activate'.
    * install the requirements by 'pip install -r requirements.txt'.
    * change current directory by 'cd scheduling_api'.
    * run command 'python manage.py runserver'.

### Working mechanism:
    * first we have to call the API with a site_url containng a url and a *timestamp* containing a date and time in specific format and It would be a POST call. This will schedule the task for us.

    * Then if the current date and time matches with the one specified at the time of POST request the api will send a GET request request to the url and it will return a status code.
