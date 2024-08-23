import random

#list of names
names = ["Milad", "Behdad", "Parsa", "Saeb", "Taher"]

#Random word generator
selected_name = random.choice(names)
guessed_count = len(selected_name)
guessed_list = ['-'] * len(selected_name)
while guessed_count > 0:
    guessed_char = input("Enter a character:  \n")
    
    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print("You have guessed befor, try new character. ")
            else:
                for idx, char in enumerate(selected_name):
                    if char == guessed_char:
                        guessed_list[idx] = guessed_char
                current_guess = " ".join(guessed_list)
                print(f"Perfect => {current_guess}")
                
                if not "-" in guessed_list:
                    print("You won!")
                    break
        else:
            guessed_count -= 1
            print("Wrong!")
    else:
        print("Enter a valid character.")