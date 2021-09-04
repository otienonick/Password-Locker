import pyperclip
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

    @classmethod

    def find_by_app(cls,appname):

        '''
        Method that takes in an appname and returns user's credential that matches that appname.

        Args:
            appname: appname to search for
        Returns :

            user's credentials that matches the appname.
        '''

        for app_credential in cls.credentials_list:
            if app_credential.app_name == appname:
                return app_credential


    @classmethod
    def user_credential_exist(cls,appname):

        '''
        Method that checks if a user's credantial details exists from the credentials list.

        Args:
            appname: appname to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for app_credential in cls.credentials_list:
            if app_credential.app_name == appname:
                    return True

        return False



    @classmethod
    def display_user_credential(cls):
        '''
        method that returns the credentials  list.

        '''
        return cls.credentials_list  

    def deleted_credentials(self):
        '''
        method that deletes saved credentials from the list.
        '''
        Credentials.credentials_list.remove(self)    

    @classmethod
    def copy_credentials(cls,appname):
        user_found = Credentials.find_by_app(appname)
        pyperclip.copy(user_found.username)
 
    