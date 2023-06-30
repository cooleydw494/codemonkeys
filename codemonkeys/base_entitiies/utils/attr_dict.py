class AttrDict(dict):
    """
    A custom dictionary class that allows attribute-like access.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self
