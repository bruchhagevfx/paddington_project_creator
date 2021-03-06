import os, sys
import webbrowser



print ("-----------------------------------")
print ("Paddington Project Creator V001")
print ("-----------------------------------")

##---------userinputs---------##
proj_location = input("enter a location for your project:") 
proj_name = input("enter Project Name:")
number_shots = 101 + int(input("enter number of Shots:"))
name_shots = input("Name Shots?..(y/n):")

##---------folder---------##
base_folder= ["00_pipeline","01_management","02_shots","03_assets","05_Dailies"]
task_folders = ["__publish","00_footage","01_layout","02_animation","03_effects","04_lighting","05_comp"]
management_folders= ["__in","__out","documents"]


shotdir = os.path.join(proj_location, proj_name, "02_shots")
shotlist = [] 




##----------##

    
def change_dir():
    os.chdir(proj_location)
    print ("create Project in:", os.getcwd())
    

def create_project():
    try:
        os.makedirs(proj_name)
    except OSError:
        print ("failed")
    else:
        print ("Project " + proj_name + " building..")
        print("-----------------------------------")


def create_base():
    os.chdir(proj_name)
    for folder in base_folder:
            os.mkdir(folder)


def create_shots():
    os.chdir("02_shots")
    print ("create Shots in:", os.getcwd())
    print("-----------------------------------")


    if name_shots == "n":
        for shots in range(101,number_shots):
            os.makedirs("sh_" + str(shots))

         
    else:
        for shots in range(101,number_shots):
            print ("Shot " + str(shots))
            pick_name = input("pick a name: ")
            print ()
            os.makedirs("sh_" + str(shots) + "_" + pick_name)


def get_shotlist():
    for subdir, dirs, files in os.walk(shotdir):
        for dir in dirs:
            shotlist.append(os.path.join(subdir, dir))


def create_task():
    for rootdir in shotlist:
        for folder in task_folders:
            os.mkdir(os.path.join(rootdir,folder))


def management_folder():
    os.chdir(os.path.join(proj_location,proj_name,"01_management"))
    for folder in management_folders:
            os.mkdir(folder)


def summary():
    print ("-----------------------------------")
    print ("Project.. " + proj_name + " ..created")
    print ("Location: "+ proj_location)
    print ("Shots created: " + str(number_shots-101))
    print ("-----------------------------------")
    print ("thanks for using Paddington")
    print ("devloped by Lucas Bruchhage 2020")
    print ("-----------------------------------")


def opendir():
    webbrowser.open('file:///' + proj_location)





##--------------##

#run those guys
change_dir()
create_project()
create_base()
create_shots()
get_shotlist()
create_task()
management_folder()

summary()
opendir()
