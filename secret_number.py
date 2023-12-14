secret_number = 9
guess = 0
guess_count = 4

while guess < guess_count:

    user = int (input("Coba tebak angka : "))
    if int(user) == 9:
        print("Anjay betul")
        break
    else:
        print("Coba lagi yaa <3")
        guess = guess + 1
else :
    print("Kesempatanmu udah habis")