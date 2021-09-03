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


    def tearDown(self):

        '''
        teardown method that does clean up after each test case has run.

        '''
        Credentials.credentials_list = []
        
    def test_save_multiple_credentials(self):
        
        '''
        testcase to check if user can save multiple credentials to the credentials_list

        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials('app','credential','2021')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)  

    def test_find_by_app(self):
        
        '''
        test to check if we can find a user's credentials by appname and display information.

        '''

        self.new_credential.save_credentials()
        test_credentials = Credentials('app','credential','2021') # new contact
        test_credentials.save_credentials()

        found_credential = Credentials.find_by_app('app')

        self.assertEqual(found_credential.username,test_credentials.username)

    def test_credential_exists(self):

        '''
        test to check if we can return a Boolean  if we cannot find the user's credentials.

        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials('app','credential','2021') # new contact
        test_credentials.save_credentials()

        credential_exists = Credentials.user_credential_exist('app')

        self.assertTrue(credential_exists)


if __name__ == '__main__':
    unittest.main()
