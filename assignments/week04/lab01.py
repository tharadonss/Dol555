"""
Personal Information Manager 
#Tharadon Suesat 6730251115
#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies
 
#Allow the user to:
 
Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)
 
"""
 
# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Tharadon", 20, "Chonburi", "TH")  # name, age, city, country
    hobbies = []
 
    while True:
        choice = input("What do you want to do? (1:display, 2:add hobby, 3:remove hobby, 4:edit age, 5:exit)")
 
        if choice == "1":
            # Display all info
            print("Name: ", person[0])
            print("Age: ", person[1])
            print("City: ", person[2])
            print("Country: ", person[3])
            print("Hobbies: ", hobbies)
 
        elif choice == "2":
            # Append hobby
            hobby = input("What is your new hobbies: ")
            hobbies.append(hobby)  
 
        elif choice == "3":
            # Remove hobby
            if hobbies:  
                hobbies.pop()
            else:
                print("No hobbies to remove.")
 
        elif choice == "4":
            # Edit age
            person_list = list(person)  # ("jeerawat", 20, "Chonburi", "TH")
            age = input("How old are you?: ")
            try:
                person_list[1] = int(age) 
                person = tuple(person_list)
            except ValueError:
                print("Please enter a number.")
 
        elif choice == "5":
            break  
 
if __name__ == "__main__":
    personal_info_manager()