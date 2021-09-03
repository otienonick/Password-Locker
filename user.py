class User:
    
    '''
    a class that generates an instance of a new user

    '''
    user_list =[]
    
    def __init__(self,username,password):

        '''
        a method that defines the properties of the class object

        '''
        
        self.username =username
        self.password = password

    def save_user(self):

        '''
         method that saves user details
            
        '''
        User.user_list.append(self)    
        
 