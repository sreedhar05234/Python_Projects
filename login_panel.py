import csv
file="login_details.txt"
def check(uname,passwrd):   #this will verify the credentials
    with open(file) as f:   #accessing the file storing the credentials
        data=csv.reader(f)  #reading the file using csv
        for line in data:   #checking each line and verifying the crfedentials and displaying the message accordingly
            try:
                unameC=line[0]
                pswrdC=line[1]
                if uname==unameC and passwrd==pswrdC:
                    print("Login Successful")
                    break   #in case of correct cfedentials it will ask you to re-enter thecredentials to verify
            except IndexError:
                pass
        else:
            print("Try again")
            credentials()
def credentials():          #this function will take credentials from user
    uname=input("Enter username: ") 
    passwrd=input("Enter password: ")
    check(uname,passwrd)

if __name__=="__main__":
    credentials()
