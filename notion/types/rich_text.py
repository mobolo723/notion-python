from __future__ import annotations

from typing import TypedDict, Optional, Union, Dict, TYPE_CHECKING
from .enums import *

__all__ = (
    'RichTextObject',
    'Equation',
    'Mention',
    'Text',
    'Annotation',
    'RichTextObjects'
)

if TYPE_CHECKING:




class RichTextObject(TypedDict):
    type: RichTextType
    object: Union[Equation, Mention, Text]
    annotations: Annotation
    plain_text: str
    href: Optional[str]


class Equation(TypedDict):
    expression: str


class Mention(TypedDict):
    type: MentionType
    object: Union[Database, Date, LinkPreview, Page, TemplateMention, User]


class Text(TypedDict):
    content: str
    link: Optional[Dict[str, str]]


class Annotation(TypedDict):
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: Color


RichTextObjects = Union[Equation, Mention, Text]
