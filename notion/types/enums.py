"""This file contains all string enums types listed in the API."""

from __future__ import annotations

from enum import Enum

__all__ = (
    'BlockType',
    'PageType',
    'Color',
    'RichTextType',
    'MentionType',
    'FileType',
    'ImageType'
)


class BlockType(str, Enum):
    BOOKMARK = "bookmark"
    BREADCRUMB = "breadcrumb"
    BULLETED_LIST_ITEM = "bulleted_list_item"
    CALLOUT = "callout"
    CHILD_DATABASE = "child_database"
    CHILD_PAGE = "child_page"
    COLUMN = "column"
    COLUMN_LIST = "column_list"
    DIVIDER = "divider"
    EMBED = "embed"
    EQUATION = "equation"
    FILE = "file"
    HEADING_1 = "heading_1"
    HEADING_2 = "heading_2"
    HEADING_3 = "heading_3"
    IMAGE = "image"
    LINK_PREVIEW = "link_preview"
    LINK_TO_PAGE = "link_to_page"
    NUMBERED_LIST_ITEM = "numbered_list_item"
    PARAGRAPH = "paragraph"
    PDF = "pdf"
    QUOTE = "quote"
    SYNCED_BLOCK = "synced_block"
    TABLE = "table"
    TABLE_OF_CONTENTS = "table_of_contents"
    TABLE_ROW = "table_row"
    TEMPLATE = "template"
    TO_DO = "to_do"
    TOGGLE = "toggle"
    UNSUPPORTED = "unsupported"
    VIDEO = "video"


class PageType(str, Enum):
    CHECKBOX = "checkbox"
    CREATED_BY = "created_by"
    CREATED_TIME = "created_time"
    DATE = "date"
    EMAIL = "email"
    FILES = "files"
    FORMULA = "formula"
    LAST_EDITED_BY = "last_edited_by"
    LAST_EDITED_TIME = "last_edited_time"
    MULTI_SELECT = "multi_select"
    NUMBER = "number"
    PEOPLE = "people"
    PHONE_NUMBER = "phone_number"
    RELATION = "relation"
    ROLLUP = "rollup"
    RICH_TEXT = "rich_text"
    SELECT = "select"
    STATUS = "status"
    TITLE = "title"
    URL = "url"
    UNIQUE_ID = "unique_id"
    VERIFICATION = "verification"


class Color(str, Enum):
    BLUE = "blue"
    BLUE_BACKGROUND = "blue_background"
    BROWN = "brown"
    BROWN_BACKGROUND = "brown_background"
    DEFAULT = "default"
    GRAY = "gray"
    GRAY_BACKGROUND = "gray_background"
    GREEN = "green"
    GREEN_BACKGROUND = "green_background"
    ORANGE = "orange"
    ORANGE_BACKGROUND = "orange_background"
    YELLOW = "yellow"
    YELLOW_BACKGROUND = "yellow_background"
    PINK = "pink"
    PINK_BACKGROUND = "pink_background"
    PURPLE = "purple"
    PURPLE_BACKGROUND = "purple_background"
    RED = "red"
    RED_BACKGROUND = "red_background"


class RichTextType(str, Enum):
    TEXT = "text"
    MENTION = "mention"
    EQUATION = "equation"


class MentionType(str, Enum):
    DATABASE = "database"
    DATE = "date"
    LINK_PREVIEW = "link_preview"
    PAGE = "page"
    TEMPLATE_MENTION = "template_mention"
    USER = "user"


class FileType(str, Enum):
    EXTERNAL = 'external'
    FILE = 'file'


class ImageType(str, Enum):
    BMP = '.bmp'
    GIF = '.gif'
    HEIC = '.heic'
    JPEG = '.jpeg'
    JPG = '.jpg'
    PNG = '.png'
    SVG = '.svg'
    TIF = '.tif'
    TIFF = '.tiff'
