import sqlite3
from sqlite3 import Error


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






create_users_table = """
DROP TABLE  inventory ;
CREATE TABLE IF NOT EXISTS  inventory (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Name TEXT,
  NiceName TEXT,
  Reward TEXT,
  Level INTEGER,
  Img_Location TEXT,
  Checked TEXT,
  Bonus TEXT
);
"""

create_color_table = """
CREATE TABLE IF NOT EXISTS Color0 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color1 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color2 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color3 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color4 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color5 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color6 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color7 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color8 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color9 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color10 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color11 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color12 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color13 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color14 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color15 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color16 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color17 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color18 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color19 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color20 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color21 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color22 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color23 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );
CREATE TABLE IF NOT EXISTS Color24 (  id INTEGER PRIMARY KEY AUTOINCREMENT ,  Por1z1 TEXT  ,  Por1z2 TEXT ,  Por2z2 TEXT,  Por1z3 TEXT,  Por2z3 TEXT,  Por3z3 TEXT,  Por1z4 TEXT,  Por2z4 TEXT,  Por3z4 TEXT,  Por4z4 TEXT );

"""

insert = """
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Toxic" ,"Toxic","Generic,Gems","1","img/Toxic.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Chaosweaver" ,"Chaosweaver","Gems","1","img/Chaosweaver.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Frostweaver" ,"Frostweaver","Armour","1","img/Frostweaver.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Permafrost" ,"Permafrost","Generic,Armour","1","img/Permafrost.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Hasted" ,"Hasted","Generic","1","img/Hasted.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Deadeye" ,"Deadeye","Armour,Trinkets","1","img/Deadeye.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Bombardier" ,"Bombardier","Weapon,Armour","1","img/Bombardier.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Flameweaver" ,"Flameweaver","Weapon","1","img/Flameweaver.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Incendiary" ,"Incendiary","Generic,Weapon","1","img/Incendiary.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Arcane_Buffer","Arcane Buffer","Essences","1","img/Arcane_Buffer.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Echoist" ,"Echoist","Generic,Currency","1","img/Echoist.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Stormweaver" ,"Stormweaver","Trinkets","1","img/Stormweaver.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Dynamo" ,"Dynamo","Generic,Trinkets","1","img/Dynamo.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Bonebreaker" ,"Bonebreaker","Generic,Weapon","1","img/Bonebreaker.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Bloodletter" ,"Bloodletter","Weapon,Trinkets","1","img/Bloodletter.png","0","Items dropped from the Monster and its Minions are Corrupted"); 
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Steelinfused" ,"Steel-infused","Weapon","1","img/Steel-infused.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Gargantuan" ,"Gargantuan","Currency","1","img/Gargantuan.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Berserker" ,"Berserker","Uniques","1","img/Berserker.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Sentinel" ,"Sentinel","Armour,Armour","1","img/Sentinel.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Juggernaut" ,"Juggernaut","Harbinger","1","img/Juggernaut.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Vampiric" ,"Vampiric","Fossils","1","img/Vampiric.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Overcharged" ,"Overcharged","Trinkets,Trinkets","1","img/Overcharged.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Soul_Conduit" ,"Soul Conduit","Maps","1","img/Soul_Conduit.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Opulent" ,"Opulent","Generic,Gems","1","img/Opulent.png","0","Monster is fabulously wealthy");       
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Malediction" ,"Malediction","DivinationCards","1","img/Malediction.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Consecrator" ,"Consecrator","Fragments","1","img/Consecrator.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Frenzied" ,"Frenzied","Generic,Uniques","1","img/Frenzied.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Heralding_Minions","Heralding Minions","Fragments,Fragments","2","img/Heralding_Minions.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Empowering_Minions","Empowering Minions","Blight,Ritual","2","img/Empowering_Minions.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Assassin","Assassin","Currency,Currency","2","img/Assassin.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Trickster","Trickster","Currency,Uniques,DivinationCards","2","img/Trickster.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Necromancer","Necromancer","Generic","2","img/Necromancer.png","0","Rewards are rolled 2 additional times, choosing the rarest result"); 
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Rejuvenating","Rejuvenating","Currency","2","img/Rejuvenating.png","0","Rewards are rolled 1 additional time, choosing the rarest result"); 
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Executioner","Executioner","Legion,Breach","2","img/Executioner.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Hexer","Hexer","Essences,Essences","2","img/Hexer.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Drought_Bringer","Drought Bringer","Labyrinth,Labyrinth","2","img/Drought_Bringer.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Entangler","Entangler","Fossils,Fossils","2","img/Entangler.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Temporal_Bubble","Temporal Bubble","Heist,Expedition","2","img/Temporal_Bubble.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Treant_Horde" ,"Treant Horde","Generic","2","img/Treant_Horde.png","0","Monster's Minions drop a randomly-chosen Reward Type");   
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Frost_Strider" ,"Frost Strider","Armour,Armour,Armour","2","img/Frost_Strider.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Ice_Prison" ,"Ice Prison","Armour,Armour","2","img/Ice_Prison.png","0","Rewards are rolled 1 additional time, choosing the rarest result");
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Soul_Eater" ,"Soul Eater","Maps,Maps","2","img/Soul_Eater.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Flame_Strider" ,"Flame Strider","Weapon,Weapon,Weapon","2","img/Flame_Strider.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Corpse_Detonator" ,"Corpse Detonator","DivinationCards,DivinationCards","2","img/Corpse_Detonator.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Evocationist" ,"Evocationist","Generic,Weapon,Armour,Trinkets","2","img/Evocationist.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Magma_Barrier" ,"Magma Barrier","Weapon,Weapon","2","img/Magma_Barrier.png","0","Rewards are rolled 1 additional time, choosing the rarest result");
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Mirror_Image" ,"Mirror Image","Scarabs","2","img/Mirror_Image.png","0","Rewards are rolled 2 additional times, choosing the rarest result");
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Storm_Strider" ,"Storm Strider","Trinkets,Trinkets,Trinkets","2","img/Storm_Strider.png","0","None");         
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Mana_Siphoner" ,"Mana Siphoner","Trinkets,Trinkets","2","img/Mana_Siphoner.png","0","Rewards are rolled 1 additional time, choosing the rarest result");
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Corrupter" ,"Corrupter","Abyss,Abyss","2","img/Corrupter.png","0","Items dropped from the Monster and its Minions are Corrupted"); 
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Invulnerable" ,"Invulnerable","Delirium,Metamorphosis","2","img/Invulnerable.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Crystalskinned" ,"Crystal-skinned","Harbinger,Harbinger","2","img/Crystal-skinned.png","0","None");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Empowered_Elements" ,"Empowered Elements","Uniques,Uniques","2","img/Empowered_Elements.png","0","Rewards are rolled 1 additional time, choosing the rarest result");
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Effigy" ,"Effigy","DivinationCards,DivinationCards","2","img/Effigy.png","0","Rewards are rolled 1 additional time, choosing the rarest result"); 
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Lunaristouched" ,"Lunaris-touched","Uniques","3","img/Lunaris-touched.png","0","All Reward Types have an additional reward");    
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Solaristouched" ,"Solaris-touched","Scarabs","3","img/Solaris-touched.png","0","All Reward Types have an additional reward");    
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Arakaalitouched" ,"Arakaali-touched","DivinationCards","3","img/Arakaali-touched.png","0","All Reward Types are Divination Cards");     
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Brine_Kingtouched" ,"Brine King-touched","Armour,Armour,Armour","3","img/Brine_King-touched.png","0","Rewards are rolled 6 additional times, choosing the rarest result");
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Tukohamatouched" ,"Tukohama-touched","Weapon,Weapon,Fragments","3","img/Tukohama-touched.png","0","Rewards are rolled 4 additional times, choosing the rarest result"); 
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Abberathtouched" ,"Abberath-touched","Trinkets,Trinkets,Maps","3","img/Abberath-touched.png","0","Rewards are rolled 4 additional times, choosing the rarest result");          
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Shakaritouched" ,"Shakari-touched","Uniques","3","img/Shakari-touched.png","0","All Reward Types are Uniques");      
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Innocencetouched" ,"Innocence-touched","Currency,Currency,Currency","3","img/Innocence-touched.png","0","All Reward Types are Currency");      
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Kitavatouched" ,"Kitava-touched","Generic","3","img/Kitava-touched.png","0","Rewards are doubled");							
insert into inventory (Name,NiceName,Reward,Level,Img_Location,Checked,Bonus) values ("Empty" ,"Empty","Dick","4","img/Empty.png","0","Rewards are in your ass");
"""



drd="""
CREATE TABLE IF NOT EXISTS Toxic (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Chaosweaver (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Frostweaver (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Permafrost (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Hasted (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Deadeye (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Bombardier (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Flameweaver (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Incendiary (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Arcane_Buffer (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Echoist (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Stormweaver (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Dynamo (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Bonebreaker (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Bloodletter (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Steelinfused (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Gargantuan (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Berserker (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Sentinel (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Juggernaut (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Vampiric (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Overcharged (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Soul_Conduit (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Opulent (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Malediction (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Consecrator (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Frenzied (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Heralding_Minions (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Empowering_Minions (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Assassin (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Trickster (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Necromancer (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Rejuvenating (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Executioner (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Hexer (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Drought_Bringer (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Entangler (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Temporal_Bubble (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Treant_Horde (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Frost_Strider (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Ice_Prison (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Soul_Eater (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Flame_Strider (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Corpse_Detonator (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Evocationist (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Magma_Barrier (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Mirror_Image (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Storm_Strider (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Mana_Siphoner (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Corrupter (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Invulnerable (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Crystalskinned (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Empowered_Elements (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Effigy (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Lunaristouched (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Solaristouched (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Arakaalitouched (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Brine_Kingtouched (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Tukohamatouched (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Abberathtouched (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Shakaritouched (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Innocencetouched (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Kitavatouched (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Empty (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER  );
CREATE TABLE IF NOT EXISTS Stash (  id INTEGER PRIMARY KEY AUTOINCREMENT,  Cordx INTEGER,  Cordy INTEGER, Name Text, Color Text,Checked INTEGER );
"""

connection = create_connection("inventory.sqlite")
execute_query(connection, create_color_table)
execute_query(connection, create_users_table) 
execute_query(connection, drd)  
execute_query(connection, insert)  
