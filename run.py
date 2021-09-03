#!/usr/bin/env python3.6

from user import User
def create_user(user_name,pwd):
    '''
    function to create a new user

    '''
    new_user = User(user_name,pwd)
    return new_user

def save_users(details):
    '''
    function to save user details

    '''
    details.save_users()    


def main():

        print('Helo welcome to Password Locker.What is your name?')

        user_name = input()

        print(f'Hello {user_name}. what would you like to do?')
        print('\n')

        while True:
            print('Use these short codes : cu - create a new user ,lg - login to your account ,ex - exit')

            short_code =  input().lower()

            if short_code == 'cu':

                print('Username ....')

                user_names = input()

                print('password .....')

                pwds = input()

                save_users(create_user(user_names,pwds))
                print(f'New user:{user_names} {pwds} created')

if __name__ == '__main__':
    main()