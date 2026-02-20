req_met = False
print('Password needs 12 characters, 1 Upper, 1 Lower, and 1 Special Character.')
user_input = input('Password:')
while req_met == False:  
    up_char = False
    low_char = False
    spec_char = False
    
    if len(user_input) >= 12:
        for char in user_input:
            if char.isupper():
                up_char = True
            elif char.islower():
                low_char = True
            elif char.isalnum() == False:
                spec_char = True
        if up_char and low_char and spec_char == True:
            print('Password created succefuly!')
            req_met = True
        else:
            if up_char == False:
                print('Missing a Upper Character')
                user_input = input('Password:')
            elif low_char == False:
                print('Missing a Lower Character')
                user_input = input('Password:')
            elif spec_char == False:
                print('Missing a Special Character')
                user_input = input('Password:')
    else:
        print(f"Password is {(12 - len(user_input))} characters too short. Try Again.")
        user_input = input('Password:')