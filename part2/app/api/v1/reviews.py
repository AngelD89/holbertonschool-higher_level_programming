"""Review API endpoints."""
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define models for API documentation
user_summary_model = api.model('UserSummary', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='User first name'),
    'last_name': fields.String(description='User last name'),
    'email': fields.String(description='User email')
})

place_summary_model = api.model('PlaceSummary', {
    'id': fields.String(description='Place ID'),
    'title': fields.String(description='Place title')
})

review_model = api.model('Review', {
    'text': fields.String(required=True, description='Review text'),
    'rating': fields.Integer(required=True, description='Rating (1-5)', min=1, max=5),
    'place_id': fields.String(required=True, description='Place ID'),
    'user_id': fields.String(required=True, description='User ID')
})

review_response_model = api.model('ReviewResponse', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Review text'),
    'rating': fields.Integer(description='Rating'),
    'place_id': fields.String(description='Place ID'),
    'user_id': fields.String(description='User ID'),
    'user': fields.Nested(user_summary_model, description='User details'),
    'place': fields.Nested(place_summary_model, description='Place details'),
    'created_at': fields.String(description='Creation timestamp'),
    'updated_at': fields.String(description='Last update timestamp')
})

review_update_model = api.model('ReviewUpdate', {
    'text': fields.String(description='Review text'),
    'rating': fields.Integer(description='Rating (1-5)', min=1, max=5)
})


def serialize_review(review):
    """
    Serialize review with extended data.

    Args:
        review: Review instance to serialize.

    Returns:
        Dictionary with review data including user and place details.
    """
    review_dict = review.to_dict()

    # Add user details
    user = facade.get_user(review.user_id)
    if user:
        review_dict['user'] = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }

    # Add place details
    place = facade.get_place(review.place_id)
    if place:
        review_dict['place'] = {
            'id': place.id,
            'title': place.title
        }

    return review_dict


@api.route('/')
class ReviewList(Resource):
    """Review list resource."""

    @api.doc('list_reviews')
    @api.marshal_list_with(review_response_model)
    def get(self):
        """Retrieve a list of all reviews."""
        reviews = facade.get_all_reviews()
        return [serialize_review(review) for review in reviews], 200

    @api.doc('create_review')
    @api.expect(review_model, validate=True)
    @api.marshal_with(review_response_model, code=201)
    @api.response(400, 'Invalid input')
    @api.response(404, 'Place or User not found')
    def post(self):
        """Create a new review."""
        try:
            review_data = api.payload
            review = facade.create_review(review_data)
            return serialize_review(review), 201
        except ValueError as e:
            if "not found" in str(e).lower():
                api.abort(404, str(e))
            api.abort(400, str(e))
        except Exception as e:
            api.abort(400, str(e))


@api.route('/<string:review_id>')
@api.param('review_id', 'The review identifier')
class ReviewResource(Resource):
    """Review resource for individual review operations."""

    @api.doc('get_review')
    @api.marshal_with(review_response_model)
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Retrieve a review by ID."""
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, 'Review not found')
        return serialize_review(review), 200

    @api.doc('update_review')
    @api.expect(review_update_model, validate=True)
    @api.marshal_with(review_response_model)
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input')
    def put(self, review_id):
        """Update a review's information."""
        try:
            review_data = api.payload
            review = facade.update_review(review_id, review_data)
            if not review:
                api.abort(404, 'Review not found')
            return serialize_review(review), 200
        except ValueError as e:
            api.abort(400, str(e))
        except Exception as e:
            api.abort(400, str(e))

    @api.doc('delete_review')
    @api.response(204, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review."""
        success = facade.delete_review(review_id)
        if not success:
            api.abort(404, 'Review not found')
        return '', 204


@api.route('/places/<string:place_id>')
@api.param('place_id', 'The place identifier')
class PlaceReviewList(Resource):
    """Resource for retrieving all reviews for a specific place."""

    @api.doc('get_place_reviews')
    @api.marshal_list_with(review_response_model)
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Retrieve all reviews for a specific place."""
        # Verify place exists
        place = facade.get_place(place_id)
        if not place:
            api.abort(404, 'Place not found')

        reviews = facade.get_reviews_by_place(place_id)
        return [serialize_review(review) for review in reviews], 200
