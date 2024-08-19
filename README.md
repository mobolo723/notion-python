Python package for Notion API. As API version from April 2024

# Structure

As Notion API provides JSON object with fields name equals to the type of the object, I added a common field
name `object` that can be any type. This field name has to be translated during the execution (reponding or reading
response) in order to preserve API
structure. Property should be used in the future to match object name attribute.

# Ressources

* [Notion API documentation](https://developers.notion.com/reference)