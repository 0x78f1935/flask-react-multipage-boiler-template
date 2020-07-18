from backend.unittest.template import BoilerUnitTestTemplate
import unittest

class BoilerUnitTest(object):
    @classmethod
    def run(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(BoilerUnitTestTemplate)
        unittest.TextTestRunner().run(suite)
