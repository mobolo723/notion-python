from __future__ import annotations

from typing import TypedDict, Optional, List, Union

from .emoji import *
from .enums import *
from .file import *
from .parent import *
from .user import *
from .rich_text import *

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
    # {type} An object containing type-specific block information.


class Bookmark(TypedDict):
    caption: List[Text]
    url: str


class Breadcrump(TypedDict):
    pass


class BulletedListItem(TypedDict):
    """Bulleted list item block objects contain the following information within the bulleted_list_item property"""
    rich_text: List[RichTextObjects]
    color: Color
    children: List[BlockObject]

class Callout(TypedDict):
    """Callout block objects contain the following information within the callout property"""
    rich_text: List[RichTextObjects]
    icon: Union[EmojiObject, File] # File object not Block Object File object -> to fix
    color: Color

class ChildDatabase(TypedDict):
    title: str


class ChildPage(TypedDict):
    title: str


class Code(TypedDict):
    caption: List[RichTextObjects] # may be Text
    rich_text: List[RichTextObjects] # may be Text
    language: str # todo create enums of lang


class Column(TypedDict):
    pass


class ColumnList(TypedDict):
    pass


class Divider(TypedDict):
    pass


class Embed(TypedDict):
    url: str


class Equation(TypedDict):
    expression: str


class File(TypedDict):
    caption: List[RichTextObjects]
    type: Union[FileType.FILE, FileType.EXTERNAL]
    file: FileObject
    name: str


class Headings(TypedDict):
    rich_text: List[RichTextObjects]
    color: Color
    is_toggleable: bool

class Heading1(Headings):
    pass

class Heading2(Headings):
    pass

class Heading3(Headings):
    pass


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


BlockObjects = Union[
    Bookmark, Breadcrump, BulletedListItem, Callout, ChildDatabase, ChildPage, Code, Column, ColumnList, Divider, Embed,
    Equation, File, Headings, Image, LinkPreview, Mention, NumberedListItem, Paragraph, Pdf, Quote, SyncedBlock, Table,
    TableOfContents, Template, Todo, Toggle, Video]
