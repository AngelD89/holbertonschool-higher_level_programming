"""User model."""
import re
from app.models.base import BaseModel


class User(BaseModel):
    """User entity representing a user in the system."""

    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        """
        Initialize a User instance.

        Args:
            first_name: User's first name.
            last_name: User's last name.
            email: User's email address.
            password: User's password.

        Raises:
            ValueError: If validation fails.
        """
        super().__init__()
        self.first_name = self._validate_name(first_name, "First name")
        self.last_name = self._validate_name(last_name, "Last name")
        self.email = self._validate_email(email)
        self.password = password  # In production, this should be hashed
        self.is_admin = False

    @staticmethod
    def _validate_name(name: str, field_name: str) -> str:
        """
        Validate name fields.

        Args:
            name: The name to validate.
            field_name: The name of the field for error messages.

        Returns:
            The validated name.

        Raises:
            ValueError: If validation fails.
        """
        if not name or not isinstance(name, str):
            raise ValueError(f"{field_name} is required and must be a string")
        if len(name) > 50:
            raise ValueError(f"{field_name} must not exceed 50 characters")
        return name

    @staticmethod
    def _validate_email(email: str) -> str:
        """
        Validate email format.

        Args:
            email: The email to validate.

        Returns:
            The validated email.

        Raises:
            ValueError: If validation fails.
        """
        if not email or not isinstance(email, str):
            raise ValueError("Email is required and must be a string")

        # Basic email validation pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValueError("Invalid email format")

        return email

    def to_dict(self) -> dict:
        """
        Convert user to dictionary, excluding password.

        Returns:
            Dictionary representation without password.
        """
        user_dict = super().to_dict()
        # Remove password from the response
        if 'password' in user_dict:
            del user_dict['password']
        return user_dict
