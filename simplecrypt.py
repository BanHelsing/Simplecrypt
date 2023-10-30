import random as r
import regex as re

# .venv\Scripts\activate

#excluded = [34, 44]
#        = [ ",  ']
valid = [i for i in range(33,126)]
#valid = [i for i in range(33,126) if i not in excluded]


def chk_key(key) -> bool:
    """Checks the validity of the given key

    Args:
        key (str): The key to check

    Returns:
        bool: True if valid, False otherwise
    """
    return True if re.match("^([a-z]+)\d$", key) else False
    
    
def encrypt(message, key, file_name = "") -> str:
    """Encrypts based on the key provided      

    Args:
        message (str): The string to be encrypted
        key (str): The key used for encryption should be a short word followed
            by a single number with no whitespace inbetween them.
            eg: sword5, main8, magnetic2

    Raises:
        Exception: If the key doesn't follow the format

    Returns:
        str: Encrypted string
    """
    #TODO add dopc for filename
    # the fuck is this comment above supposed to mean?
    if not chk_key(key):
        raise Exception("Invalid encryption key")
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
            coded_message += chr(r.choice(valid))
            #coded_message += chr(r.randint(33,126))
        else:
            if letter+key < 32 or letter+key > 125:
                key = key_num
            coded_message += chr(letter-key)
            coded_message += chr(r.choice(valid))
            #coded_message += chr(r.randint(33,126))
        if counter % 2 == 0:
            key += key_num
        else:
            key -= key
        counter += 1
    if file_name == "":
        return coded_message
    with open(file_name,'w', encoding="ascii") as output:
        output.write(coded_message)
        return coded_message


def decrypt(message, key) -> str:
    """Decrypts based on the key provided

    Args:
        message (str): The string to be decrypted
        key (str): The key used for decryption should be a short word followed
            by a single number with no whitespace inbetween them.
            eg: sword5, main8, magnetic2

    Raises:
        Exception: If the key doesn't follow the format

    Returns:
        str: Decrypted string
    """
    if not chk_key(key):
        raise Exception("Invalid encryption key")
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