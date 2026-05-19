"""ID generator classes for creating unique identifiers."""
from abc import ABC, abstractmethod
import uuid
import random


class IDGenerator(ABC):  # pylint: disable=too-few-public-methods
    """Abstract base class for ID generators."""

    @abstractmethod
    def get_id(self):
        """Return a unique ID."""


class AlphaNumericIDGenerator(IDGenerator):  # pylint: disable=too-few-public-methods
    """Generates UUID-based alphanumeric IDs."""

    def get_id(self):
        """Return a UUID1-based string ID."""
        return str(uuid.uuid1())


class NumericIDGenerator(IDGenerator):  # pylint: disable=too-few-public-methods
    """Generates random numeric IDs."""

    def get_id(self):
        """Return a random integer ID."""
        return random.randint(10000, 100000000000)
