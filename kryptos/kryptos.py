def encrypt(text, key):
    output = ""
    indexPos = 0
    key = key.lower()

    for character in text:
        if character >= "a" and character <= "z":
            shift = ord(key[indexPos % len(key)]) - ord("a")
            output += chr((ord(character) - ord("a") + shift) % 26 + ord("a"))
            indexPos += 1
        else:
            output += character

    return output

def decrypt(text, key):
    output = ""
    indexPos = 0
    text = text.lower()
    key = key.lower()
    
    for character in text:
        if character >= "a" and character <= "z":
            shift = ord(key[indexPos % len(key)]) - ord("a")
            output += chr((ord(character) - ord("a") - shift + 26) % 26 + ord("a"))
            indexPos += 1
        else:
            output += character
    
    return output

mode = ""
while mode != "e" or mode != "d":
    mode = input("Mode (e/d or anything else to end): ").lower()
    text = input("Text: ").lower()
    key = input("Key: ").lower()
    if mode == "e":
        print(f"Output: {encrypt(text,key)}")
    elif mode == "d":
        print(f"Output: {decrypt(text, key)}")
