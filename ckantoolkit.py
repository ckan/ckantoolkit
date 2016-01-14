import sys

# XXX: required to prevent a mysterious
# "TypeError: expected string or Unicode object, NoneType found"
# in the _initialize() import statement
import ckan

class _CKANToolkit(object):
    """
    Late initialization to match ckan.plugins.toolkit
    """
    def __init__(self):
        self._toolkit = None

    def _initialize(self):
        import ckan.plugins.toolkit as tk
        self._toolkit = tk

    def __getattr__(self, name):
        if not self._toolkit:
            self._initialize()
        return getattr(self._toolkit, name)

    def __dir__(self):
        if not self._toolkit:
            self._initialize()
        return dir(self._toolkit)


# https://mail.python.org/pipermail/python-ideas/2012-May/014969.html
sys.modules[__name__] = _CKANToolkit()
