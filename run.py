#!/usr/bin/env python3.6

from user import User
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


def main():

        print('Helo welcome to Password Locker.What is your name?')

        user_name = input()

        print(f'Hello {user_name}. what would you like to do?')

        print('\n')

        while True:
            print('Use these short codes : ca - create a new account ,lg - login to your account ,ex - exit')

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

                    print(f'logged in successfully ! Welcome {my_user_name} where would you like to navigate to ? ')

                    print('\n')

                    while True:

                        print('Use these short codes : sc - store your credentials ,cr- create new credentials dc - display your credentials , dd - delete existing credentials ,ex - logout')
                        
                        shorter_code =  input().lower()


                        if shorter_code == 'sc':

                            print('chill')

                        break



                else:    

                    print('Account does not exist!')

                    


if __name__ == '__main__':
    main()