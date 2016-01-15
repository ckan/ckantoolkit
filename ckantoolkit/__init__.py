import sys

# XXX: required to prevent a mysterious
# "TypeError: expected string or Unicode object, NoneType found"
# in the _initialize() import statement
import ckan

class _CKANToolkit(object):
    """
    Late initialization to match ckan.plugins.toolkit
    """
    __path__ = __path__

    def __init__(self):
        self._toolkit = None

    def _initialize(self):
        import ckan.plugins.toolkit as tk
        self._toolkit = tk

    def __getattr__(self, name):
        if not self._toolkit:
            self._initialize()
        try:
            value = getattr(self._toolkit, name)
        except AttributeError:
            # backports here:
            if name == 'ungettext':
                from ckan.common import ungettext as value
            elif name == 'DefaultGroupForm':
                from ckan.lib.plugins import DefaultGroupForm as value
            elif name == 'missing':
                from ckan.lib.navl.dictization_functions import missing as value
            else:
                raise
        setattr(self, name, value) # skip this function next time
        return value

    def __dir__(self):
        if not self._toolkit:
            self._initialize()
        return dir(self._toolkit)


# https://mail.python.org/pipermail/python-ideas/2012-May/014969.html
sys.modules[__name__] = _CKANToolkit()
