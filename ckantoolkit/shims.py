
class HelpersNoMagic(object):
    """
    Access helper.functions as attributes, but raise AttributeError
    for missing functions instead of returning null_function

    adapted from ckan/config/environment.py:_HelpersNoMagic
    """
    def __init__(self, helpers):
        self._helpers = helpers

    def __getattr__(self, name):
        fn = getattr(self._helpers, name)
        if fn == self._helpers.null_function:
            raise AttributeError("No helper found named '%s'" % name)
        return fn
