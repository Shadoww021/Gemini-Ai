# users={
#     'ali':'1234',
#     'hasan':'2345',
#     'reza':'6789'
# }
# max_ateempt = 5
# attempt = 0
# while max_ateempt>attempt:
#     entered_username=input("Enter your username: ").strip()  
#     attempt+=1
# while entered_username not in users:    
#     remailning=max_ateempt-attempt                            #Check username
#     entered_username=input(f"Wrong username\nYou have{remailning} choice\nEnter again username : ").strip()    #if its wrong,Take is again
# while max_ateempt>attempt:   
#     entered_pass=input("Enter your pass: ").strip()                 #Take pass
#     users[entered_username]!=entered_pass                           #Check pass
#     remailning=max_ateempt-attempt
#     entered_pass=input("Wrong pass!\nEnter again your pass : ").strip()         #if pass wrong,Take it again
#     if remailning==0:
#         print("You loged in")
# ---------------------------------------------------------------------------------------------------------------------------------------------
#login

users = {
    'ali': '1234',
    'hasan': '2345',
    'reza': '6789'
}

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    entered_username = input("Enter your username: ").strip()
    attempts += 1
    remaining = max_attempts - attempts
    
    if entered_username not in users:
        if remaining > 0:
            print(f"Wrong username! You have {remaining} attempt(s) left.")
        continue
    
    entered_pass = input("Enter your pass: ").strip()
    if entered_pass == users[entered_username]:
        print("Welcome bro")
        break
    else:
        if remaining > 0:
            print(f"Wrong password! You have {remaining} attempt(s) left.")
        continue

if attempts == max_attempts and entered_pass != users.get(entered_username, ''):
    print("You have used all your attempts. Access denied.")
# ------------------------------------------------------------------
#password
def Mu_pass(password):
    if len(password) < 8:
        print("Your pass must had 8 char")
    elif password.isnumeric():          #if all pass be number it returns true
        print("Your pass must have at least one letter")     
    elif password.isalpha():           #if all pass be words it return true
        print("Your pass must have at least one number")
    elif password.isupper():
        print("Your pass must have at least one small word")
    elif password.islower():
        print("Your pass must have at least one big word")
    else:
        print("Your pass is right")


while True:
    password = input("Enter your password: ").strip()
    password = password.replace(" ", "")  # Remove all spaces
    result = Mu_pass(password)
    print(result)

    continue_choice = input("Do you want to try another password? (yes/no): ").lower()
    if continue_choice != 'yes':
        break