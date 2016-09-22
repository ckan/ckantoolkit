import sys
import os

from nose.tools import assert_raises

HERE = os.path.split(__file__)[0]

class TestOldCKAN(object):
    def setUp(self):
        sys.path.append(HERE + '/old_ckan')

    def tearDown(self):
        sys.path.remove(HERE + '/old_ckan')

    def test_import_ckan(self):
        import ckan
        assert 'old_ckan' in ckan.__path__[0]

    def test_import_literal(self):
        from ckantoolkit import literal
        assert literal == 'figurative'

    def test_import_ungettext(self):
        from ckantoolkit import ungettext
        assert ungettext == 'many things'

    def test_import_DefaultGroupForm(self):
        from ckantoolkit import DefaultGroupForm
        assert DefaultGroupForm == 'formy'

    def test_import_missing(self):
        from ckantoolkit import missing
        assert missing == 'present and reporting'

    def test_import_tests(self):
        from ckantoolkit.tests.helpers import thing
        assert thing == 'that helps'

    def test_import_StopOnError(self):
        from ckantoolkit import StopOnError
        assert StopOnError == 'do not pass go'

    def test_import_DefaultOrganizationForm(self):
        from ckantoolkit import DefaultOrganizationForm
        assert DefaultOrganizationForm == 'disorderly'

    def test_import_h_existing_attr(self):
        from ckantoolkit import h
        assert h.icon_url('a') == 'a'

    def test_import_h_missing_attr(self):
        from ckantoolkit import h
        assert_raises(AttributeError, getattr, h, 'no_helper_named_like_this')

    def test_import_config(self):
        from ckantoolkit import config
        assert config['mock_pylons_config']
