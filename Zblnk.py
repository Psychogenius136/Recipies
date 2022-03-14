import sys

from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from sqlite3 import Error
import pyautogui
from PyQt5.QtCore import QObject, QThread, pyqtSignal


global SettingShow 
global GridShow 
SettingShow = 1
GridShow = 1




def create_connection(path):

    connection = None

    try:

        connection = sqlite3.connect(path)

        print("Connection to SQLite DB successful")

    except Error as e:

        print(f"The error '{e}' occurred")


    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.executescript(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")



def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")





        
connection = create_connection("inventory.sqlite")
Name = "Toxic"
write_data = 'insert into Color24  (Por1z1) values ("{}") ;'.format(Name)

execute_query(connection, write_data)   

def Truncate_tables():
    
        connection = create_connection("inventory.sqlite")
    
        truncate = """
           DELETE FROM Toxic;
           DELETE FROM Chaosweaver;
           DELETE FROM Frostweaver;
           DELETE FROM Permafrost;
           DELETE FROM Hasted;
           DELETE FROM Deadeye;
           DELETE FROM Bombardier;
           DELETE FROM Flameweaver;
           DELETE FROM Incendiary;
           DELETE FROM Arcane_Buffer;
           DELETE FROM Echoist;
           DELETE FROM Stormweaver;
           DELETE FROM Dynamo;
           DELETE FROM Bonebreaker;
           DELETE FROM Bloodletter;
           DELETE FROM Steelinfused;
           DELETE FROM Gargantuan;
           DELETE FROM Berserker;
           DELETE FROM Sentinel;
           DELETE FROM Juggernaut;
           DELETE FROM Vampiric;
           DELETE FROM Overcharged;
           DELETE FROM Soul_Conduit;
           DELETE FROM Opulent;
           DELETE FROM Malediction;
           DELETE FROM Consecrator;
           DELETE FROM Frenzied;
           DELETE FROM Heralding_Minions;
           DELETE FROM Empowering_Minions;
           DELETE FROM Assassin;
           DELETE FROM Trickster;
           DELETE FROM Necromancer;
           DELETE FROM Rejuvenating;
           DELETE FROM Executioner;
           DELETE FROM Hexer;
           DELETE FROM Drought_Bringer;
           DELETE FROM Entangler;
           DELETE FROM Temporal_Bubble;
           DELETE FROM Treant_Horde;
           DELETE FROM Frost_Strider;
           DELETE FROM Ice_Prison;
           DELETE FROM Soul_Eater;
           DELETE FROM Flame_Strider;
           DELETE FROM Corpse_Detonator;
           DELETE FROM Evocationist;
           DELETE FROM Magma_Barrier;
           DELETE FROM Mirror_Image;
           DELETE FROM Storm_Strider;
           DELETE FROM Mana_Siphoner;
           DELETE FROM Corrupter;
           DELETE FROM Invulnerable;
           DELETE FROM Crystalskinned;
           DELETE FROM Empowered_Elements;
           DELETE FROM Effigy;
           DELETE FROM Lunaristouched;
           DELETE FROM Solaristouched;
           DELETE FROM Arakaalitouched;
           DELETE FROM Brine_Kingtouched;
           DELETE FROM Tukohamatouched;
           DELETE FROM Abberathtouched;
           DELETE FROM Shakaritouched;
           DELETE FROM Innocencetouched;
           DELETE FROM Kitavatouched;
           DELETE FROM Empty;
           DELETE FROM Stash;
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("0" ,"0","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("0" ,"1","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("0" ,"2","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("0" ,"3","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("0" ,"4","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("0" ,"5","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("0" ,"6","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("0" ,"7","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("1" ,"0","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("1" ,"1","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("1" ,"2","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("1" ,"3","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("1" ,"4","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("1" ,"5","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("1" ,"6","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("1" ,"7","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("2" ,"0","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("2" ,"1","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("2" ,"2","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("2" ,"3","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("2" ,"4","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("2" ,"5","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("2" ,"6","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("2" ,"7","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("3" ,"0","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("3" ,"1","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("3" ,"2","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("3" ,"3","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("3" ,"4","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("3" ,"5","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("3" ,"6","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("3" ,"7","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("4" ,"0","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("4" ,"1","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("4" ,"2","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("4" ,"3","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("4" ,"4","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("4" ,"5","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("4" ,"6","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("4" ,"7","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("5" ,"0","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("5" ,"1","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("5" ,"2","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("5" ,"3","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("5" ,"4","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("5" ,"5","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("5" ,"6","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("5" ,"7","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("6" ,"0","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("6" ,"1","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("6" ,"2","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("6" ,"3","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("6" ,"4","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("6" ,"5","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("6" ,"6","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("6" ,"7","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("7" ,"0","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("7" ,"1","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("7" ,"2","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("7" ,"3","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("7" ,"4","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("7" ,"5","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("7" ,"6","None","Green",1);
           insert into Stash (Cordx,Cordy,Name,Color,Checked) values ("7" ,"7","None","Green",1);
           """
        
        execute_query(connection, truncate)





def Reload_stash():




    connection = create_connection("inventory.sqlite")

    Truncate_tables()

    select = 'Select Name,Img_Location from  inventory;'
    Mods_NameImg = execute_read_query(connection, select)
    stash = pyautogui.screenshot()
    stash.save("stash.png")


    for x in range(len(Mods_NameImg)):

        #Located = (list(pyautogui.locateAllOnScreen( Mods_NameImg[x][1], confidence=0.99,region=(155, 461, 584, 584) )))
        Located = list(pyautogui.locateAll(Mods_NameImg[x][1], stash, confidence=0.99,region=(155, 461, 584, 584)))

        for y in range(len(Located )):

            Cordx = int((Located[y][0]-155+36)/73)
            Cordy = int((Located[y][1]-461+36)/73)

            Insert = "Insert into  {} (Cordx,Cordy) values({},{}); ".format(Mods_NameImg[x][0],Cordx,Cordy)

            execute_query(connection, Insert)     
            Insert2 ='Update Stash set Name="{}" where Cordx={} and Cordy={} ; '.format(Mods_NameImg[x][0],Cordx,Cordy)

            execute_query(connection, Insert2)             

                                                                                   


class Worker(QObject):
    finished = pyqtSignal()
    

    def run(self):
        Reload_stash()
        self.finished.emit()

class DragButton():
    def updateconf(Name,OldColor,NewColor,PozOld,PozNew):
    
        if PozOld == 0 : 
            Pozname = "1z1"
        if PozOld == 1 : 
            Pozname = "1z2"   
        if PozOld == 2 : 
            Pozname = "2z2"
        if PozOld == 3 : 
            Pozname = "1z3"   
        if PozOld == 4 : 
            Pozname = "2z3"
        if PozOld == 5 : 
            Pozname = "3z3"   
        if PozOld == 6 : 
            Pozname = "1z4"
        if PozOld == 7 : 
            Pozname = "2z4"          
        if PozOld == 8 : 
            Pozname = "3z4"
        if PozOld == 9 : 
            Pozname = "4z4"  
            
            
        if PozNew == 0 : 
            Pozname2 = "1z1"
        if PozNew == 1 : 
            Pozname2 = "1z2"   
        if PozNew == 2 : 
            Pozname2 = "2z2"
        if PozNew == 3 : 
            Pozname2 = "1z3"   
        if PozNew == 4 : 
            Pozname2 = "2z3"
        if PozNew == 5 : 
            Pozname2 = "3z3"   
        if PozNew == 6 : 
            Pozname2 = "1z4"
        if PozNew == 7 : 
            Pozname2 = "2z4"          
        if PozNew == 8 : 
            Pozname2 = "3z4"
        if PozNew == 9 : 
            Pozname2 = "4z4"                    
    
        delete_data = 'delete from Color'+OldColor+' where Poz'+Pozname+' ="'+Name+'"; '
        
        
        
        write_data = 'insert into Color'+newColor+' (Poz'+Pozname2+')  values ("{}") ;'.format(Name)
        execute_query(connection, delete_data)
        execute_query(connection, write_data)          
        
    def Closethis(self): 
            #zapis do DB
            self.Uberbuton.setParent(None)  
    def setcolor(self, color): 
                print (color)
                if color == "0" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid black; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")         
                if color == "1" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(127, 127, 127, 1); "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}") 
                if color == "2" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(136, 0, 21, 1); "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")  
                if color == "3" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(255, 127,39, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")         
                if color == "4" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(255, 242, 0, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}") 
                if color == "5" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(34, 177, 76, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}") 
                if color == "6" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(0, 162, 232, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")         
                if color == "7" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(63, 72, 204, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}") 
                if color == "8" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(163, 73, 167, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")  
                if color == "9" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(0, 234, 234, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")         
                if color == "10" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(255, 128, 128, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}") 
                if color == "11" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(255, 255, 128, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}") 
                        
                if color == "12" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(128, 255, 128, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")         
                if color == "13" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(209, 200, 12, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}") 
                if color == "14" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(128, 128, 0, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")  
                if color == "15" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(237, 69, 241, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")         
                if color == "16" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(0, 128, 64, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}") 
                if color == "17" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(0, 0, 255, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")  
                if color == "18" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid rgba(0, 255, 0, 1);; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")     
                if color == "19" :
                        self.Uberbuton.setStyleSheet("#Framik" 
                        "{" 
                            "border: 3px solid white; "
                            "background-color : rgba(255, 255, 255, 1);"
                          "}")                                  
    def __init__(self, Name, Cordx, Cordy,color,poz,where):
            self.Name = Name
            self.Cordx = Cordx
            self.Cordy = Cordy
            self.where = where         
            self.Color = color
            self.Poz = poz
            
        
            read_data = 'select Reward,Bonus,Level,Img_Location,NiceName from inventory where Name="{}";'.format(self.Name)    
            status = execute_read_query(connection, read_data)
            Rewards =  status[0][0]        
            Bonus =  status[0][1]
            Level =  status[0][2]
            Img_location = status[0][3]
            NiceName = status[0][4]

                 
           
           
            #zapis do DB
            self.Uberbuton = QtWidgets.QFrame(self.where)
            self.Uberbuton.setGeometry(QtCore.QRect(self.Cordx, self.Cordy, 300,100))
            self.Uberbuton.setObjectName("Framik")
            self.Uberbuton.setStyleSheet("#Framik" 
            "{" 
                "border: 3px solid White; "
                "background-color : rgba(255, 255, 255, .9);"
              "}")
            self.Uberbuton.setAcceptDrops(True)
            self.Uberbuton.show()

            self.button = QtWidgets.QPushButton(self.Uberbuton)
            self.button.setGeometry(QtCore.QRect(290, 0, 10,10))
            self.button.setText('X')
            self.button.clicked.connect( self.Closethis )
            self.button.show()                  

            self.setcolor(str(self.Color))
            
            MainImage = QtWidgets.QLabel(self.Uberbuton)
            MainImage.setScaledContents(True)
            MainImage.setGeometry(0,0, 55,55)
            
            
            MainImageIcon = QtGui.QPixmap("icon/"+Img_location)
            MainImage.setPixmap(MainImageIcon)
            MainImage.show()                         
            

            self.movebuttonUP = QtWidgets.QPushButton(self.Uberbuton)
            self.movebuttonUP.setGeometry(QtCore.QRect(263, 15,15,20))
            iconUP = QtGui.QIcon()
            iconUP.addPixmap(QtGui.QPixmap('icon/Up.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.movebuttonUP.setIconSize(QtCore.QSize(15,20))
            self.movebuttonUP.setIcon(iconUP)            
            self.movebuttonUP.clicked.connect(lambda: self.moveMe(1))
            self.movebuttonUP.setStyleSheet("QPushButton" 
                                                "{" 
                                                   
                                                    "background-color : Transparent;"
                                                  "}")            
            self.movebuttonUP.show() 
            
            self.movebuttonDown = QtWidgets.QPushButton(self.Uberbuton)
            self.movebuttonDown.setGeometry(QtCore.QRect(263,50,15,20))
            iconDown = QtGui.QIcon()
            iconDown.addPixmap(QtGui.QPixmap('icon/Down.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.movebuttonDown.setIconSize(QtCore.QSize(15,20))
            self.movebuttonDown.setIcon(iconDown)          
            self.movebuttonDown.clicked.connect(lambda: self.moveMe(2))
            self.movebuttonDown.setStyleSheet("QPushButton" 
                                                "{" 
                                                   
                                                    "background-color : Transparent;"
                                                  "}")                 
            self.movebuttonDown.show() 
            
            self.movebuttonLeft = QtWidgets.QPushButton(self.Uberbuton)
            self.movebuttonLeft.setGeometry(QtCore.QRect(243, 35, 20,15))
            iconLeft = QtGui.QIcon()
            iconLeft.addPixmap(QtGui.QPixmap('icon/Left.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.movebuttonLeft.setIconSize(QtCore.QSize(20,15))
            self.movebuttonLeft.setIcon(iconLeft)          
            self.movebuttonLeft.clicked.connect(lambda: self.moveMe(3))
            self.movebuttonLeft.setStyleSheet("QPushButton" 
                                                "{" 
                                                   
                                                    "background-color : Transparent;"
                                                  "}")                 
            self.movebuttonLeft.show() 
            
            self.movebuttonRight = QtWidgets.QPushButton(self.Uberbuton)
            self.movebuttonRight.setGeometry(QtCore.QRect(278,35, 20,15))
            iconRight = QtGui.QIcon()
            iconRight.addPixmap(QtGui.QPixmap('icon/Right.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.movebuttonRight.setIcon(iconRight) 
            self.movebuttonRight.setIconSize(QtCore.QSize(20,15))
            self.movebuttonRight.clicked.connect(lambda: self.moveMe(4))
            self.movebuttonRight.setStyleSheet("QPushButton" 
                                                "{" 
                                                   
                                                    "background-color : Transparent;"
                                                  "}")                 
            self.movebuttonRight.show()             
            
            self.label = QtWidgets.QLabel(self.Uberbuton)
            self.label.setText(NiceName)
            self.label.setStyleSheet("QLabel{font-size: 15pt;}")
            self.label.move(60,5)
            self.label.show() 
            
            
            self.Bonuslabel = QtWidgets.QLabel(self.Uberbuton)
            self.Bonuslabel.setGeometry(QtCore.QRect(60,35, 180,50))
            self.Bonuslabel.setText(Bonus)
            self.Bonuslabel.setStyleSheet("QLabel{font-size: 10pt;}")
            self.Bonuslabel.setWordWrap(True)
            self.Bonuslabel.show()             
            
            
            
            Rewards_list  = Rewards.split(",")
            print(Rewards_list)
            if len(Rewards_list) == 1:
                        rewards1 = QtWidgets.QLabel(self.Uberbuton)
                        rewards1.setScaledContents(True)
                        rewards1.setGeometry(7,55, 20,22)
                        
                        rewards1.setText(self.Name)
                        iconrewards1 = QtGui.QPixmap("rewards/"+Rewards_list[0]+".png")
                        rewards1.setPixmap(iconrewards1)
                        rewards1.show()             
            if len(Rewards_list) == 2:
                        rewards1 = QtWidgets.QLabel(self.Uberbuton)
                        rewards1.setScaledContents(True)
                        rewards1.setGeometry(7,55, 20,22)
                        
                        rewards1.setText(self.Name)
                        iconrewards1 = QtGui.QPixmap("rewards/"+Rewards_list[0]+".png")
                        rewards1.setPixmap(iconrewards1)
                        rewards1.show()                             
                
                        rewards2 = QtWidgets.QLabel(self.Uberbuton)
                        rewards2.setScaledContents(True)
                        rewards2.setGeometry(27,55, 20,22)
                
                        rewards2.setText(self.Name)
                        iconrewards2 = QtGui.QPixmap("rewards/"+Rewards_list[1]+".png")
                        rewards2.setPixmap(iconrewards2)
                        rewards2.show()                     
            if len(Rewards_list) == 3:
                        rewards1 = QtWidgets.QLabel(self.Uberbuton)
                        rewards1.setScaledContents(True)
                        rewards1.setGeometry(7,55, 20,22)
                
                        rewards1.setText(self.Name)
                        iconrewards1 = QtGui.QPixmap("rewards/"+Rewards_list[0]+".png")
                        rewards1.setPixmap(iconrewards1)
                        rewards1.show()                             
                
                        rewards2 = QtWidgets.QLabel(self.Uberbuton)
                        rewards2.setScaledContents(True)
                        rewards2.setGeometry(27,55, 20,22)
                
                        rewards2.setText(self.Name)
                        iconrewards2 = QtGui.QPixmap("rewards/"+Rewards_list[1]+".png")
                        rewards2.setPixmap(iconrewards2)
                        rewards2.show()                                 
            
                        rewards3 = QtWidgets.QLabel(self.Uberbuton)
                        rewards3.setScaledContents(True)
                        rewards3.setGeometry(7,75, 20,22)
                    
                        rewards3.setText(self.Name)
                        iconrewards3 = QtGui.QPixmap("rewards/"+Rewards_list[2]+".png")
                        rewards3.setPixmap(iconrewards3)
                        rewards3.show()   
            if len(Rewards_list) == 4:
                        rewards1 = QtWidgets.QLabel(self.Uberbuton)
                        rewards1.setScaledContents(True)
                        rewards1.setGeometry(7,55, 20,22)
                
                        rewards1.setText(self.Name)
                        iconrewards1 = QtGui.QPixmap("rewards/"+Rewards_list[0]+".png")
                        rewards1.setPixmap(iconrewards1)
                        rewards1.show()                             
                
                        rewards2 = QtWidgets.QLabel(self.Uberbuton)
                        rewards2.setScaledContents(True)
                        rewards2.setGeometry(27,55, 20,22)
                
                        rewards2.setText(self.Name)
                        iconrewards2 = QtGui.QPixmap("rewards/"+Rewards_list[1]+".png")
                        rewards2.setPixmap(iconrewards2)
                        rewards2.show()                                 
                
                        rewards3 = QtWidgets.QLabel(self.Uberbuton)
                        rewards3.setScaledContents(True)
                        rewards3.setGeometry(7,75, 20,22)
                
                        rewards3.setText(self.Name)
                        iconrewards3 = QtGui.QPixmap("rewards/"+Rewards_list[2]+".png")
                        rewards3.setPixmap(iconrewards3)
                        rewards3.show()                                            
                                
                        rewards4 = QtWidgets.QLabel(self.Uberbuton)
                        rewards4.setScaledContents(True)
                        rewards4.setGeometry(27,75, 20,22)
                    
                        rewards4.setText(self.Name)
                        iconrewards4 = QtGui.QPixmap("rewards/"+Rewards_list[3]+".png")
                        rewards4.setPixmap(iconrewards4)
                        rewards4.show()                             
                        
            
            
            self.comboBox2 = QtWidgets.QComboBox(self.Uberbuton)
            self.comboBox2.setGeometry(QtCore.QRect(300-104, 100-25, 40, 20))
            self.comboBox2.setObjectName("packsize")
            self.comboBox2.setIconSize(QtCore.QSize(50, 10))
            
            self.comboBox2.addItem("1")
            self.comboBox2.setItemText(0,"1/1")     
            self.comboBox2.addItem("2")
            self.comboBox2.setItemText(1,"1/2")
            self.comboBox2.addItem("3")
            self.comboBox2.setItemText(2,"2/2")         
            
            self.comboBox2.addItem("4")
            self.comboBox2.setItemText(3,"1/3")    
            
            self.comboBox2.addItem("5")
            self.comboBox2.setItemText(4,"2/3")    
            
            self.comboBox2.addItem("6")
            self.comboBox2.setItemText(5,"3/3")                
            
            self.comboBox2.addItem("7")
            self.comboBox2.setItemText(6,"1/4")
            self.comboBox2.addItem("8")
            self.comboBox2.setItemText(7,"2/4")
            self.comboBox2.addItem("9")
            self.comboBox2.setItemText(8,"3/4")
            self.comboBox2.addItem("10")
            self.comboBox2.setItemText(9,"4/4")            
            self.comboBox2.setCurrentIndex(self.Poz)
            self.comboBox2.show()
            
            self.comboBox = QtWidgets.QComboBox(self.Uberbuton)
            self.comboBox.setGeometry(QtCore.QRect(300-64, 100-25, 60, 20))
            self.comboBox.setObjectName("ColorcomboBox")
       
            
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("Colors/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon1, "1")
            self.comboBox.setItemText(0,"1")
        
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("Colors/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon2, "2")
            self.comboBox.setItemText(1,"2")	
        
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("Colors/3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon3, "3")
            self.comboBox.setItemText(2,"3")
        
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap("Colors/4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon4, "4")
            self.comboBox.setItemText(3,"4")
        
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap("Colors/5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon5, "5")
            self.comboBox.setItemText(4,"5")
        
            icon6 = QtGui.QIcon()
            icon6.addPixmap(QtGui.QPixmap("Colors/6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon6, "6")
            self.comboBox.setItemText(5,"6")
        
            icon7 = QtGui.QIcon()
            icon7.addPixmap(QtGui.QPixmap("Colors/7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon7, "7")
            self.comboBox.setItemText(6,"7")
        
            icon8 = QtGui.QIcon()
            icon8.addPixmap(QtGui.QPixmap("Colors/8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon8, "8")
            self.comboBox.setItemText(7,"8")
        
            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("Colors/9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon9, "9")
            self.comboBox.setItemText(8,"9")
        
            icon10 = QtGui.QIcon()
            icon10.addPixmap(QtGui.QPixmap("Colors/10.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon10, "10")
            self.comboBox.setItemText(9,"10")
        
            icon11 = QtGui.QIcon()
            icon11.addPixmap(QtGui.QPixmap("Colors/11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon11, "11")
            self.comboBox.setItemText(10,"11")
        
            icon12 = QtGui.QIcon()
            icon12.addPixmap(QtGui.QPixmap("Colors/12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon12, "12")
            self.comboBox.setItemText(11,"12")
        
            icon13 = QtGui.QIcon()
            icon13.addPixmap(QtGui.QPixmap("Colors/13.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon13, "13")
            self.comboBox.setItemText(12,"13")
        
            icon14 = QtGui.QIcon()
            icon14.addPixmap(QtGui.QPixmap("Colors/14.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon14, "14")
            self.comboBox.setItemText(13,"14")
        
            icon15 = QtGui.QIcon()
            icon15.addPixmap(QtGui.QPixmap("Colors/15.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon15, "15")
            self.comboBox.setItemText(14,"15")
        
            icon16 = QtGui.QIcon()
            icon16.addPixmap(QtGui.QPixmap("Colors/16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon16, "16")
            self.comboBox.setItemText(15,"16")
        
            icon17 = QtGui.QIcon()
            icon17.addPixmap(QtGui.QPixmap("Colors/17.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon17, "17")
            self.comboBox.setItemText(16,"17")
        
            icon18 = QtGui.QIcon()
            icon18.addPixmap(QtGui.QPixmap("Colors/18.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon18, "18")
            self.comboBox.setItemText(17,"18")
        
            icon19 = QtGui.QIcon()
            icon19.addPixmap(QtGui.QPixmap("Colors/19.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon19, "19")
            self.comboBox.setItemText(18,"19")
        
            icon20 = QtGui.QIcon()
            icon20.addPixmap(QtGui.QPixmap("Colors/20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.comboBox.addItem(icon20, "20")
            self.comboBox.setItemText(19,"20")  
            self.comboBox.setCurrentIndex(self.Color)
            
            self.comboBox.show()
         
            self.comboBox.currentIndexChanged.connect(lambda: self.setcolor(str(self.comboBox.currentIndex())))
            
    def moveMe(self , direction):
        if direction == 1 :
    
            self.Uberbuton.move(self.Uberbuton.x(),self.Uberbuton.y()-110)   
            #zapis do DB
        if direction == 2 :
    
            self.Uberbuton.move(self.Uberbuton.x(),self.Uberbuton.y()+110)  
            #zapis do DB
        if direction == 3 :
    
            self.Uberbuton.move(self.Uberbuton.x()-310,self.Uberbuton.y())
            #zapis do DB
            

        if direction == 4 :

            self.Uberbuton.move(self.Uberbuton.x()+310,self.Uberbuton.y())
            #zapis do DB
   
                
             
class Ui_MainWindow(object):
      def runLongTask(self):
            # Step 2: Create a QThread object
            self.thread = QThread()
            # Step 3: Create a worker object
            self.worker = Worker()
            # Step 4: Move worker to the thread
            self.worker.moveToThread(self.thread)
            # Step 5: Connect signals and slots
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)

            # Step 6: Start the thread
            self.thread.start()
        
            
            self.thread.finished.connect(
                    lambda: print("refresheed")
                )      
            
      def createuberbuton(self, Name, Cordx, Cordy,color,poz,where):
            
            
            self.Name = Name
            self.Cordx = Cordx
            self.Cordy = Cordy
            self.where = where 
            self.color = color
            self.poz = poz
            
            
            
            
            self.newUberButton = DragButton(self.Name,self.Cordx,self.Cordy,color,poz,self.where)
            
      def draw_something(self):
                painter = QtGui.QPainter(self.Painter.pixmap())
                pen = QtGui.QPen()
                pen.setWidth(80)
                pen.setColor(QtGui.QColor('white'))
                painter.setOpacity(0.6)
                painter.setPen(pen)
                painter.drawPoint(40, 40)
                painter.end()    
                           
      def draw_somethingelse(self):
                print (self.Grid_Painter.pixmap())
                painterelse = QtGui.QPainter(self.Grid_Painter.pixmap())
                penelse = QtGui.QPen()
                penelse.setWidth(4)
                penelse.setColor(QtGui.QColor('red'))
                #painterelse.setOpacity(0.3)
                painterelse.setPen(penelse)
                
                painterelse.drawRect(2, 2, 73, 73)

                
                
                painterelse.end()                
                
      def ShowHideSettings(self): 
        
        global SettingShow
        if SettingShow == 1:
            SettingShow = 0
            self.tabWidget.hide()
        else:      
            SettingShow = 1
            self.tabWidget.show() 
      def ShowHideGrid(self): 
        
        global GridShow
        if GridShow == 1:
            GridShow = 0
            self.Grid_Base.hide()

            
        else:      
            GridShow = 1
            self.Grid_Base.show()  

            
            
      def ShowHideAll(self): 
        global SettingShow
        global GridShow
        if GridShow == 1 & SettingShow == 1 :
            GridShow = 0
            SettingShow = 0
            self.Grid_Base.hide()
            self.tabWidget.hide()
          
        else:      
            GridShow = 1
            SettingShow = 1
            self.Grid_Base.show()
            self.tabWidget.show()                
      def ShowNew(self):
            insert = """
                        select Cordx,Cordy from Stash where Name="None";          
                        """                
            ddd = execute_read_query(connection, insert)  
            print (ddd)                      
      
    
      def setupUi(self, MainWindow):
            MainWindow.setObjectName("Setting")
            MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)
            MainWindow.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
            MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
            MainWindow.move(0,0)
            MainWindow.resize(2560,1440)
            self.runLongTask()
            
            

            
            
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            
        
            
        
        
        
            
            
         
        
    

    
            
    
          
            
         
            
             #-----MENU-----
        
            
            self.Painter = QtWidgets.QLabel(self.centralwidget)
            self.Painter.canvas = QtGui.QPixmap(2560, 1440)
            self.Painter.setPixmap(self.Painter.canvas)
    
            
            self.draw_something() 
    
    
            
            
            self.MinMaxButton = QtWidgets.QPushButton(self.centralwidget)
            self.MinMaxButton.setGeometry(QtCore.QRect(5, 2, 50, 70))
            self.MinMaxButton.setObjectName("MinMaxButton")  
            self.MinMaxButton.icon = QtGui.QIcon()
            self.MinMaxButton.icon.addPixmap(QtGui.QPixmap('Iconcroped.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.MinMaxButton.setIcon(self.MinMaxButton.icon)
            self.MinMaxButton.setIconSize(QtCore.QSize(50, 70))    
            self.MinMaxButton.clicked.connect(self.ShowHideAll)             
            self.MinMaxButton.setStyleSheet("QPushButton"
                                             "{"
                                             "background-color : Transparent;"
                                             "}"  ) 
            
            
            
            self.SettingButton = QtWidgets.QPushButton(self.centralwidget)
            self.SettingButton.setGeometry(QtCore.QRect(4, 58, 20, 20))
            self.SettingButton.setObjectName("SettingButton")  
            self.SettingButton.icon = QtGui.QIcon()
            self.SettingButton.icon.addPixmap(QtGui.QPixmap('Setting.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.SettingButton.setIcon(self.SettingButton.icon)
            self.SettingButton.setIconSize(QtCore.QSize(20, 20))    
            self.SettingButton.clicked.connect(self.ShowHideSettings)             
            self.SettingButton.setStyleSheet("QPushButton"
                                             "{"
                                             "background-color : Transparent;"
                                             "}"  )         
            self.OverlayButton = QtWidgets.QPushButton(self.centralwidget)
            self.OverlayButton.setGeometry(QtCore.QRect(34, 58, 20, 20))
            self.OverlayButton.setObjectName("OverlayButton")  
            self.OverlayButton.icon = QtGui.QIcon()
            self.OverlayButton.icon.addPixmap(QtGui.QPixmap('Overlay.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.OverlayButton.setIcon(self.OverlayButton.icon)
            self.OverlayButton.setIconSize(QtCore.QSize(20, 20))    
            self.OverlayButton.clicked.connect(self.ShowHideGrid)             
            self.OverlayButton.setStyleSheet("QPushButton"
                                             "{"
                                             "background-color : Transparent;"
                                             "}"  )             
            self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
            self.CloseButton.setGeometry(QtCore.QRect(60, 5, 20, 20))
            self.CloseButton.setObjectName("CloseButton")  
            self.CloseButton.icon = QtGui.QIcon()
            self.CloseButton.icon.addPixmap(QtGui.QPixmap('Close.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.CloseButton.setIcon(self.CloseButton.icon)
            self.CloseButton.setIconSize(QtCore.QSize(20, 20))    
            self.CloseButton.clicked.connect(app.quit)             
            self.CloseButton.setStyleSheet("QPushButton"
                                             "{"
                                             "background-color : Transparent;"
                                             "}"  )                     
            
    
    
    
                      
            
            
            #_____RECEPT_AND SETTINGS__________
            
            self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
            self.tabWidget.setGeometry(QtCore.QRect(900, 20, 1600,1400))
            self.tabWidget.setObjectName("tabWidget")

            
            
            self.Recipes = QtWidgets.QWidget()

      
            self.tabWidget.addTab(self.Recipes, "")
            self.Recipes.setObjectName("Recipes")
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.Recipes), "Recipes")
            stylesheet = """ 
                        QTabWidget::pane{border-color:red;background-color: rgba(255, 50, 50, .8);} 
    
                """        
            self.tabWidget.setStyleSheet(stylesheet)      
            
            self.Settings = QtWidgets.QWidget()
            self.tabWidget.addTab(self.Settings, "")    
            self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
            self.Settings.setObjectName("Settings")    
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), "Settings")
            self.tabWidget.font = QtGui.QFont('Arial', 15)
            
            self.tabWidget.setFont(self.tabWidget.font)    
            
            #_____Setting Page _________
        
            # self.Settings.
            
            
            
            FindNewButton = QPushButton("Find New",self.Settings)
            FindNewButton.clicked.connect(self.ShowNew)    
            FindNewButton.setGeometry(QtCore.QRect(100,400, 80, 30))
            
            
            FindNewButton.show()
            
            
            
            
            
            
            
            
    
            #__________________GRID________
            
            self.Grid_Base = QtWidgets.QFrame(self.centralwidget)
            self.Grid_Base.setGeometry(QtCore.QRect(155, 461, 584, 584))
            self.Grid_Base.setObjectName("Grid")    
            self.Grid_Base.setStyleSheet("QFrame" 
                                         "{" 
                                         #"background-color : rgba(222, 184, 135, .6);"
                                         "background-color : Transparent;"
                                           "}"
            )
                 
                 
            self.Grid_Painter = QtWidgets.QLabel(self.Grid_Base)
            self.Grid_Painter.canvas = QtGui.QPixmap(584, 584)
            self.Grid_Painter.setPixmap(self.Grid_Painter.canvas)
            
        
            
            self.draw_somethingelse()                                       
            
            
            
            
            self.ModcomboBox = QtWidgets.QComboBox(self.Recipes)
            self.ModcomboBox.setGeometry(QtCore.QRect(20, 20, 130, 20))
            self.ModcomboBox.setObjectName("ModcomboBox")
            self.ModcomboBox.addItem("0")
            self.ModcomboBox.addItem("1")
            self.ModcomboBox.addItem("2")
            self.ModcomboBox.addItem("3")
            self.ModcomboBox.addItem("4")
            self.ModcomboBox.addItem("5")
            self.ModcomboBox.addItem("6")
            self.ModcomboBox.addItem("7")
            self.ModcomboBox.addItem("8")
            self.ModcomboBox.addItem("9")
            self.ModcomboBox.addItem("10")
            self.ModcomboBox.addItem("11")
            self.ModcomboBox.addItem("12")
            self.ModcomboBox.addItem("13")
            self.ModcomboBox.addItem("14")
            self.ModcomboBox.addItem("15")
            self.ModcomboBox.addItem("16")
            self.ModcomboBox.addItem("17")
            self.ModcomboBox.addItem("18")
            self.ModcomboBox.addItem("19")
            self.ModcomboBox.addItem("20")
            self.ModcomboBox.addItem("21")
            self.ModcomboBox.addItem("22")
            self.ModcomboBox.addItem("23")
            self.ModcomboBox.addItem("24")
            self.ModcomboBox.addItem("25")
            self.ModcomboBox.addItem("26")
            self.ModcomboBox.addItem("27")
            self.ModcomboBox.addItem("28")
            self.ModcomboBox.addItem("29")
            self.ModcomboBox.addItem("30")
            self.ModcomboBox.addItem("31")
            self.ModcomboBox.addItem("32")
            self.ModcomboBox.addItem("33")
            self.ModcomboBox.addItem("34")
            self.ModcomboBox.addItem("35")
            self.ModcomboBox.addItem("36")
            self.ModcomboBox.addItem("37")
            self.ModcomboBox.addItem("38")
            self.ModcomboBox.addItem("39")
            self.ModcomboBox.addItem("40")
            self.ModcomboBox.addItem("41")
            self.ModcomboBox.addItem("42")
            self.ModcomboBox.addItem("43")
            self.ModcomboBox.addItem("44")
            self.ModcomboBox.addItem("45")
            self.ModcomboBox.addItem("46")
            self.ModcomboBox.addItem("47")
            self.ModcomboBox.addItem("48")
            self.ModcomboBox.addItem("49")
            self.ModcomboBox.addItem("50")
            self.ModcomboBox.addItem("51")
            self.ModcomboBox.addItem("52")
            self.ModcomboBox.addItem("53")
            self.ModcomboBox.addItem("54")
            self.ModcomboBox.addItem("55")
            self.ModcomboBox.addItem("56")
            self.ModcomboBox.addItem("57")
            self.ModcomboBox.addItem("58")
            self.ModcomboBox.addItem("59")
            self.ModcomboBox.addItem("60")
            self.ModcomboBox.addItem("61")
            self.ModcomboBox.addItem("62")             
            self.ModcomboBox.setItemText(0,"Toxic")
            self.ModcomboBox.setItemText(1,"Kitavatouched")
            self.ModcomboBox.setItemText(2,"Chaosweaver")
            self.ModcomboBox.setItemText(3,"Frostweaver")
            self.ModcomboBox.setItemText(4,"Permafrost")
            self.ModcomboBox.setItemText(5,"Hasted")
            self.ModcomboBox.setItemText(6,"Deadeye")
            self.ModcomboBox.setItemText(7,"Bombardier")
            self.ModcomboBox.setItemText(8,"Flameweaver")
            self.ModcomboBox.setItemText(9,"Incendiary")
            self.ModcomboBox.setItemText(10,"Arcane_Buffer")
            self.ModcomboBox.setItemText(11,"Echoist")
            self.ModcomboBox.setItemText(12,"Stormweaver")
            self.ModcomboBox.setItemText(13,"Dynamo")
            self.ModcomboBox.setItemText(14,"Bonebreaker")
            self.ModcomboBox.setItemText(15,"Bloodletter")
            self.ModcomboBox.setItemText(16,"Steelinfused")
            self.ModcomboBox.setItemText(17,"Gargantuan")
            self.ModcomboBox.setItemText(18,"Berserker")
            self.ModcomboBox.setItemText(19,"Sentinel")
            self.ModcomboBox.setItemText(20,"Juggernaut")
            self.ModcomboBox.setItemText(21,"Vampiric")
            self.ModcomboBox.setItemText(22,"Overcharged")
            self.ModcomboBox.setItemText(23,"Soul_Conduit")
            self.ModcomboBox.setItemText(24,"Opulent")
            self.ModcomboBox.setItemText(25,"Malediction")
            self.ModcomboBox.setItemText(26,"Consecrator")
            self.ModcomboBox.setItemText(27,"Frenzied")
            self.ModcomboBox.setItemText(28,"Heralding_Minions")
            self.ModcomboBox.setItemText(29,"Empowering_Minions")
            self.ModcomboBox.setItemText(30,"Assassin")
            self.ModcomboBox.setItemText(31,"Trickster")
            self.ModcomboBox.setItemText(32,"Necromancer")
            self.ModcomboBox.setItemText(33,"Rejuvenating")
            self.ModcomboBox.setItemText(34,"Executioner")
            self.ModcomboBox.setItemText(35,"Hexer")
            self.ModcomboBox.setItemText(36,"Drought_Bringer")
            self.ModcomboBox.setItemText(37,"Entangler")
            self.ModcomboBox.setItemText(38,"Temporal_Bubble")
            self.ModcomboBox.setItemText(39,"Treant_Horde")
            self.ModcomboBox.setItemText(40,"Frost_Strider")
            self.ModcomboBox.setItemText(41,"Ice_Prison")
            self.ModcomboBox.setItemText(42,"Soul_Eater")
            self.ModcomboBox.setItemText(43,"Flame_Strider")
            self.ModcomboBox.setItemText(44,"Corpse_Detonator")
            self.ModcomboBox.setItemText(45,"Evocationist")
            self.ModcomboBox.setItemText(46,"Magma_Barrier")
            self.ModcomboBox.setItemText(47,"Mirror_Image")
            self.ModcomboBox.setItemText(48,"Storm_Strider")
            self.ModcomboBox.setItemText(49,"Mana_Siphoner")
            self.ModcomboBox.setItemText(50,"Corrupter")
            self.ModcomboBox.setItemText(51,"Invulnerable")
            self.ModcomboBox.setItemText(52,"Crystalskinned")
            self.ModcomboBox.setItemText(53,"Empowered_Elements")
            self.ModcomboBox.setItemText(54,"Effigy")
            self.ModcomboBox.setItemText(55,"Lunaristouched")
            self.ModcomboBox.setItemText(56,"Solaristouched")
            self.ModcomboBox.setItemText(57,"Arakaalitouched")
            self.ModcomboBox.setItemText(58,"Brine_Kingtouched")
            self.ModcomboBox.setItemText(59,"Tukohamatouched")
            self.ModcomboBox.setItemText(60,"Abberathtouched")
            self.ModcomboBox.setItemText(61,"Shakaritouched")
            self.ModcomboBox.setItemText(62,"Innocencetouched")
            
            
            self.AddButton = QtWidgets.QPushButton(self.Recipes)
            self.AddButton.setGeometry(QtCore.QRect(160, 20, 30, 20))
            self.AddButton.setObjectName("AddButton")  
            self.AddButton.setText("Add")
            
            
            self.AddButton.clicked.connect(lambda: ui.createuberbuton(self.ModcomboBox.currentText(), 20, 60,19,0,self.Recipes))             
                      
    
    
            
            
            
            
      
            
            
            MainWindow.setCentralWidget(self.centralwidget)         
 
        
        
        



if __name__ == "__main__":
      import sys
      app = QtWidgets.QApplication(sys.argv)
      
      
      MainWindow = QtWidgets.QMainWindow()
      ui = Ui_MainWindow()
      ui.setupUi(MainWindow)
      MainWindow.show()
      
      
      
      sys.exit(app.exec_())