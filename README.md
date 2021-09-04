# Password Locker

#### Developer
#### Nick Otieno

### Project Description

   - An application that helps a logged in user manage his/her social media passwords and even generate new ones and save them.

### Setup Requirements
    - Github
    - Code Editor

### Setup Installation 
    - Fork app from github
    - Clone the app in your terminal using $git clone command
    - Run the code in your code editor  using :
    $ chmod +x run.py
    $ ./run.py command

    

## BDD
|Behaviour|Input|Output|
|:--------|:-------|:------|
|Run the application in the terminal of your code editor|$ ./run.py|Hello what is your name?|
|input your name|name|Welcome name to Password locker what do you want to do? -ca - create a new account , lg - login to your account xx-exit
| input ca|input username,password and comfirm password|congratualtions username new account created.Proceed to login|
|input lg|input created username and password| logged in successfully where would you like to navigate to? sc-store your credentials, cr-create new credentials dc-display your credentials, dd-delete existing credentials, cu-copy user credentials to clipboard,ex-logout|
input sc|input application name,username and password|your application name have been successfully saved|
input cr|input application name and username|Choose the following options: 1 - create my own password , 2 - let password locker generate a password for me|
|input dc|dc|Here is a list of all your credentials|
|input dd|enter the name application name of the credential to be deleted|application credentials has been successfully deleted|
|input cu|enter the application name of the credential you want to copy|application credentials have been successfully copied to clip board|
|input ex| ex|you are logged out ...bye|

   
### Known Bugs
    The application works perfectly well,there are no known bugs.

### Technologies used
    - Python


#### Contacts:
#### Email :otienonick70@gmail.com
#### &copy;2021 Nick Otieno.    