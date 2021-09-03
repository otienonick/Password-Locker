import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):

        '''
        a method that runs before any test

        '''
        self.new_user  = User('nick','1982') #create a dummy user

    def test_init(self):
        
        '''
        testcase to check if object or class is instanciated correctly

        '''
        self.assertEqual(self.new_user.username,'nick') 
        self.assertEqual(self.new_user.password,'1982') 

    def test_save_user(self):

        '''
        testcase to check if user details have been saved.

        '''  
        self.new_user.save_user() #saving new user
        self.assertEqual(len(User.user_list),1)  


    def test_user_exists(self):
        
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user")
        test_user.save_user()

        user_exists = User.user_exist("Test","user")

        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()


