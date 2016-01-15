import sys
import os


HERE = os.path.split(__file__)[0]

class TestOldCKAN(object):
    def setUp(self):
        sys.path.append(HERE + '/new_ckan')

    def tearDown(self):
        sys.path.remove(HERE + '/new_ckan')

    def test_import_ckan(self):
        import ckan
        assert 'new_ckan' in ckan.__path__[0]

    def test_import_literal(self):
        from ckantoolkit import literal
        assert literal == 'one from toolkit'

    def test_import_ungettext(self):
        from ckantoolkit import ungettext
        assert ungettext == 'two from toolkit'

    def test_import_DefaultGroupForm(self):
        from ckantoolkit import DefaultGroupForm
        assert DefaultGroupForm == 'three from toolkit'

    def test_import_missing(self):
        from ckantoolkit import missing
        assert missing == 'four from toolkit'
