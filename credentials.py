class Credentials:

    '''
    class that generates a new instance of credentials.
    '''
    
    credentials_list = []

    def __init__(self,app_name,username,password):

        '''
        a method that defines the properties of the class object.

        '''
        self.app_name = app_name
        self.username = username
        self.password = password

    def save_credentials(self):

        '''
         method that saves  credentials.
            
        '''
        Credentials.credentials_list.append(self) 

