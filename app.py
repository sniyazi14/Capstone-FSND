import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import User, Advisor
from auth import AuthError, requires_auth

database_path = os.environ['DATABASE_URL']


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(app)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    # Fetch users information, needs permission
    @app.route('/users')
    @requires_auth('get:users')
    def fetch_users(jwt):
        users = User.query.all()
        if len(users) == 0:
            abort(404)
        users_list = [u.fetch() for u in users]
        result = {
            "success": True,
            "users": users_list
        }
        return jsonify(result)

    # Fetch advisors information
    @app.route('/advisors')
    def fetch_advisors():
        advisors = Advisor.query.all()
        if len(advisors) == 0:
            abort(404)
        advisors_list = [a.fetch() for a in advisors]
        result = {
            "success": True,
            "advisors": advisors_list
        }
        return jsonify(result)

    # Add a new advisor to the database
    @app.route('/advisors', methods=['POST'])
    @requires_auth('post:advisor')
    def add_advisor(jwt):
        try:
            body = request.get_json()
            first_name = body.get('first_name', None)
            last_name = body.get('last_name', None)
            field = body.get('field', None)
            position = body.get('position', None)
            experience = body.get('experience', None)
            country = body.get('country', None)
            if first_name is None or field is None:
                abort(400)
            advisor = Advisor(first_name=first_name, last_name=last_name,
                              field=field, position=position,
                              experience=experience, country=country)
            advisor.insert()
            result = {
                "success": True,
                "advisor": advisor.fetch()
            }
            return jsonify(result)
        except Exception:
            abort(422)

    # Add a new user to the database
    @app.route('/users', methods=['POST'])
    #@requires_auth('post:users')
    def add_new_user():
        try:
            body = request.get_json()
            first_name = body.get('first_name', '')
            last_name = body.get('last_name', '')
            field = body.get('field', '')
            advisor_name = body.get('advisor_name', '')
            level = body.get('level', '')
            subscription_active = body.get('subscription_active', '')
            #if first_name is None or field is None:
                #abort(400)
            print('here 1')
            user = User(first_name=first_name, last_name=last_name,
                        field=field, level=level,
                        advisor_name=advisor_name,
                        subscription_active=subscription_active)
            print('here 2')
            user.insert()
            print('here 3')
            result = {
                "success": True,
                "user": user.fetch()
            }
            return jsonify(result)
        except Exception:
            abort(422)

    # Update a certain drink
    @app.route('/users/<int:u_id>', methods=['PATCH'])
    @requires_auth('patch:users')
    def update_user_subscription(jwt, u_id):
        try:
            user = User.query.filter(User.id == u_id).one_or_none()
            if user is None:
                return json.dumps({
                    'success': False,
                    'error': 'User ' + id + ' not found'
                }), 404
            body = request.get_json()
            subscription_active = body.get('subscription_active', True)
            user.subscription_active = subscription_active
            user.update()
            result = {
                "success": True,
                "user": user.fetch()
            }
            return jsonify(result)
        except Exception:
            abort(422)

    # Delete an advisor from the database
    @app.route('/advisors/<int:a_id>', methods=['DELETE'])
    @requires_auth('delete:advisors')
    def delete_advisor(jwt, a_id):
        try:
            advisor = Advisor.query.filter(Advisor.id == a_id).one_or_none()
            if advisor is None:
                abort(404)
            name = advisor.first_name + ' ' + advisor.last_name
            advisor.delete()
            return jsonify({
                'success': True,
                'delete': name
            })
        except Exception:
            abort(422)

    # Delete a user from the database
    @app.route('/users/<int:u_id>', methods=['DELETE'])
    @requires_auth('delete:users')
    def delete_user(jwt, u_id):
        try:
            user = User.query.filter(User.id == u_id).one_or_none()
            if user is None:
                abort(404)
            name = user.first_name + ' ' + user.last_name
            user.delete()
            return jsonify({
               'success': True,
               'delete': name
            })
        except Exception:
            abort(422)

    # Error Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
            }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "internal server error"
            }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
            }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
            }), 404

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


APP = create_app()


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
