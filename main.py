import datetime

def user_entries(user_input):
    time = datetime.datetime.now()
    updated_time = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("entries.txt","a",encoding="utf-8") as f:
        f.write(f"\n{updated_time} || {user_input}")

def read_user_entries():
    with open("entries.txt","r") as f:
        entry = f.read()
        return entry
    

print("""**********WELCOME TO GRATITUDE JOURNAL **********
Type:
1. To enter a new entry
2. To view all the entries
3. To exit
""")
user_choice = int(input("Enter your choice: "))

if user_choice == 1:
    user_input = input("Enter whatever you are grateful for: ")
    user_entries(user_input)
    print("Your entry has been recorded successfully!")
elif user_choice == 2:
    print("***************🥰 I AM GRATEFUL FOR 🥰***************")
    entry = read_user_entries()
    print(entry)
else:
    print("Thankyou")
