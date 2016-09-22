class _Helpers(object):
    @classmethod
    def null_function(*args, **kwargs):
        return ''

    def __getattr__(self, name):
        return self.null_function

    def icon_url(self, x):
        return x

config = {
    'pylons.h': _Helpers(),
    'mock_pylons_config': True,
}
