Basic discord bot made with python, for free music downloading, cuz why not.


For educational purposes only!

RIGHT NOW ONLY WORKS WITH CHROME 135.x.x.x, TO CHECK:
GO to the 3 dots on the top right > Help > About Google Chrome


YOU NEED TO USE CHROME, IF YOU DON'T WANT TO MESS AROUND WITH THE SETTINGS. I used the undetected_chromedriver to bypass cloudflare
THIS ALSO USES PYTHON, SO MAKE SURE YOU HAVE THAT INSTALLED AND READY

WARNING!!!
UNDETECTED_CHROMEDRIVER DOES NOT HIDE YOUR IP ADDRESS, SO YOU MIGHT NEED TO USE VPN IF YOU DON'T WANT TO GET FLAGGED.


In the terminal:
```bash
git clone git@github.com:endtrastic/spotbot.git
```


THEN LOCATE THE PATH AND OPEN IT IN VS CODE OR WHATEVER YOU WANT TO USE!


On the main path in the terminal run:

```bash
pip install -r requirements.txt
```
!!!! OR (if the part before didn't work!)

```bash
py -3.11 -m pip install -r requirements.txt
```

AFTER THAT!



Fill out the .env file, 
![image](https://github.com/user-attachments/assets/28a93003-94b6-4d69-a336-0ca2dcc45356)
MAKE SURE TO SAVE THE FILE WITH THE INFO YOU ENTERED: CTRL + S for WINDOWS.


TO RUN THE BOT, MAKE SURE IN THE TERMINAL, YOUR PATH ENDS WITH: bot/ 
(To check path ending in the terminal, type this in the terminal ofc)
```bash
pwd
```
To get there, on the main path enter: 

```bash
cd bot
```

To go back: 
```bash
cd ..
```
if you fucked up

ONCE ON THE PATH ENDING WITH: \bot
![pilt](https://github.com/user-attachments/assets/ca44b95e-2333-4887-adb2-e09dc36a50c6)

RUN THIS:
```bash
py -3.11 bots.py
```

You need to run this with python version 3.11!!!!
(I ran into a few issues trying to run it on a different machine that had a python version > 3.11!!)

WHEN SETUP GO ON YOUR DISCORD SERVER AND ENTER:
!spt track_name
example (THIS GOES INTO THE DISCORD SERVER WHERE YOU'VE SETUP YOUR BOT!!! NOT THE TERMINAL): 
```bash
!spt  https://open.spotify.com/track/1GoQ5EQ0ZNURRrJKdThflm
```

![image](https://github.com/user-attachments/assets/59fc5c55-599e-4bb8-b518-545aad86fb57)



WHEN CLICKING ON THE LINK, YOU GET SENT TO THE DOWNLOAD PAGE.



YOU MIGHT SEE SOME ERRORS IN THE TERMINAL, IGNORE THOSE IF THE BOT IS WORKING!



USE AT YOUR OWN RISK, trust me!
