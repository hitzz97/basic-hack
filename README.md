# basic-hack

this app is just to play arround with friend not for malicious use
the .exe files where made with pyinstaller and for some reasons 
dont work as good as the .py file.

the app basically copies itself to windows startup folder,
"C:\\Users\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

The files in this folder are executed automatically when the pc starts.
so the app is executed and asks for email and password if not given
then the pc restarts, if provided then they are mailed to person whose 
email and password is written in the app.

to get the email from the app 
write your email in the py code and your password in the py code.

[HINT: if you want to prevent your pc from restarting open cmd and type the code 
       to abort shutdown. However if you will set this shutdown time too low then,
       one might not have enough time to fire up cmd and type the code ]
