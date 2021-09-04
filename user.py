class User:
    
    '''
    a class that generates an instance of a new user

    '''
    user_list =[]
    
    def __init__(self,username,password):

        '''
        a method that defines the properties of the class object

        '''
        
        self.username = username
        self.password = password

    def save_user(self):

        '''
         method that saves user details
            
        '''
        User.user_list.append(self)    
        

    @classmethod
    def user_exist(cls,my_used_name,my_used_password):
        '''
        Method that checks if a user exists from the user_list.
        Args:
            number: username and password to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == my_used_name:
                    return True

        return False
        
 