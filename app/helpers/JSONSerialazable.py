"""
    JSON serialization ABC.
"""

from abc import ABC, abstractmethod
import typing as t

class JSONSerialazable(ABC):
    """
        JSON serialization ABC.
    """

    @abstractmethod
    def to_json(self) -> t.Dict[str, t.Any]:
        pass