"""In-memory repository for storing objects."""
from typing import Dict, List, Optional, Any


class InMemoryRepository:
    """In-memory storage repository implementing the Repository pattern."""

    def __init__(self):
        """Initialize the repository with an empty storage dictionary."""
        self._storage: Dict[str, Any] = {}

    def add(self, obj: Any) -> None:
        """
        Add an object to the repository.

        Args:
            obj: The object to add. Must have an 'id' attribute.
        """
        if not hasattr(obj, 'id'):
            raise ValueError("Object must have an 'id' attribute")
        self._storage[obj.id] = obj

    def get(self, obj_id: str) -> Optional[Any]:
        """
        Retrieve an object by its ID.

        Args:
            obj_id: The unique identifier of the object.

        Returns:
            The object if found, None otherwise.
        """
        return self._storage.get(obj_id)

    def get_all(self) -> List[Any]:
        """
        Retrieve all objects from the repository.

        Returns:
            A list of all stored objects.
        """
        return list(self._storage.values())

    def update(self, obj_id: str, data: Dict[str, Any]) -> Optional[Any]:
        """
        Update an object with the given data.

        Args:
            obj_id: The unique identifier of the object.
            data: Dictionary containing the attributes to update.

        Returns:
            The updated object if found, None otherwise.
        """
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                if hasattr(obj, key):
                    setattr(obj, key, value)
        return obj

    def delete(self, obj_id: str) -> bool:
        """
        Delete an object from the repository.

        Args:
            obj_id: The unique identifier of the object.

        Returns:
            True if the object was deleted, False otherwise.
        """
        if obj_id in self._storage:
            del self._storage[obj_id]
            return True
        return False

    def get_by_attribute(self, attr_name: str, attr_value: Any) -> List[Any]:
        """
        Retrieve objects by a specific attribute value.

        Args:
            attr_name: The name of the attribute to filter by.
            attr_value: The value to match.

        Returns:
            A list of objects matching the criteria.
        """
        return [
            obj for obj in self._storage.values()
            if hasattr(obj, attr_name) and getattr(obj, attr_name) == attr_value
        ]
