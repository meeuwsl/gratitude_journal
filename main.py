import datetime
import string

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

#analyzing journal (most frequently used words)
def analyze_journal():

    with open("entries.txt","r",encoding="utf-8") as f:
        data = f.readlines()
        if data == []:
            print("No entries yet, start journaling!🚀") 
        else:
            new_data = []
            for i in data:
                if "||" in i: #seperating the entry and timestamp
                    new = i.split("||")
                    new_data.append(new[1].strip().lower()) #new_data will only have the entry

            #combining all the entries into one string 
            count =  0
            combined_entry = ""  
            while count<len(new_data):
                combined_entry += new_data[count]+" "
                count = count+1
    
            #removing punctuations
            for punct in string.punctuation:
                combined_entry = combined_entry.replace(punct,"")

            #splitting the string into words:
            words = combined_entry.split(" ")

            waste_words = ["the","a","for","of","in","at","every","being","to"]
            filtered_words = [word for word in words if word not in waste_words]

            #word count
            word_freq = {}
            for word in filtered_words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1

            if word_freq == {}:
                print("Nothing to reflect as such, write more! You got this💗")
            else:
                #printing most occuring word
                flag  = False
                print("**********You are consistently grateful for-being: **********")
                for word,count in word_freq.items():
                    if(count>=3):
                        print("🫶 ",word)
                        flag = True
                if(flag==False):
                    print("Be grateful, write more, be consistent! Not written enough to draw a conclusion🥶")

def check_streak():

    with open("entries.txt","r") as f:
        #read the file
        data = f.readlines()

        #split the entry on the basis of " "
        processed_entry = []
        for entry in data:
            processed_entry.append(entry.rsplit(" "))
        
        #append only the dates into the dates array
        dates = []
        for entry in processed_entry:
            dates.append(entry[0]) 

    #convert dates into set datatype to remove duplicates
    filter_dates = set(dates)

    #convert back into list
    filter_dates = list(filter_dates)

    #extracting the current date
    today = datetime.datetime.now()
    curr_date = today.strftime("%Y-%m-%d")
    
    converted_dates = [datetime.datetime.strptime(d, "%Y-%m-%d").date() for d in filter_dates]

    converted_dates_set = set(converted_dates)
    
    current_day = datetime.date.today()
    current_day -= datetime.timedelta(days=1)

    streak = 0
    current_day = datetime.date.today()
    while current_day in converted_dates_set:
        streak += 1
        current_day -= datetime.timedelta(days=1)

    print(f"🔥 You’re on a {streak}-day gratitude streak!")

    if(streak==0):
        print("Start jounaling daily to begin😉")
                
def delete_entry():

    try:
        with open("entries.txt","r",encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No entries yet. Start writing..🖋️")
        return

    if lines == []:
        print("No entries to delete.")
        return

    print("***************🗑️ SELECT ENTRY TO DELETE 🗑️***************")
    for idx, line in enumerate(lines, start=1):
        print(f"{idx}. {line}", end="")

    try:
        choice = int(input("Enter the entry number to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice < 1 or choice > len(lines):
        print("Invalid choice. No entry deleted.")
        return

    to_delete = lines[choice - 1].rstrip("\n")
    confirm = input(f"Delete this entry? (y/N) => {to_delete}\n").strip().lower()
    if confirm != 'y':
        print("Deletion cancelled.")
        return

    del lines[choice - 1]
    with open("entries.txt","w",encoding="utf-8") as f:
        f.writelines(lines)
    print("Entry deleted successfully.")

print("""**********🙏 WELCOME TO GRATITUDE JOURNAL 🙏**********
Type:
1. To enter a new entry
2. To view all the entries
3. Search entries by date
4. Aanalyze journal
5. Check streak🔥
6. To exit
7. Delete an entry
""")

user_choice = int(input("Enter your choice: "))

#ask for user choice until it says to exit(i.e types 6)

while user_choice != 6:

    if user_choice == 1:
        user_input = input("Enter whatever you are grateful for: ")
        user_entries(user_input) #call the function created to write the entry to the file
        print("Your entry has been recorded successfully!")

    elif user_choice == 2:
        entry = read_user_entries() #call the function created to read the entries 

        if entry == "":
            print("No entries yet. Start writing..🖋️")
        else:
            print("***************🥰 I AM GRATEFUL FOR 🥰***************")
            print(entry)

    elif user_choice == 3: 
        search_through_date() #call the function created to filter the entries through date

    elif user_choice == 4: 
        analyze_journal() #call the function created to filter the entries through date

    elif user_choice == 5: 
        check_streak() #call the function created to track your streak

    elif user_choice == 7:
        delete_entry()

    user_choice = int(input("Enter your choice: "))

#once exited, print:
print("Thankyou, Have a good day!🤍")  
