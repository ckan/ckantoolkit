import sys
import os

HERE = os.path.split(__file__)[0]


class TestNewCKAN(object):
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

    def test_import_tests(self):
        from ckantoolkit.tests.helpers import thing
        assert thing == 'in the right place'

    def test_import_StopOnError(self):
        from ckantoolkit import StopOnError
        assert StopOnError == 'five from toolkit'

    def test_import_DefaultOrganizationForm(self):
        from ckantoolkit import DefaultOrganizationForm
        assert DefaultOrganizationForm == 'six from toolkit'

    def test_import_h(self):
        from ckantoolkit import h
        assert h == 'seven from toolkit'

    def test_import_config(self):
        from ckantoolkit import config
        assert config == 'eight from toolkit'

    def test_import_HelperError(self):
        from ckantoolkit import HelperError
        assert HelperError == 'nine from toolkit'
