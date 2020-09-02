# Full Stack Nanodegree Capstone Project
# Career Advising Company
https://unit4.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=tAeXeJlyCZcxJpLI0MpMm7FXGMR9QLwf&redirect_uri=http://localhost:8100/login-results

curl http://127.0.0.1:5000/users -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVEdlNCdkRzMzZ4ZFcwdFZTYW90cyJ9.eyJpc3MiOiJodHRwczovL3VuaXQ0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwOTQ1ODcxNzgzOTE5Njk1OTAwOCIsImF1ZCI6WyJjYXBzdG9uZSIsImh0dHBzOi8vdW5pdDQudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5ODk3NjM3NywiZXhwIjoxNTk5MDYyNzc3LCJhenAiOiJ0QWVYZUpseUNaY3hKcExJME1wTW03RlhHTVI5UUx3ZiIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWR2aXNvcnMiLCJkZWxldGU6dXNlcnMiLCJnZXQ6dXNlcnMiLCJwYXRjaDphZHZpc29ycyIsInBhdGNoOnVzZXJzIiwicG9zdDphZHZpc29ycyIsInBvc3Q6dXNlcnMiXX0.mBcRWqbSbzl-JQ2u17otgf0Dy8JCx4wKohU7wlu1T-o2wEWd9eizzmZmGvHElKGl1grc1olAmFk9bWOqTwFEsRTr1podB6Al88m3edtGAjMlwphoHccNQmPXHt6YlLP45pOUPEM2xeMVk7NuHMQslQj72n9IJwXb-Oi7ZSgnifyuNHrTgcPt_A1L0Hjh3u9o-RvKrKR32uYCDu7UoQwo0twi3MbhejooCZRb0r24Xzr5HyHZ3dpXROsy74zH_s2uGIeqSUT7f0NauXuWF3eGsvqr9yFMcg3Uh0uzcPFX_eHoWfexg2Nh6uN6chRzKvpD1q4ClhvPpJcDzQPcLWOyBg&scope=openid%20profile%20email&expires_in=86400&token_type=Bearer&state=g6Fo2SA1T1FZMDNEXzhKOWV6YWN1SUVOank0dWZFU0REdzhYaaN0aWTZIEdwdmZRLUxTRmdWMUhjV002ZGdFdUFxT2Q4MkQycG94o2NpZNkgdEFlWGVKbHlDWmN4SnBMSTBNcE1tN0ZYR01SOVFMd2Y" -H "Content-Type: application/json"

## Motivation
This project was created to model a company that provides career advising services online through matching users(customers) to one of the many advisors from around the world registered with the company that match their field and career aspirations. The services are provided to users that pay for monthly subscription to the services.


### Installing Dependencies

#### Python 3.8 (preferred)

Install using instructions in [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### PIP Dependencies

Run the following command in the terminal to install all the pip packages required 

```bash
pip install -r requirements.txt
```

## Create a database
You need to create a postgreSQL database to store the data. Use the following command in the terminal to create a database
```bash
CREATEDB {database_name}
```

## Running the server

To run the server using the environmental variables in setup.sh file, use the following commands in the terminal:

```bash
source setup.sh
export FLASK_APP=app
flask run --reload
```


## Endpoints

###GET '/users'
###GET '/advisors'
###DELETE '/users/<int>'
###DELETE '/advisors/<int>'
###POST '/users'
###POST '/advisors'
###PATCH '/users'
###PATCH '/advisors'


###GET '/users'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
-Example request:

-Example response:


###GET '/advisors'
- Fetches a dictionary of all questions in the database which contains each question, answer, id, category and difficulty which is paginated with 10 questions per page
- Also returns the categories similar to GET '/categories' endpoint
- Request Arguments: None
- Returns: An object with 5 keys, categories, that contains a object of id: category_string key:value pairs.
-curl http://127.0.0.1:5000/advisors

###DELETE '/users/<int>'
###DELETE '/advisors/<int>'
###POST '/users'
curl -X POST -H "Content-Type: application/json" -d '{"first_name":"Laila", "last_name":"Doen", "field":"Internet of Things", "level":"1", "subscription_active":"True", "advisor_name":"Deema"}' http://127.0.0.1:5000/users
###POST '/advisors'
###PATCH '/users'
###PATCH '/advisors'

DELETE '/questions/<int>'
- Deletes a specific question from the database
- Request Arguments: id of question to be deleted (integer)
- Returns: all questions in similar format to GET '/questions'
- Example Request:
curl -X DELETE http://127.0.0.1:5000/questions/31
- Example response:


POST '/questions/add'
- Creates new question in the database
- Request Arguments: new question parameters as json object: question(string), answer(string), difficulty(integer), category(string)
- Returns: success: result key value pair
-Example request:
curl -X POST -H "Content-Type: application/json" -d '{"question":"new question", "answer":"this", "difficulty":"1", "category":"1"}' http://127.0.0.1:5000/questions/add
- Example response:
{
  "success": true
}

POST '/questions/search'
-Performs case-insensitive search on questions table in database to find questions that contain given search term
- Request Arguments: search term (string)
- Returns: Response similar to '/questions' with only questions that contain specified search term as substring of the question
- Example request:
curl -X POST -H "Content-Type: application/json" -d '{"searchTerm":"title"}' http://127.0.0.1:5000/questions/search
- Example response:
  

POST '/quizzes'
- Fetches a question a new question that is in selected category and not one of previous questions
- Request Arguments: previous questions array and quiz category dictionary with type and id
- Return: single question JSON object
- Example request:
curl -d '{"previous_questions": [16],"quiz_category": {"type":"Art","id": "2"}}' -H 'Content-Type: application/json' -X POST http://127.0.0.1:5000/quizzes
- Example response:
{
  "question": {
    "answer": "One",
    "category": 2,
    "difficulty": 4,
    "id": 18,
    "question": "How many paintings did Van Gogh sell in his lifetime?"
  },
  "success": true
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

## Authentication
Roles:
-Employee: Can view, modify, add and delete users only
-Manager: Can do everything an employee can as well as add and delete an advisor
No authentication is need for viewing advisors (non-confidential information)

## Testing
For testing, a new database can be created called capstone_test. Then the file test_app.py which has all the tests should be run using the command:
```bash
python test_app.py
```
