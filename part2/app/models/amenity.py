"""Amenity model."""
from app.models.base import BaseModel


class Amenity(BaseModel):
    """Amenity entity representing an amenity in the system."""

    def __init__(self, name: str):
        """
        Initialize an Amenity instance.

        Args:
            name: Amenity name.

        Raises:
            ValueError: If validation fails.
        """
        super().__init__()
        self.name = self._validate_name(name)

    @staticmethod
    def _validate_name(name: str) -> str:
        """
        Validate amenity name.

        Args:
            name: The name to validate.

        Returns:
            The validated name.

        Raises:
            ValueError: If validation fails.
        """
        if not name or not isinstance(name, str):
            raise ValueError("Name is required and must be a string")
        if len(name) > 50:
            raise ValueError("Name must not exceed 50 characters")
        return name
