"""Place API endpoints."""
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define models for API documentation
amenity_summary_model = api.model('AmenitySummary', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Amenity name')
})

owner_summary_model = api.model('OwnerSummary', {
    'id': fields.String(description='Owner ID'),
    'first_name': fields.String(description='Owner first name'),
    'last_name': fields.String(description='Owner last name'),
    'email': fields.String(description='Owner email')
})

review_summary_model = api.model('ReviewSummary', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Review text'),
    'rating': fields.Integer(description='Rating'),
    'user_id': fields.String(description='User ID')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Place title', max_length=100),
    'description': fields.String(required=True, description='Place description'),
    'price': fields.Float(required=True, description='Price per night', min=0),
    'latitude': fields.Float(required=True, description='Latitude', min=-90, max=90),
    'longitude': fields.Float(required=True, description='Longitude', min=-180, max=180),
    'owner_id': fields.String(required=True, description='Owner ID'),
    'amenities': fields.List(fields.String, description='List of amenity IDs')
})

place_response_model = api.model('PlaceResponse', {
    'id': fields.String(description='Place ID'),
    'title': fields.String(description='Place title'),
    'description': fields.String(description='Place description'),
    'price': fields.Float(description='Price per night'),
    'latitude': fields.Float(description='Latitude'),
    'longitude': fields.Float(description='Longitude'),
    'owner_id': fields.String(description='Owner ID'),
    'owner': fields.Nested(owner_summary_model, description='Owner details'),
    'amenities': fields.List(fields.Nested(amenity_summary_model), description='Amenities'),
    'reviews': fields.List(fields.Nested(review_summary_model), description='Reviews'),
    'created_at': fields.String(description='Creation timestamp'),
    'updated_at': fields.String(description='Last update timestamp')
})

place_update_model = api.model('PlaceUpdate', {
    'title': fields.String(description='Place title', max_length=100),
    'description': fields.String(description='Place description'),
    'price': fields.Float(description='Price per night', min=0),
    'latitude': fields.Float(description='Latitude', min=-90, max=90),
    'longitude': fields.Float(description='Longitude', min=-180, max=180),
    'amenities': fields.List(fields.String, description='List of amenity IDs')
})


def serialize_place(place):
    """
    Serialize place with extended data.

    Args:
        place: Place instance to serialize.

    Returns:
        Dictionary with place data including owner and amenities details.
    """
    place_dict = place.to_dict()

    # Add owner details
    owner = facade.get_user(place.owner_id)
    if owner:
        place_dict['owner'] = {
            'id': owner.id,
            'first_name': owner.first_name,
            'last_name': owner.last_name,
            'email': owner.email
        }

    # Add amenities details
    amenities_details = []
    for amenity_id in place.amenities:
        amenity = facade.get_amenity(amenity_id)
        if amenity:
            amenities_details.append({
                'id': amenity.id,
                'name': amenity.name
            })
    place_dict['amenities'] = amenities_details

    # Add reviews details
    reviews_details = []
    for review_id in place.reviews:
        review = facade.get_review(review_id)
        if review:
            reviews_details.append({
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'user_id': review.user_id
            })
    place_dict['reviews'] = reviews_details

    return place_dict


@api.route('/')
class PlaceList(Resource):
    """Place list resource."""

    @api.doc('list_places')
    @api.marshal_list_with(place_response_model)
    def get(self):
        """Retrieve a list of all places."""
        places = facade.get_all_places()
        return [serialize_place(place) for place in places], 200

    @api.doc('create_place')
    @api.expect(place_model, validate=True)
    @api.marshal_with(place_response_model, code=201)
    @api.response(400, 'Invalid input')
    @api.response(404, 'Owner not found')
    def post(self):
        """Create a new place."""
        try:
            place_data = api.payload
            place = facade.create_place(place_data)
            return serialize_place(place), 201
        except ValueError as e:
            if "not found" in str(e).lower():
                api.abort(404, str(e))
            api.abort(400, str(e))
        except Exception as e:
            api.abort(400, str(e))


@api.route('/<string:place_id>')
@api.param('place_id', 'The place identifier')
class PlaceResource(Resource):
    """Place resource for individual place operations."""

    @api.doc('get_place')
    @api.marshal_with(place_response_model)
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Retrieve a place by ID."""
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, 'Place not found')
        return serialize_place(place), 200

    @api.doc('update_place')
    @api.expect(place_update_model, validate=True)
    @api.marshal_with(place_response_model)
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input')
    def put(self, place_id):
        """Update a place's information."""
        try:
            place_data = api.payload
            place = facade.update_place(place_id, place_data)
            if not place:
                api.abort(404, 'Place not found')
            return serialize_place(place), 200
        except ValueError as e:
            api.abort(400, str(e))
        except Exception as e:
            api.abort(400, str(e))
