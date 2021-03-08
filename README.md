# Full Stack Nanodegree Capstone Project
# Career Advising Company

## Motivation
This project was created to model a company that provides career advising services online through matching users(customers) to one of the many advisors from around the world registered with the company that match their field and career aspirations. The services are provided to users that pay for monthly subscription to the services.


### Installing Dependencies

#### Python 3.8 (preferred)

Install using instructions in [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### PIP Dependencies

Run the following command in the terminal to install all the pip packages required 

```bash
pip3 install -r requirements.txt
```

## Data Modelling:
MODELS.PY
The schema for the database and helper methods to simplify API behavior are in models.py:

There are two tables created: Advisor and User.
The Advisor table has all the advisors that are available to match with users based on the field. It stores their name, field, position, years of exeperience and country.
The User table keeps track of the users of the service who receive career advising from the advisors by storing their name, field, level, advisor name and subscription status.
Each table has an insert, update, delete, and format helper functions.

## Create a database
You need to create a postgreSQL database to store the data. Use the following command in the terminal to create a database
```bash
CREATEDB {database_name}
```
## Virtual Environment
It is recommended to run this application using a virtual environment. To run a virtual environment run the following commands in the terminal while in your project folder
Linux
  ```bash
virtualenv --python 'path-to-python' venv
source venv/bin/activate
  ```
Windows
  ```bash
virtualenv --python 'path-to-python' venv
.\venv\Scripts\activate
  ```
## Running the server

To run the server using the environmental variables in setup.sh file, use the following commands in the terminal:

On Linux : export
```bash
source setup.sh
export FLASK_APP=app
flask run --reload
```

On Windows : set
set FLASK_APP=app.py;
```bash
source setup.sh
set FLASK_APP=app
flask run --reload
```

## Endpoints
### GET '/'
### GET '/users'
### GET '/advisors'
### DELETE '/users/<int>'
### DELETE '/advisors/<int>'
### POST '/users'
### POST '/advisors'
### PATCH '/users'
### PATCH '/advisors'

### GET '/'
- Root route 
- Request Arguments: None
- Returns: An json object with message
-Example request: curl http://127.0.0.1:5000/
-Example response:
{
    "message": "Welcome to Career Advising Capstone API"
}

### GET '/users'
- Fetches a dictionary of users 
- Request Arguments: None
- Returns: Json object that contains {'succes': True, 'user': {}} and lists all users in the database
-Example request:
curl -H "Authorization: Bearer <MANAGER_TOKEN>" http://127.0.0.1:5000/users
-Example response:
{
    "success": true,
    "users": [
        {
            "advisor_name": "Doe",
            "field": "Marketing & PR",
            "first_name": "janes",
            "id": 2,
            "last_name": "does",
            "level": 2,
            "subscription_active": false
        },
        {
            "advisor_name": "Deema",
            "field": "Internet of Things",
            "first_name": "Laila",
            "id": 4,
            "last_name": "Doen",
            "level": 1,
            "subscription_active": true
        }
    ]
}

### GET '/advisors'
- Fetches a dictionary of all questions in the database which contains each question, answer, id, category and difficulty which is paginated with 10 questions per page
- Also returns the categories similar to GET '/categories' endpoint
- Request Arguments: None
- Returns: Json object that contains {'succes': True, 'advisors': {}} and lists all advisors in the database
Example request:
-curl  http://127.0.0.1:5000/advisors
Example response:
{
    "advisors": [
        {
            "country": "Saudi Arabia",
            "experience": 8,
            "field": "Electrical Engineering",
            "first_name": "Lana",
            "id": 3,
            "last_name": "Dodd",
            "position": "Director of Maintenance"
        },
        {
            "country": "Saudi Arabia",
            "experience": 15,
            "field": "Marketing & PR",
            "first_name": "jane",
            "id": 4,
            "last_name": "doe",
            "position": "Marketing Director"
        }
    ],
    "success": true
}

### DELETE '/users/<int>'
-Deletes a user by id from the database
Request Arguments: id of user to be deleted
Returns: Json object that contains {'succes': True, 'deleted': first + last name }
Example request:curl -X DELETE -H "Authorization: Bearer <MANAGER_TOKEN>" http://127.0.0.1:5000/users/3
Example response:
{
    "delete":"Laila Doen",
    "success":true
}

### DELETE '/advisors/<int>'
-Deletes a user by id from the database
Request Arguments: id of user to be deleted
Returns: Json object that contains {'succes': True, 'deleted': first + last name }
Example request: curl -X DELETE -H "Authorization: Bearer <MANAGER_TOKEN>" http://127.0.0.1:5000/advisors/2
Example response:
{
    "delete":"jane doe",
    "success":true
}

### POST '/users'
-Adds a user to the database
Request Arguments: json object that contains the following values (first_name, last_name, field, level, subscription_active, advisor_name)
Returns: Json object that contains {'succes': True, 'user': {}}
Example request: curl -X POST -H "Content-Type: application/json" -d '{"first_name":"Laila", "last_name":"Doen", "field":"Internet of Things", "level":1, "subscription_active":true, "advisor_name":"Deema"}' -H "Authorization: Bearer <MANAGER_TOKEN>" http://127.0.0.1:5000/users
Example response:
{
    "success":true,
    "user":{
        "advisor_name":"Deema",
        "field":"Internet of Things",
        "first_name":"Laila",
        "id":3,
        "last_name":"Doen",
        "level":1,
        "subscription_active":true
        }
}


### POST '/advisors'
-Adds an advisor to the database
Request Arguments: json object that contains the following values (first_name, last_name, field, postion, experience, country)
Returns: Json object that contains {'succes': True, 'advisor': {}}
Example request: curl -X POST -H "Content-Type: application/json" -d '{"first_name":"Lana", "last_name":"Dodd", "field":"Electrical Engineering", "position":"Director of Maintenance", "experience":8, "country":"Saudi Arabia"}' -H "Authorization: Bearer <MANAGER_TOKEN>" http://127.0.0.1:5000/advisors
Example response:
{
    "advisor":
    {
        "country":"Saudi Arabia",
        "experience":8,
        "field":"Electrical Engineering",
        "first_name":"Lana",
        "id":3,
        "last_name":"Dodd",
        "position":"Director of Maintenance"},
    "success":true
}

### PATCH '/users'
-Update a specific users subscription by id
Request Arguments: json object contains the boolean value for subscription_active
Returns: Json object that contains {'succes': True, 'user': {}}
Example request: curl -X PATCH http://127.0.0.1:8080/actors/2 -H "Authorization: Bearer <MANAGER_TOKEN>" -d '{"subscription_active":"True"}'
Example response:
{
    "success":true,
    "user":{
        "advisor_name":"Doe",
        "field":"Marketing & PR",
        "first_name":"janes",
        "id":2,
        "last_name":"does",
        "level":2,
        "subscription_active":false
        }
}


## Errors
-400: Bad Request
-401: Unauthorized
-403: Forbidden
-404: Resource Not Found
-422: Unprocessable Entity
-500: Internal Server Error

Format example in JSON:
   {
    "success": False,
    "error": 422,
    "message": "Unprocessable entity"
    }

## Testing
For testing, a new database can be created called capstone_test. Then the file test_app.py which has all the tests should be run using the command:
```bash
python3 test_app.py
```

## Authentication
Roles:
-Employee: Can view, modify, add and delete users only
-Manager: Can do everything an employee can as well as add and delete an advisor
No authentication is need for viewing advisors (non-confidential information)
Permissions are stored in the JWTs. The permissions are the following:
-delete:advisors		
-delete:users		
-get:users			
-patch:users		
-post:advisors		
-post:users

## Heroku Deployment
Application has been deployed on the following heroku url:
https://capstone-sbn.herokuapp.com/
