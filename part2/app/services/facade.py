"""Facade pattern implementation for HBnB business logic."""
from typing import Optional, List, Dict, Any
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    """
    Facade class to manage interactions between the API and business logic.

    This class provides a simplified interface for managing users, places,
    reviews, and amenities.
    """

    def __init__(self):
        """Initialize the facade with repositories for each entity."""
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # User management methods
    def create_user(self, user_data: Dict[str, Any]) -> User:
        """
        Create a new user.

        Args:
            user_data: Dictionary containing user information.

        Returns:
            The created User instance.

        Raises:
            ValueError: If email already exists or validation fails.
        """
        # Check if email already exists
        existing_users = self.user_repo.get_by_attribute('email', user_data.get('email'))
        if existing_users:
            raise ValueError("Email already registered")

        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id: str) -> Optional[User]:
        """
        Retrieve a user by ID.

        Args:
            user_id: The user's unique identifier.

        Returns:
            The User instance if found, None otherwise.
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Retrieve a user by email.

        Args:
            email: The user's email address.

        Returns:
            The User instance if found, None otherwise.
        """
        users = self.user_repo.get_by_attribute('email', email)
        return users[0] if users else None

    def get_all_users(self) -> List[User]:
        """
        Retrieve all users.

        Returns:
            List of all User instances.
        """
        return self.user_repo.get_all()

    def update_user(self, user_id: str, user_data: Dict[str, Any]) -> Optional[User]:
        """
        Update a user's information.

        Args:
            user_id: The user's unique identifier.
            user_data: Dictionary containing updated user information.

        Returns:
            The updated User instance if found, None otherwise.

        Raises:
            ValueError: If email already exists for another user.
        """
        user = self.user_repo.get(user_id)
        if not user:
            return None

        # Check if email is being updated and if it's already in use
        if 'email' in user_data and user_data['email'] != user.email:
            existing_users = self.user_repo.get_by_attribute('email', user_data['email'])
            if existing_users:
                raise ValueError("Email already registered")

        # Don't allow updating certain fields
        restricted_fields = ['id', 'created_at', 'password']
        for field in restricted_fields:
            user_data.pop(field, None)

        user.update(user_data)
        return user

    # Amenity management methods
    def create_amenity(self, amenity_data: Dict[str, Any]) -> Amenity:
        """
        Create a new amenity.

        Args:
            amenity_data: Dictionary containing amenity information.

        Returns:
            The created Amenity instance.

        Raises:
            ValueError: If validation fails.
        """
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id: str) -> Optional[Amenity]:
        """
        Retrieve an amenity by ID.

        Args:
            amenity_id: The amenity's unique identifier.

        Returns:
            The Amenity instance if found, None otherwise.
        """
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self) -> List[Amenity]:
        """
        Retrieve all amenities.

        Returns:
            List of all Amenity instances.
        """
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id: str, amenity_data: Dict[str, Any]) -> Optional[Amenity]:
        """
        Update an amenity's information.

        Args:
            amenity_id: The amenity's unique identifier.
            amenity_data: Dictionary containing updated amenity information.

        Returns:
            The updated Amenity instance if found, None otherwise.
        """
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None

        # Don't allow updating certain fields
        restricted_fields = ['id', 'created_at']
        for field in restricted_fields:
            amenity_data.pop(field, None)

        amenity.update(amenity_data)
        return amenity

    # Place management methods
    def create_place(self, place_data: Dict[str, Any]) -> Place:
        """
        Create a new place.

        Args:
            place_data: Dictionary containing place information.

        Returns:
            The created Place instance.

        Raises:
            ValueError: If owner doesn't exist or validation fails.
        """
        # Verify owner exists
        owner = self.user_repo.get(place_data.get('owner_id'))
        if not owner:
            raise ValueError("Owner not found")

        # Extract amenity IDs if provided
        amenity_ids = place_data.pop('amenities', [])

        place = Place(**place_data)

        # Add amenities if provided
        for amenity_id in amenity_ids:
            amenity = self.amenity_repo.get(amenity_id)
            if amenity:
                place.add_amenity(amenity_id)

        self.place_repo.add(place)
        return place

    def get_place(self, place_id: str) -> Optional[Place]:
        """
        Retrieve a place by ID.

        Args:
            place_id: The place's unique identifier.

        Returns:
            The Place instance if found, None otherwise.
        """
        return self.place_repo.get(place_id)

    def get_all_places(self) -> List[Place]:
        """
        Retrieve all places.

        Returns:
            List of all Place instances.
        """
        return self.place_repo.get_all()

    def update_place(self, place_id: str, place_data: Dict[str, Any]) -> Optional[Place]:
        """
        Update a place's information.

        Args:
            place_id: The place's unique identifier.
            place_data: Dictionary containing updated place information.

        Returns:
            The updated Place instance if found, None otherwise.
        """
        place = self.place_repo.get(place_id)
        if not place:
            return None

        # Don't allow updating certain fields
        restricted_fields = ['id', 'created_at', 'owner_id']
        for field in restricted_fields:
            place_data.pop(field, None)

        # Handle amenities separately
        if 'amenities' in place_data:
            amenity_ids = place_data.pop('amenities')
            place.amenities = []
            for amenity_id in amenity_ids:
                amenity = self.amenity_repo.get(amenity_id)
                if amenity:
                    place.add_amenity(amenity_id)

        place.update(place_data)
        return place

    # Review management methods
    def create_review(self, review_data: Dict[str, Any]) -> Review:
        """
        Create a new review.

        Args:
            review_data: Dictionary containing review information.

        Returns:
            The created Review instance.

        Raises:
            ValueError: If place or user doesn't exist, or validation fails.
        """
        # Verify place exists
        place = self.place_repo.get(review_data.get('place_id'))
        if not place:
            raise ValueError("Place not found")

        # Verify user exists
        user = self.user_repo.get(review_data.get('user_id'))
        if not user:
            raise ValueError("User not found")

        # Check if user is trying to review their own place
        if place.owner_id == review_data.get('user_id'):
            raise ValueError("You cannot review your own place")

        review = Review(**review_data)
        self.review_repo.add(review)

        # Add review to place
        place.add_review(review.id)

        return review

    def get_review(self, review_id: str) -> Optional[Review]:
        """
        Retrieve a review by ID.

        Args:
            review_id: The review's unique identifier.

        Returns:
            The Review instance if found, None otherwise.
        """
        return self.review_repo.get(review_id)

    def get_all_reviews(self) -> List[Review]:
        """
        Retrieve all reviews.

        Returns:
            List of all Review instances.
        """
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id: str) -> List[Review]:
        """
        Retrieve all reviews for a specific place.

        Args:
            place_id: The place's unique identifier.

        Returns:
            List of Review instances for the place.
        """
        return self.review_repo.get_by_attribute('place_id', place_id)

    def update_review(self, review_id: str, review_data: Dict[str, Any]) -> Optional[Review]:
        """
        Update a review's information.

        Args:
            review_id: The review's unique identifier.
            review_data: Dictionary containing updated review information.

        Returns:
            The updated Review instance if found, None otherwise.
        """
        review = self.review_repo.get(review_id)
        if not review:
            return None

        # Don't allow updating certain fields
        restricted_fields = ['id', 'created_at', 'place_id', 'user_id']
        for field in restricted_fields:
            review_data.pop(field, None)

        review.update(review_data)
        return review

    def delete_review(self, review_id: str) -> bool:
        """
        Delete a review.

        Args:
            review_id: The review's unique identifier.

        Returns:
            True if the review was deleted, False otherwise.
        """
        review = self.review_repo.get(review_id)
        if not review:
            return False

        # Remove review from place
        place = self.place_repo.get(review.place_id)
        if place:
            place.remove_review(review_id)

        return self.review_repo.delete(review_id)
