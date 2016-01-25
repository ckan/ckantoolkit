import sys

# XXX: required to prevent a mysterious
# "TypeError: expected string or Unicode object, NoneType found"
# in the ckan.plugins.toolkit import statement
import ckan

class _CKANToolkit(object):
    """
    Late initialization to match ckan.plugins.toolkit
    """
    __path__ = __path__

    def __getattr__(self, name):
        import ckan.plugins.toolkit as tk

        try:
            value = getattr(tk, name)
        except AttributeError:
            # backports here:
            if name == 'ungettext':
                from ckan.common import ungettext as value
            elif name == 'DefaultGroupForm':
                from ckan.lib.plugins import DefaultGroupForm as value
            elif name == 'missing':
                from ckan.lib.navl.dictization_functions import missing as value
            elif name == 'StopOnError':
                from ckan.lib.navl.dictization_functions import StopOnError as value
            elif name == 'DefaultOrganizationForm':
                from ckan.lib.plugins import DefaultOrganizationForm as value
            elif name == 'h':
                import pylons
                from ckantoolkit.shims import HelpersNoMagic
                value = HelpersNoMagic(pylons.config['pylons.h'])
            else:
                raise
        setattr(self, name, value) # skip this function next time
        return value

    def __dir__(self):
        import ckan.plugins.toolkit as tk
        return dir(tk)


# https://mail.python.org/pipermail/python-ideas/2012-May/014969.html
sys.modules[__name__] = _CKANToolkit()
