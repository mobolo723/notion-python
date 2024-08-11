from __future__ import annotations

from typing import TypedDict, Optional, List, Union

from .parent import *
from .user import *


__all__ = ('BlockObject', )


class BlockObject(TypedDict):
    object: str
    id: str
    parent: ParentObject
    type: str
    created_time: str
    created_by: str
    last_edited_time: str
    last_edited_by: UserObject  # partial
    archived: bool
    in_trash: bool
    has_children: bool

class Bookmark(TypedDict):
    caption