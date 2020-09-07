import os, sys


print ("-----------------------------------")
print ("Paddington Project Creator V001")
print ("-----------------------------------")

proj_location = "/Volumes/zeugs/00_pipeline/testproj"
proj_name = input("enter Project Name:")
number_shots = 101 + int(input("enter number of Shots:"))
name_shots = input("Name Shots?..(y/n):")
user_tasks = input("put task: ")
task_list = user_tasks.split(",")
print (task_list)

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



def create_shots():
    os.chdir(proj_name)
    os.makedirs("02_shots")
    os.chdir("02_shots")
    print ("create Shots in:", os.getcwd())
    print("-----------------------------------")


    if name_shots == "n":
        for shots in range(101,number_shots):
            #os.makedirs(str(shots))
            shot = str(shots)
            task = str(task_list)
            print(task)
    else:
        for shots in range(101,number_shots):
            print ("Shot " + str(shots))
            pick_name = input("pick a name: ")
            print ()
            os.makedirs(str(shots)+"_"+pick_name)



def summary():
    print ("-----------------------------------")
    print ("Project.. " + proj_name + " ..created")
    print ("Location: "+ proj_location)
    print ("Shots created: " + str(number_shots-101))
    print ("-----------------------------------")
    print ("thanks for using Paddington")
    print ("devloped by Lucas Bruchhage 2020")
    print ("-----------------------------------")




##--------------##

#run those guys
change_dir()
create_project()
create_shots()
summary()
