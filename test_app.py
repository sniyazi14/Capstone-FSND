import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


manager_jwt = os.environ['MANAGER']
employee_jwt = os.environ['ASSISTANT']
manager_header = {'Authorization': 'Bearer' + str(manager_jwt)}
employee_header = {'Authorization': 'Bearer' + str(employee_jwt)}

class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = 'postgresql://postgres:1234@localhost:5432/capstone_test'
        setup_db(self.app, self.database_path)

        self.advisor = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'field': 'field',
            'position': 'position',
            'experience': 10,
            'country': 'country'
        }

        self.user = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'field': 'field',
            'level': 'level',
            'subscription_active': True,
            'advisor_name': 'advisor_name'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_users(self):
        res = self.client().get('/users', headers=manager_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        #self.assertTrue(len(data['users']))
        self.assertTrue(data['users'])

    def test_get_advisors(self):
        res = self.client().get('/advisors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['advisors']))

    def test_add_user(self):
        res = self.client().post('/users', json=self.question, headers=manager_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_user_without_data(self):
        res = self.client().post('/advisors', headers=manager_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entity')

    def test_update_user(self):
        res = self.client().patch('/users/1', json=self.question, headers=manager_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_nonexisting_user(self):
        res = self.client().post('/users/1000', headers=manager_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'User 1000 not found')

    def test_add_advisor(self):
        res = self.client().post('/users', json=self.question, headers=manager_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_add_advisor_without_data(self):
        res = self.client().post('/advisors', headers=manager_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entity')

    def test_delete_user(self):
        res = self.client().delete('/user/1', headers=manager_header)
        data = json.loads(res.data)
        user = User.query.filter(User.id == 1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(user, None)

    def test_delete_nonexistent_user(self):
        res = self.client().delete('/users/1000', headers=manager_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entity')

    def test_delete_advisor(self):
        res = self.client().delete('/advisors/1')
        data = json.loads(res.data)
        user = User.query.filter(User.id == 1).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(user, None)

    def test_delete_nonexistent_advisor(self):
        res = self.client().delete('/advisors/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entity')

    def test_forbidden_employee(self):
        res = self.client().delete('/advisors/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entity')

    def test_auth_allowed_employee(self):
        res = self.client().get('/users', headers=employee_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entity')

    def test_unauthorized(self):
        res = self.client().delete('/advisors/1000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entity')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
