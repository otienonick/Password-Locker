from credentials import Credentials
import unittest


class TestCredentials(unittest.TestCase):

    def setUp(self):

        '''
        a method that runs before any test

        '''
        self.new_credential  = Credentials('twitter','oti','0084') #create a dummy credential

    def test_init(self):
        
        '''
        testcase to check if object or class is instanciated correctly

        '''
        self.assertEqual(self.new_credential.app_name,'twitter') 
        self.assertEqual(self.new_credential.username,'oti') 
        self.assertEqual(self.new_credential.password,'0084') 


    def test_save_credentials(self):

        '''
        testcase method to save objects into credentials list.

        '''
        self.new_credential.save_credentials() #saving credential
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()
