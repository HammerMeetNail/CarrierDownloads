import os
import time
import shutil
import pyautogui

## Add directory location
amsDir = ''
arbellaDir = ''
safetyDir = ''
progressiveDir = ''
premierDir = ''
premierLocal = ''
commerceDir = ''

directories = [amsDir, arbellaDir, safetyDir, progressiveDir, premierDir, commerceDir]

## Left Click icon once
def leftClick(image):
    try:
        if type(image) == tuple:
            location = image
        else:
            location = pyautogui.locateOnScreen(image, grayscale=True)
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
    except TypeError:
        print 'click error' + ' ' + image
        return leftClick(image)

## Left click icon twice
def leftClickTwice(image):
    try:
        if type(image) == tuple:
            location = image
        else:
            location = pyautogui.locateOnScreen(image, grayscale=True)
        x, y = pyautogui.center(location)
        pyautogui.doubleClick(x, y)
    except TypeError:
        print 'double click error' + ' ' + image
        return leftClickTwice(image)

## Locates newly downloaded files
def copyNewFiles(directory):
    today = time.time()
    twelveHoursAgo = today - 60*60*12
    files = os.listdir(directory)
    files.reverse()
    for file in files:
        fileDate = os.path.getctime(directory + file)
        if fileDate > twelveHoursAgo and len(file) > 5:
            srcDir = directory + file
            dstDir = amsDir + file
            shutil.copyfile(srcDir, dstDir)
            if directory == premierDir:
                try:
                    localDir = premierLocal + file
                    shutil.copyfile(srcDir, localDir)
                except TypeError:
                    pass
            print 'Copied {0}'.format(file)
        else:
            break

## Upload files to AMS
def upload(directoriesList):
    for directory in directoriesList:
        print directory
        copyNewFiles(directory)
    leftClick('amsSSO.png')
    leftClick('amsToolbox.png')
    leftClick('amsIntegration.png')
    leftClick('amsDownload.png')
    leftClick('amsMoveDownload.png')
    leftClick('amsBrowse.png')
    pyautogui.typewrite(directory, interval=0.25)
    pyautogui.press('enter')
    files = os.listdir(amsDir)
    output = ''
    for file in files:
        output += '"' + file + '"' + ' '
    pyautogui.typewrite(output, interval=0.25)
    pyautogui.press('enter')

## Open IE11 from Desktop and sign into LastPass
leftClickTwice('ie.png')
leftClick('lastpassIE11off.png')
pyautogui.typewrite('password', interval=0.25)
pyautogui.press('enter')

## Download from CGI
leftClick('morningDownload1.png')
leftClick('md1AL3Request.png')
leftClickTwice('md1FileName.png')
if pyautogui.locateOnScreen('md1NotAvailable.png', grayscale=True) != None:
    print 'No CGI today'
    pyautogui.hotkey('ctrl', 'w')
else:
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    priorNum = os.listdir('C:\Premier')[-1]
    newNum = int(priorNum[10:]) + 1
    newFile = ':\Premier\direct.isi' + str(newNum)
    pyautogui.typewrite(newFile, interval=0.25)
    pyautogui.press('tab')
    pyautogui.press('enter')
    leftClick('md1Complete.png')
    pyautogui.press('enter')
    leftClick('md1MainMenu.png')
    leftClick('md1CGI.png')
    pyautogui.hotkey('ctrl', 'w')

## Download from Commerce
leftClick('morningDownload2.png')
leftClick('md2AL3Request.png')
leftClick('md2DownloadPage.png')
if pyautogui.locateOnScreen('md2DownloadFound.png', grayscale=True) != None:
    leftClick('md2DownloadFound.png')
    leftClick('md2DownloadCIC.png')
    leftClick('md2Open.png')
    leftClick('md2OK.png')
    leftClick('md2DownloadComplete.png')
else:
    print 'No Commerce today'
    pyautogui.hotkey('alt', 'f4')

## Upload to AMS
upload(directories)


