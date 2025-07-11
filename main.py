import datetime

# function for taking user entries
def user_entries(user_input):
    time = datetime.datetime.now()  #stores the current time and date
    updated_time = time.strftime("%Y-%m-%d %H:%M:%S") #converting to str in format(YYYY-MM-DD HH:MM:SS)
    with open("entries.txt","a",encoding="utf-8") as f:
        f.write(f"{updated_time} || {user_input}\n") #enter it in the file

#funtion to read the user entries
def read_user_entries():
    with open("entries.txt","r") as f: #using read mode
        entry = f.read()
        return entry
    
#filtering the entries through date
def search_through_date():
   
    with open("entries.txt","r",encoding="utf-8") as f: #reading the file
        data = f.readlines()
        if data == []: #check if the file is empty
            print("No data found")
        else: #if file have data then
            user_date = input("enter the date('YYYY-MM-DD'):")
            found = False #assuming that user has not entered any data on the day it is searching data for
            print("****** Data Entered on:",user_date,"******")
            for entry in data:
                if(user_date in entry):
                    print("😇",entry)
                    found = True #data found thus initialized to true
            
            if found == False: #if data is not found then
                print("No data has been entered that day!","😕")
 

print("""********** WELCOME TO GRATITUDE JOURNAL **********
Type:
1. To enter a new entry
2. To view all the entries
3. Search entries by date
4. To exit
""")

user_choice = int(input("Enter your choice: "))

#ask for user choice until it says to exit(i.e types 4)

while user_choice != 4:
    
    if user_choice == 1:
        user_input = input("Enter whatever you are grateful for: ")
        user_entries(user_input) #call the function created to write the entry to the file
        print("Your entry has been recorded successfully!")

    elif user_choice == 2:
        entry = read_user_entries() #call the function created to read the entries 

        if entry == "":
            print("No entries yet.")
        else:
            print("***************🥰 I AM GRATEFUL FOR 🥰***************")
            print(entry)

    elif user_choice == 3: 
        search_through_date() #call the function created to filter the entries through date

    user_choice = int(input("Enter your choice: "))

#once exited, print:
print("Thankyou, Have a good day!🤍")  
