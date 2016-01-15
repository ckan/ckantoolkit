import sys
import os


HERE = os.path.split(__file__)[0]

class TestOldCKAN(object):

    def setUp(self):
        sys.path.append(HERE + '/old_ckan')

    def tearDown(self):
        sys.path.remove(HERE + '/old_ckan')

    def test_import_ckan(self):
        import ckan
