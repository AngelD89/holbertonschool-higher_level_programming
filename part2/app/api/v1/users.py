"""User API endpoints."""
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define user model for API documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name', max_length=50),
    'last_name': fields.String(required=True, description='Last name', max_length=50),
    'email': fields.String(required=True, description='Email address'),
    'password': fields.String(required=True, description='Password', min_length=6)
})

user_response_model = api.model('UserResponse', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name'),
    'email': fields.String(description='Email address'),
    'is_admin': fields.Boolean(description='Admin status'),
    'created_at': fields.String(description='Creation timestamp'),
    'updated_at': fields.String(description='Last update timestamp')
})

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(description='First name', max_length=50),
    'last_name': fields.String(description='Last name', max_length=50),
    'email': fields.String(description='Email address')
})


@api.route('/')
class UserList(Resource):
    """User list resource."""

    @api.doc('list_users')
    @api.marshal_list_with(user_response_model)
    def get(self):
        """Retrieve a list of all users."""
        users = facade.get_all_users()
        return [user.to_dict() for user in users], 200

    @api.doc('create_user')
    @api.expect(user_model, validate=True)
    @api.marshal_with(user_response_model, code=201)
    @api.response(400, 'Invalid input')
    @api.response(409, 'Email already registered')
    def post(self):
        """Create a new user."""
        try:
            user_data = api.payload
            user = facade.create_user(user_data)
            return user.to_dict(), 201
        except ValueError as e:
            api.abort(400, str(e))
        except Exception as e:
            if "already registered" in str(e).lower():
                api.abort(409, str(e))
            api.abort(400, str(e))


@api.route('/<string:user_id>')
@api.param('user_id', 'The user identifier')
class UserResource(Resource):
    """User resource for individual user operations."""

    @api.doc('get_user')
    @api.marshal_with(user_response_model)
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Retrieve a user by ID."""
        user = facade.get_user(user_id)
        if not user:
            api.abort(404, 'User not found')
        return user.to_dict(), 200

    @api.doc('update_user')
    @api.expect(user_update_model, validate=True)
    @api.marshal_with(user_response_model)
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input')
    @api.response(409, 'Email already registered')
    def put(self, user_id):
        """Update a user's information."""
        try:
            user_data = api.payload
            user = facade.update_user(user_id, user_data)
            if not user:
                api.abort(404, 'User not found')
            return user.to_dict(), 200
        except ValueError as e:
            if "already registered" in str(e).lower():
                api.abort(409, str(e))
            api.abort(400, str(e))
        except Exception as e:
            api.abort(400, str(e))
