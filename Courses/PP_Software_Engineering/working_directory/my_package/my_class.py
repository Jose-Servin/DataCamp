from tokenize import tokenize


class Document:
    """
    A minimal class example
    """

    def __init__(self, text):
        self.text = text
        # adding an underscore to show this method is intended for internal use only
        self.tokens = self._tokenize()

    def _tokenize(self):
        return tokenize(self.text)
