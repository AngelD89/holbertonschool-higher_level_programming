"""Amenity API endpoints."""
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define amenity model for API documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Amenity name', max_length=50)
})

amenity_response_model = api.model('AmenityResponse', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Amenity name'),
    'created_at': fields.String(description='Creation timestamp'),
    'updated_at': fields.String(description='Last update timestamp')
})


@api.route('/')
class AmenityList(Resource):
    """Amenity list resource."""

    @api.doc('list_amenities')
    @api.marshal_list_with(amenity_response_model)
    def get(self):
        """Retrieve a list of all amenities."""
        amenities = facade.get_all_amenities()
        return [amenity.to_dict() for amenity in amenities], 200

    @api.doc('create_amenity')
    @api.expect(amenity_model, validate=True)
    @api.marshal_with(amenity_response_model, code=201)
    @api.response(400, 'Invalid input')
    def post(self):
        """Create a new amenity."""
        try:
            amenity_data = api.payload
            amenity = facade.create_amenity(amenity_data)
            return amenity.to_dict(), 201
        except ValueError as e:
            api.abort(400, str(e))
        except Exception as e:
            api.abort(400, str(e))


@api.route('/<string:amenity_id>')
@api.param('amenity_id', 'The amenity identifier')
class AmenityResource(Resource):
    """Amenity resource for individual amenity operations."""

    @api.doc('get_amenity')
    @api.marshal_with(amenity_response_model)
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Retrieve an amenity by ID."""
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            api.abort(404, 'Amenity not found')
        return amenity.to_dict(), 200

    @api.doc('update_amenity')
    @api.expect(amenity_model, validate=True)
    @api.marshal_with(amenity_response_model)
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input')
    def put(self, amenity_id):
        """Update an amenity's information."""
        try:
            amenity_data = api.payload
            amenity = facade.update_amenity(amenity_id, amenity_data)
            if not amenity:
                api.abort(404, 'Amenity not found')
            return amenity.to_dict(), 200
        except ValueError as e:
            api.abort(400, str(e))
        except Exception as e:
            api.abort(400, str(e))
