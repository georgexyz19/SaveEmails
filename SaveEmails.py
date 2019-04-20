# save_emails.py by Geroge Zhang on 2/1/2019
# The GMail window should be in a status shown in SaveEMails.png
# The EMails should be in a folder(label), the program clicks next button
# This program only works on my laptop
# Use Al Sweigart's pyautogui package, read last chapter of 
#   Automate The Boring Stuff With Python. 

# Chrome settings -> Advanced -> Privacy and security -> Content settings ->
# pop-ups and redirects -> allow => add https://mail.google.com

# setup the program
import pyautogui # this requires installation
import time

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

TOTALEMAILS = 10
START = 1

nextButton = (1229, 189)
printButton = (1230, 247)
saveButton = (202, 167)
filenameBox = (878, 443)
saveDialog = (788, 503)

closeButton = (470, 15)
centerWindow = (683, 7)

print('>>> 5 Seconds to start <<<')
time.sleep(5)

##print('Click window center to activate Gmail')
##pyautogui.click(centerWindow[0], centerWindow[1])

print('Please click the first email in a label group')
print('>>> 5 Seconds to start <<<')
time.sleep(5)

for i in range(START, TOTALEMAILS + START):
    print('\nNow click the print button')
    pyautogui.click(printButton[0], printButton[1])
    time.sleep(5)

    print('Click the Save email button')
    pyautogui.click(saveButton[0], saveButton[1])
    time.sleep(1)

    print('Click filename field')
    pyautogui.click(filenameBox[0], filenameBox[1])
    time.sleep(.5)

    pyautogui.press('home')
    filename_prefix = '{0:03}'.format(i) + ' - '
    pyautogui.typewrite(filename_prefix)
    time.sleep(.5) 

    print('Click the Save file button')
    pyautogui.click(saveDialog[0], saveDialog[1])
    time.sleep(.5)

    print('Close the second window')
    pyautogui.click(closeButton[0], closeButton[1])
    time.sleep(.5)

    print('Click next button')
    pyautogui.click(nextButton[0], nextButton[1])
    time.sleep(.5)

print(' >>> Done <<< ')