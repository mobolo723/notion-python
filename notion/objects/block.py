from __future__ import annotations

from typing import TypedDict, Optional, List, Union

from .parent import *
from .user import *

__all__ = ('BlockObject',)


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
    ...


class Breadcrump(TypedDict):
    ...


class BulletedListItem(TypedDict):
    ...


class Callout(TypedDict):
    ...


class ChildDatabase(TypedDict):
    ...


class ChildPage(TypedDict):
    ...


class Code(TypedDict):
    ...


class Column(TypedDict):
    ...


class ColumnList(TypedDict):
    ...


class Divider(TypedDict):
    ...


class Embed(TypedDict):
    ...


class Equation(TypedDict):
    ...


class File(TypedDict):
    ...


class Headings(TypedDict):
    ...


class Image(TypedDict):
    ...


class LinkPreview(TypedDict):
    ...


class Mention(TypedDict):
    ...


class NumberedListItem(TypedDict):
    ...


class Paragraph(TypedDict):
    ...


class Pdf(TypedDict):
    ...


class Quote(TypedDict):
    ...


class SyncedBlock(TypedDict):
    ...


class Table(TypedDict):
    ...


class TableOfContents(TypedDict):
    ...


class Template(TypedDict):
    ...


class Todo(TypedDict):
    ...


class Toggle(TypedDict):
    ...


class Video(TypedDict):
    ...
