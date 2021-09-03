import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):

        '''
        a method that runs before any test

        '''
        self.new_user  =User('nick','1982') #create a dummy user

    def test_init(self):
        
        '''
        testcase to check if object or class is instanciated correctly

        '''    


        