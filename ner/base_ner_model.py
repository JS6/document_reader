class BaseNERModel:
    """
    Base class for Named Entity Recognition models.
    """

    def __init__(self):
        raise NotImplementedError(
            "This method should be overridden by subclasses"
        )  # noqa

    def extract(self, text):
        """
        Extract named entities from the given text.
        """
        raise NotImplementedError(
            "This method should be overridden by subclasses"
        )  # noqa
