"""Place model."""
from typing import List
from app.models.base import BaseModel


class Place(BaseModel):
    """Place entity representing a place/property in the system."""

    def __init__(self, title: str, description: str, price: float,
                 latitude: float, longitude: float, owner_id: str):
        """
        Initialize a Place instance.

        Args:
            title: Place title.
            description: Place description.
            price: Price per night.
            latitude: Latitude coordinate.
            longitude: Longitude coordinate.
            owner_id: ID of the owner (User).

        Raises:
            ValueError: If validation fails.
        """
        super().__init__()
        self.title = self._validate_title(title)
        self.description = description
        self.price = self._validate_price(price)
        self.latitude = self._validate_latitude(latitude)
        self.longitude = self._validate_longitude(longitude)
        self.owner_id = owner_id
        self.amenities: List[str] = []  # List of amenity IDs
        self.reviews: List[str] = []  # List of review IDs

    @staticmethod
    def _validate_title(title: str) -> str:
        """
        Validate place title.

        Args:
            title: The title to validate.

        Returns:
            The validated title.

        Raises:
            ValueError: If validation fails.
        """
        if not title or not isinstance(title, str):
            raise ValueError("Title is required and must be a string")
        if len(title) > 100:
            raise ValueError("Title must not exceed 100 characters")
        return title

    @staticmethod
    def _validate_price(price: float) -> float:
        """
        Validate price.

        Args:
            price: The price to validate.

        Returns:
            The validated price.

        Raises:
            ValueError: If validation fails.
        """
        try:
            price = float(price)
        except (TypeError, ValueError):
            raise ValueError("Price must be a number")

        if price <= 0:
            raise ValueError("Price must be a positive value")
        return price

    @staticmethod
    def _validate_latitude(latitude: float) -> float:
        """
        Validate latitude.

        Args:
            latitude: The latitude to validate.

        Returns:
            The validated latitude.

        Raises:
            ValueError: If validation fails.
        """
        try:
            latitude = float(latitude)
        except (TypeError, ValueError):
            raise ValueError("Latitude must be a number")

        if not -90.0 <= latitude <= 90.0:
            raise ValueError("Latitude must be between -90 and 90")
        return latitude

    @staticmethod
    def _validate_longitude(longitude: float) -> float:
        """
        Validate longitude.

        Args:
            longitude: The longitude to validate.

        Returns:
            The validated longitude.

        Raises:
            ValueError: If validation fails.
        """
        try:
            longitude = float(longitude)
        except (TypeError, ValueError):
            raise ValueError("Longitude must be a number")

        if not -180.0 <= longitude <= 180.0:
            raise ValueError("Longitude must be between -180 and 180")
        return longitude

    def add_amenity(self, amenity_id: str) -> None:
        """
        Add an amenity to the place.

        Args:
            amenity_id: ID of the amenity to add.
        """
        if amenity_id not in self.amenities:
            self.amenities.append(amenity_id)

    def add_review(self, review_id: str) -> None:
        """
        Add a review to the place.

        Args:
            review_id: ID of the review to add.
        """
        if review_id not in self.reviews:
            self.reviews.append(review_id)

    def remove_review(self, review_id: str) -> None:
        """
        Remove a review from the place.

        Args:
            review_id: ID of the review to remove.
        """
        if review_id in self.reviews:
            self.reviews.remove(review_id)
