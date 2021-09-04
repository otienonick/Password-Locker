#!/usr/bin/env python3.6

import random
import pyperclip
from user import User
from credentials import Credentials

def create_user(user_name,pwd):

    '''
    function to create a new user

    '''
    new_user = User(user_name,pwd)
    return new_user

def save_users(user):
    '''
    function to save user details

    '''
    user.save_user()    

def check_existing_user(user,pwd3):

    '''
    function that checks if a user exists 

    '''
    return User.user_exist(user,pwd3)



def create_credential(app,name,passcode):

    '''
    function to create a new user

    '''
    new_credential = Credentials(app,name,passcode)
    return new_credential
   

def credentials_saved(credentials):

    '''
    function that will save user credentials

    '''
    credentials.save_credentials()

def find_credential(appname):

    '''
    function that finds a user's credentials by appname and returns the credentials

    '''
    return Credentials.find_by_app(appname)     

def check_existing_user_credential(appname):

    '''
    function that checks if a user's details exists with that appname and returns a boolean.

    '''
    return Credentials.user_credential_exist(appname)


def display_credentials():
    '''
    Function that returns all the saved user's credentials.
    '''
    return Credentials.display_user_credential()     

def delete_credentials(credentials):

    '''
    a function that deletes a user's credentials

    '''
    return Credentials.credentials_list.remove(credentials)

def copy_credentials(user_found):
    return pyperclip.copy(user_found.username)  

    

def main():

        print('Hello welcome to PASSWORD LOCKER. What is your name?')

        user_name = input()

        print(f'Hello {user_name}. what would you like to do?')
        print('.'*20)

        print('\n')

        while True:
            print('Use these short codes : ca - create a new account ,lg - login to your account ,xx - exit')

            short_code =  input().lower()

            if short_code == 'ca':

                print('Username:')

                user_names = input()

                print('password:')

                pwds = input()

                print('comfirm password:')

                pwds2 = input()
                

                if pwds == pwds2:

                    save_users(create_user(user_names,pwds))

                    print('\n')

                    print(f' Congratulations {user_names}!! New account successfully created.'.upper())

                    print('\n')
                
                    print('Proceed to login:'.upper())

                else:

                    print('passwords do not match!')

              
            elif short_code == 'lg':

                print('Welcome!!!')

                print('username:')

                my_user_name = input()

                print('password:')

                my_pwd = input()

                if check_existing_user(my_user_name,my_pwd):

                    print('\n')

                    print(f'logged in successfully ! Where would you like to navigate to {my_user_name}? ')

                    print('\n')
                    print('.' *20)

                    while True:

                        print('Use these short codes : sc - store your credentials ,cr- create new credentials dc - display your credentials , dd - delete existing credentials , cu - copy user credentials to clipboard , ex - logout')
                        print('.'*20)
                        
                        shorter_code =  input().lower()


                        if shorter_code == 'sc':

                            print('name of application:')
                            application_name = input()

                            print('username:')

                            credential_user = input()

                            print('password:')

                            credential_password = input()

                            credentials_saved(create_credential(application_name,credential_user,credential_password))

                            print(f'Your {application_name} credentials have been successfully saved')
                            print('\n')
                            print('.' *50)

                        elif shorter_code == 'cr':

                            print('name of application:')

                            appname = input()

                            print('Your Username:')

                            app_user_name =input()

                            while True:

                                print ( 'Choose the following options: 1 - create my own password , 2 - let password locker generate a password for me')
                                print('.'*50)

                                options = input()

                                if options == '1':
                                    print('create password:') 

                                    password = input()

                                elif options =='2':

                                    print(f'what length would you like your password to be {app_user_name}?')

                                    pwd_length = int(input())

                                    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#&()*'

                                    password  = ''
                                    for i in range(0,pwd_length):
                                        i = random.choice(chars)
                                        password = password + i
                          
                                    print(f'here is your password : {password}')
                                    print('\n')
                              
                                break
                  
                            credentials_saved(create_credential(appname,app_user_name,password))
                            
                            print(f' Your {appname} credentials have been successfully saved')
                            print('\n')
                            print('.' *50)

                        elif shorter_code == 'dc':
                            if display_credentials():
                                print('Here is a list of all your saved  credentials')
                                print('\n')
                                print('.'*50)

                                for detail in display_credentials():
                                    print(f'application name:{detail.app_name}') 
                                    print(f'username: {detail.username}')
                                    print(f' password:{detail.password}')

                                print('\n')
                            else:
                                print('You dont seem to have any  app credentials saved yet')
                                print('\n')

                        elif shorter_code == 'dd':

                            print('Enter the application name of the credentials yo want to delete')

                            search_app = input()

                            if check_existing_user_credential(search_app):

                                delete_app = find_credential(search_app)

                                delete_credentials(delete_app)

                                print(f'{delete_app.app_name} has been successfully deleted')

                            else:

                                print('That app does not exist in your credentials list')
                                print('\n')
                        
                        elif shorter_code == 'cu':
                            print('enter the app name of the credentials you want copy')
                            search_app = input()
                            if check_existing_user_credential(search_app):
                                copy_app_details = find_credential(search_app)
                                copy_credentials(copy_app_details)

                                print(f'{copy_app_details.app_name} credentials have been succesfully copied to clipboard')
                                print('\n')
                                print('.' *50)

                            else:
                                print(f'{search_app} does not exist in your credentials list')    

                        elif shorter_code == 'ex':
                            print('you are logged out...bye')
                            break       

                        else:
                            print('Please use the short codes')    
                else:    

                    print('Account does not exist!')

            elif short_code == 'xx':
                print('bye')
                break

            else:

                print('Please use the short codes')      


if __name__ == '__main__':
    main()