""" Custom Framework Types """

# Note: PyCharm doesn't understand Optional/Union syntax correctly (I'd use Optional if possible)
# Thus, these custom type annotations are used as a workaround for type hinting where values can also be None.

OStr = str | None
"""
Type hint for an optional string value.

This type is used to indicate that a variable can be either of type `str` or `None`.
"""

OBool = bool | None
"""
Type hint for an optional boolean value.

This type is used to indicate that a variable can be either of type `bool` or `None`.
"""

OInt = int | None
"""
Type hint for an optional integer value.

This type is used to indicate that a variable can be either of type `int` or `None`.
"""

OFloat = float | None
"""
Type hint for an optional floating-point value.

This type is used to indicate that a variable can be either of type `float` or `None`.
"""
