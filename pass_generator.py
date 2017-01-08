import random

def password_generator():
    upper_letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    number = ["1","2","3","4","5","6","7","8","9","0"]
    simbols = ["!","@","#","$","%","^","&","*"]
    weak_pass = ["fakepass", "weakpass", "menphis"]
    new_pass = []
    while True:
        choice = raw_input('How strong password you need: ')
        if choice == "weak":
            new_pass.append(weak_pass[random.randint(0, len(weak_pass) - 1)])
            break
        elif choice == "strong":
            for x in range(9):
                new_pass.append(upper_letter[random.randint(0,len(upper_letter) - 1)])
            for i in range(2):
                new_pass.append(number[random.randint(0,len(number) - 1)])

            for j in range(2):
                new_pass.append(simbols[random.randint(0,len(simbols) - 1)])
            break
    return ''.join(new_pass)

print password_generator()
