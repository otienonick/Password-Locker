from credentials import Credentials
import unittest


class TestCredentials(unittest.TestCase):

    def setUp(self):

        '''
        a method that runs before any test

        '''
        self.new_credential  = Credentials('oti','0084') #create a dummy credential

    def test_init(self):
        
        '''
        testcase to check if object or class is instanciated correctly

        '''
        self.assertEqual(self.new_credential.username,'oti') 
        self.assertEqual(self.new_credential.password,'0084') 


    


if __name__ == '__main__':
    unittest.main()
