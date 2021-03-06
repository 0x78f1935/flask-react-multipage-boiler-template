from backend import Webserver
import unittest

class BoilerUnitTestTemplate(unittest.TestCase):

    def setUp(self):
        server = Webserver()._start()
        self.server = server.test_client()

    def tearDown(self):
        pass

    def test_homepage(self):
        """
        Checks if homepage exists
        """
        response = self.server.get('/')
        self.assertEqual(response.status_code, 200)
        print("* Internal pages are available!")

    def test_aboutpage(self):
        """
        Checks if about page exists
        """
        response = self.server.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_marbles(self):
        """
        Checks if marble page exists
        """
        response = self.server.get('/marbles')
        self.assertEqual(response.status_code, 200)