import unittest
import source
Source = source.Source

class SourceTest(unittest.TestCase):
    """Test Class to test the behaviour of the Source class"""

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_source = Source("ABC","Get news up by us","English")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()

