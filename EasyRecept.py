import pyautogui
import sqlite3
from sqlite3 import Error





def create_connection(path):

       connection = None

       try:

              connection = sqlite3.connect(path)

              #print("Connection to SQLite DB successful")

       except Error as e:

              print(f"The error '{e}' occurred")


       return connection

def execute_query(connection, query):
       cursor = connection.cursor()
       try:
              cursor.executescript(query)
              connection.commit()
              #print("Query executed successfully")
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








def Truncate_tables():
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
       connection = create_connection("inventory.sqlite")
       execute_query(connection, truncate)




#---------------EXAMPLES----------------#
#update = 'update inventory set Inventory_Slot="27,28" where Name="Toxic" ; '
#execute_query(connection, update)  
#select = 'Select Name from  inventory where Level="1";'
#drd = execute_read_query(connection, select)



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










Reload_stash()    



connection = create_connection("inventory.sqlite")
select = 'Select Name,Img_Location from  inventory;'
Mods_NameImg = execute_read_query(connection, select)