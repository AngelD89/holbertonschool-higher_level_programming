"""Review model."""
from app.models.base import BaseModel


class Review(BaseModel):
    """Review entity representing a review in the system."""

    def __init__(self, text: str, rating: int, place_id: str, user_id: str):
        """
        Initialize a Review instance.

        Args:
            text: Review text/comment.
            rating: Rating value (1-5).
            place_id: ID of the place being reviewed.
            user_id: ID of the user who wrote the review.

        Raises:
            ValueError: If validation fails.
        """
        super().__init__()
        self.text = self._validate_text(text)
        self.rating = self._validate_rating(rating)
        self.place_id = place_id
        self.user_id = user_id

    @staticmethod
    def _validate_text(text: str) -> str:
        """
        Validate review text.

        Args:
            text: The text to validate.

        Returns:
            The validated text.

        Raises:
            ValueError: If validation fails.
        """
        if not text or not isinstance(text, str):
            raise ValueError("Review text is required and must be a string")
        if len(text.strip()) == 0:
            raise ValueError("Review text cannot be empty")
        return text

    @staticmethod
    def _validate_rating(rating: int) -> int:
        """
        Validate rating.

        Args:
            rating: The rating to validate.

        Returns:
            The validated rating.

        Raises:
            ValueError: If validation fails.
        """
        try:
            rating = int(rating)
        except (TypeError, ValueError):
            raise ValueError("Rating must be an integer")

        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        return rating
