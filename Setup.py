import pyautogui
import sqlite3



def TakePhotoN1Cord(Name):

                
                one = pyautogui.screenshot(region=( 165,473 ,50, 40))
                one.save('img/'+Name+'.png')
                
                
                
TakePhotoN1Cord("Bloodletter")