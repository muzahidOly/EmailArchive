#Project
def menu():
    choice=0   
    while int(choice)!=5:        
        print('Menu\n-------------------------------------')
        print('1. Look up email address\n2. Add a new name and email address')
        print('3. Change an existing email address\n4. Delete a name and email address')
        print('5. Quit the program')
        choice=input('Enter your choice: ')
        
        if int(choice)==5:
            return save(information)
        elif int(choice)==1:
            return exist(information)
        elif int(choice)==2:
            return add(information)
        elif int(choice)==3:
            return change(information)
        elif int(choice)==4:
            return delete(information)
#---------------------------------------
def add(information):
    addname=input('Enter name: ')    
    file=open('email.txt','r+')       
    if addname not in information.keys():
        addemail=input('Enter email address: ')
        information[addname] = addemail
        print("Saved")
    elif addname in information.keys():
        print("That name is already saved")
    
    return menu()
#----------------------------------------------------------------
def exist(information):    
    lookname=input('Enter name: ')    
    if lookname in information.keys():
        print('Email: ',information[lookname])
    elif lookname not in information.keys():
        print("No data")
    
    return menu()
#----------------------------------------------------------------
def change(information):
    
    changename=input('Name of the email youd like to change: ')
    changeemail=input('Name of the new email: ')
    if changename in information.keys():
        information[changename]=changeemail            
        print('Your email has been changed')
    else:
        print('Name not found')
    
    return menu()
#----------------------------------------------------------------       
def delete(information):
    deletename=input('Name of the email youd like to delete: ')    
    if deletename in information.keys():
        del information[deletename]
        print('Deleted')
    else:
        print('Name not found')
    
    return menu()
#----------------------------------------------------------------
def save(information):
    file=open('email.txt','w')
    for name,email in information.items():
        file.write(name)
        file.write(":")
        file.write(information[name])
        file.write("\n")
    
    print('Your information was saved')
#----------------------------------------------------------------
information={}
file=open('email.txt','r+')
for line in file:
    x = line.strip("\n").split(":")
    name = x[0]
    email = x[1]
    information[name] = email
menu()























