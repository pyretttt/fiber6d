"""
    Feed response entity.
"""

from dataclasses import dataclass, field
import typing as t

from helpers import JSONSerialazable

@dataclass(frozen=True)
class FeedResponse(JSONSerialazable):
    """
        Feed response entity.
    """
    type: str
    widgets: t.List[t.Dict[str, t.Any]] = field(default_factory=list)
    extra_info: t.Dict[str, t.Any] = field(default_factory=dict)

    def to_json(self) -> t.Dict[str, t.Any]:
        template = {
            'type': self.type,
            'widgets': self.widgets
        }
        if info := self.extra_info:
            template['extraInfo'] = info

        return template

