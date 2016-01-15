import sys
import os


HERE = os.path.split(__file__)[0]

class TestOldCKAN(object):
    def setUp(self):
        sys.path.append(HERE + '/old_ckan')

    def tearDown(self):
        sys.path.remove(HERE + '/old_ckan')
        for m in sys.modules:
            if m.startswith('ckan.'):
                del sys.modules[m]

    def test_import_ckan(self):
        import ckan
        assert 'old_ckan' in ckan.__path__[0]

    def test_import_literal(self):
        from ckantoolkit import literal
        assert literal == 'hitler'

    def test_import_ungettext(self):
        from ckantoolkit import ungettext
        assert ungettext == 'many things'

    def test_import_DefaultGroupForm(self):
        from ckantoolkit import DefaultGroupForm
        assert DefaultGroupForm == 'formy'

    def test_import_missing(self):
        from ckantoolkit import missing
        assert missing == 'present and reporting'
