"""
    Restful service response entity.
"""

from dataclasses import dataclass, field
import typing as t

from helpers import JSONSerialazable

@dataclass(frozen=True)
class ResponseTemplate(JSONSerialazable):
    success: bool
    payload: t.Dict[str, t.Any] = field(default_factory=dict)
    error: str = field(default=None)

    def to_json(self) -> t.Dict[str, t.Any]:
        template = {
            "success": self.success,
            "payload": self.payload
        }

        if err := self.error:
            template['error'] = err

        return template

t = ResponseTemplate(True)
print(t.to_json())
