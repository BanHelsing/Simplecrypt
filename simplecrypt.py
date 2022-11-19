import random as r

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