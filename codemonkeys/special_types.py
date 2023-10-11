from codemonkeys.utils.imports.monkey import Monkey

"""Custom Framework Types which are more likely to trigger circular imports if not separated."""

# Note: PyCharm doesn't understand Optional/Union syntax correctly (I'd use Optional if possible)
OMonkey = Monkey | None
