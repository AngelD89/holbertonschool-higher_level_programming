"""Base model for all entities."""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models with common attributes."""

    def __init__(self):
        """Initialize base model with id and timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, data: dict) -> None:
        """
        Update the model instance with the provided data.

        Args:
            data: Dictionary containing attributes to update.
        """
        for key, value in data.items():
            if hasattr(self, key) and key not in ['id', 'created_at']:
                setattr(self, key, value)
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        Convert the model instance to a dictionary.

        Returns:
            Dictionary representation of the model.
        """
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value
        return result
