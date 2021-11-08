# Add your encryption methods here
def encode(file,key):
    num = key
    cipher = ""
    for i in file:
        conv = ord(i) + num
        letter_conv = chr(conv)
        cipher = cipher + letter_conv
    return(cipher)

def encode_better(file):
    message = str(input('What is your secret message?'))
    key = file
    cipher = ""
    for i in range(len(message)):
        conv = ord(key[i]) - 97
        l_conv = ord(message[i]) + conv
        letter_conv = chr(l_conv)
        cipher = cipher + letter_conv
    print(cipher)




