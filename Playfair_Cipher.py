import time
from array import *
#Playfair Cipher

#Things to make it pretty
def start():
    print("Booting up...")
    time.sleep(2)
    print("Initializing...")
    time.sleep(2)
    print("Finalizing..")
    time.sleep(1)
    print("Welcome to Ciphertext Inx.")
    time.sleep(1)

def confirm(question):
    while True:
        answer = input(question)

        if answer in ["encrypt" , "Encrypt"]:
            return True
        elif answer in ["decrypt", "Decrypt"]:
            return False

def spacetextopen(text):
    i = 0
    counter = 0
    temp = text.replace(" ","")
    spaced_text = ""
    while i < len(temp):
        if counter == 2:
            spaced_text += " "
            counter = 0
        else:
            spaced_text += temp[i]
            counter += 1
            i += 1
    return spaced_text

def spacetextclosed(text):
    closed = ""
    for letter in text:
        if letter == " ":
            closed += ""
        else:
            closed += letter
    return closed

def filtertext(plaintext):
    filteredtext = ""
    for i in range(len(plaintext)):
        if plaintext[i] == plaintext[i-1]:
            filteredtext += "x"
        else:
            filteredtext += plaintext[i]
    if len(filteredtext) % 2 == 1:
        filteredtext += "z"
    return filteredtext

#def unfiltertext(text):

#Creations 
def create_key(word):
    key = "abcdefghiklmnopqrstuvwxyz"
    for letter in word:
        if word.count(letter) > 1:
            i = word.index(letter)
            word = word[:i]+word[i+1:]
    for letter in key:
        if word.find(letter) == -1:
            word += letter
    return word

def create_array(keyword):
    counter = 0
    Square = [[None,None,None,None,None],
              [None,None,None,None,None],
              [None,None,None,None,None],
              [None,None,None,None,None],
              [None,None,None,None,None]]
    for i in range(5):
        for j in range(5):
            Square[i][j] = keyword[(counter)]
            counter += 1
    return Square    

#Encrytion section
def encryption_setup(plaintext,keyword):
    key = create_key(keyword)
    Square = create_array(key)
    filtered = filtertext(plaintext)
    spaced = spacetextopen(filtered)
    return spaced,Square

def decryption_setup(ciphertext,keyword):
    key = create_key(keyword)
    Square = create_array(key)
    spaced = spacetextopen(ciphertext)
    return spaced,key,Square

def get_rc(Square,letter):
    r = 0
    c = 0
    for i in range (5):
        for j in range (5):
            if Square[i][j] == letter:
                r = i
                c = j
    return r,c
            

def playfair_encrypt(plaintext,keyword):
    ciphertext = ""
    text,Square = encryption_setup(plaintext, keyword)
    x1,y1,x2,y2 = 0,0,0,0
    a1,a2,b1,b2 = 0,0,0,0
    letterp1 = ""
    letterp2 = ""
    lettere1 = ""
    lettere2 = ""
    for i in range(len(text)-1):
        letterp1 = text[i]
        letterp2 = text[i+1]
        if letterp1 != " " and letterp2 != " ":
            x1,y1 = get_rc(Square, letterp1)
            x2,y2 = get_rc(Square, letterp2)
            #vertical problems
            if y1 == y2:
                z = y1
                a = (x1+1)%5
                b = (x2+1)%5
                lettere1 = Square[a][z]
                lettere2 = Square[b][z]
            #horizontal problems
            elif x1 == x2:
                z = x1
                a = (y1+1)%5
                b = (y2+1)%5
                lettere1 = Square[z][a]
                lettere2 = Square[z][b]
            else:
                lettere1 = Square[x1][y2]
                lettere2 = Square[x2][y1]
                found = False

                for i in range (5):
                    for j in range(5):
                        if Square[i][j] == lettere1:
                            found = True
                        if Square[i][j] == lettere2 and not found:
                            lettere1 = Square[x2][y1]
                            lettere2 = Square[x1][y2]
                
        ciphertext += (lettere1 + lettere2)
        lettere1,lettere2 = "",""
    return ciphertext
    
#Decryption


    
def playfair_decrypt(ciphertext,keyword):
    plaintext = ""
    text,key,Square = decryption_setup(ciphertext,keyword)
    x1,y1,x2,y2 = 0,0,0,0
    a1,a2,b1,b2 = 0,0,0,0
    letterp1 = ""
    letterp2 = ""
    letterd1 = ""
    letterd2 = ""
    for i in range(len(text)-1):
        letterp1 = text[i]
        letterp2 = text[i+1]
        if letterp1 != " " and letterp2 != " ":
            x1,y1 = get_rc(Square, letterp1)
            x2,y2 = get_rc(Square, letterp2)
            #Verticle Problem
            if y1 == y2:
                z = y1
                a = x1 - 1
                b = x2 - 1

                if a < 0:
                    a = 4
                if b < 0:
                    b = 4

                letterd1 = Square[a][z]
                letterd2 = Square[b][z]
            #Horizontal Problem
            elif x1 == x2:
                z = x1
                a = y1 - 1
                b = y2 - 1
                
                if a < 0:
                    a = 4
                if b < 0:
                    b = 4
                    
                letterd1 = Square[z][a]
                letterd2 = Square[z][b]
            else:
                letterd1 = Square[x1][y2]
                letterd2 = Square[x2][y1]
                
                

                            
        plaintext += (letterd1 + letterd2)
        letterd1,letterd2 = "",""
    return plaintext

text = "fwdwdbndutfzpx"
keyword = "band"

print(playfair_decrypt(text,keyword))
##start()
##task = confirm("Would you like to encrypt or decrypt text?")
##keyword = input("Please input key for cipher")
##
##if task == True:
##    plaintext = input("Insert message you want to encrypt")
##    print("Encrypting....")
##    time.sleep(3)
##    print(playfair_encrypt(plaintext, keyword))
    
##if task == False:
##    ciphertext = input("Insert message you want to decrypt")
##    print("Decrypting....")
##    time.sleep(5)
##    print(playfair_decrypt(ciphertext))

