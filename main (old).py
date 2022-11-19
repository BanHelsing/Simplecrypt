import random as r

is_file = False
while True:
    message = input("message\n")
    if message == "\open":
        try:
            is_file = True
            file_name = input("file?\n")
            if file_name == "\exit":
                break
            file_name = (file_name + ".txt")
            file = open(file_name, "r")
            message = file.read()
            file.close()
            break
        except FileNotFoundError:
            print("not found")
            continue
    else:
        break
    
key = input("key?\n")
choice = input("choice?\n")

def encrypt(message, key):
    counter = 0
    coded_message = ""
    key_num = int(key[-1])
    key = (len(key)-1) % key_num
    for i in message:
        letter = ord(i)
        if key % 2 == 0:
            if letter+key < 32 or letter+key > 125:
                key = key_num
            coded_message += chr(letter+key)
            coded_message += chr(r.randint(33,126))
        else:
            if letter+key < 32 or letter+key > 125:
                key = key_num
            coded_message += chr(letter-key)
            coded_message += chr(r.randint(33,126))
        if counter % 2 == 0:
            key += key_num
        else:
            key -= key
        counter += 1
    return coded_message


def decrypt(message, key):
    counter = 0
    decoded_message = ""
    key_num = int(key[-1])
    key = (len(key)-1) % key_num
    for i in range(0, len(message), 2):
        letter = ord(message[i])
        if key % 2 == 0:
            decoded_message += chr(ord(message[i])-key)
            if letter+key < 32 or letter+key > 125:
                key = key_num
        else:
            decoded_message += chr(ord(message[i])+key)
            if letter+key < 32 or letter+key > 125:
                key = key_num
        if counter % 2 == 0:
            key += key_num
        else:
            key -= key
        counter += 1
    return decoded_message

while True:
    if choice == "e":
        coded_message = encrypt(message, key)
        if is_file:
            with open(file_name, "w") as file:
                file.write(coded_message)
                file.close()
        else:
            print(coded_message)
        break
    elif choice == "d":
        decoded_message = decrypt(message, key)
        if is_file:
            with open(file_name, "w") as file:
                file.write(decoded_message)
                file.close()
        else:
            print(decoded_message)
        break
    else:
        choice = input("\n")

