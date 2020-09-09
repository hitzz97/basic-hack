# basic-hack

this app is just to play arround with friends not for malicious use.
The ".exe" files where made with pyinstaller and for some reasons 
dont work as good as the ".py" file.

## just trick someone into running it once.

[ NOTE: python must be installed and all ".py" files must be set to run with 
       python when executed. If not then you will have to explicitly execute it 
       once on your friends pc ]

When executed, the app copies itself to windows startup folder,
"C:\\Users\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

[ NOTE: if you are able to delete this copy of app then, the app will not run on startup ]

[ Possible update : There are ways to modify windows registry so that the app gets executed automatically on startup ]

The files in this startup folder are executed automatically when the pc starts.
so the app is executed and asks for email and password if not given
then the pc restarts, if provided then they are mailed to person whose 
email and password is written in the app.

to get the email from the app 
write your email in the py code and your password in the py code.

[ HINT: if you want to prevent your pc from restarting open cmd and type the code 
       to abort shutdown. However if you will set this shutdown time too low then,
       one might not have enough time to fire up cmd and type the code ]
