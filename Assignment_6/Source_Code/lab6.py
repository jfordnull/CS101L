########################################################################
##
## CS 101 Lab
## Program #6 (Lab Week 7)
## Jacob Ford
## jwfhmp@umkc.edu
##
########################################################################

import string 

def Caesar(string_text, int_key):
  '''Encrypts or decrypts string using specified key. Decided to make it one function since I was using the same logic for both.'''
  cipher = ''
  for i in string_text:
    if i.isalpha():
      new_char = (ord(i) - 65)
      new_char += int_key
        
      ##This is for situations where a character like 'A' is shifted by -1. Instead of becoming 7, it becomes Z
      if new_char < 0:
        new_char *= -1
        new_char = 26 - new_char
        #While loop allows for shift # < -25 without leaving alphabet
        while new_char < 0:
          new_char += 26

      ##This is for situations where a character like 'Z' is shifted by +1. Instead of becoming [ it becomes A.
      ##The while loop allows for a user to enter a value to shift by > 25 without leaving the alphabet
      while new_char > 25:
        new_char -= 26
        
      new_char += 65
      cipher += chr(new_char)
      
    #Didn't account for characters other than letters. Assignment examples use spaces, but unclear if numbers/symbols should represent errors.
    #Chose to preserve them, like spaces in the examples, within the string as they're entered
    else:
      cipher += i
  return cipher


def Encrypt(string_text, int_key): 
  '''Caesar-encrypts string using specified key.''' 
  cipher = Caesar(string_text, int_key)
  return cipher


def Decrypt(string_text, int_key): 
  ''' Decrypts Caesar-encrypted string with specified key. ''' 
  int_key *= -1
  decipher = Caesar(string_text, int_key)
  return decipher

 
def Get_input(): 
  '''Interacts with user. Returns one of: '1', '2', '3', '4'.'''
  return input('Enter your selection ==> ')
 

def Print_menu():
  '''Prints menu. No user interaction. '''
  print('MAIN MENU:\n1) Encode a string\n2) Decode a string\nQ) Quit')
  
  
def main(): 
  Again = True 
  while Again: 
    Print_menu()
    Choice = Get_input()
    print() 
    if Choice == '1': 
      Plaintext = input("Enter (brief) text to encrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext,'\n') 
    elif Choice == '2': 
      Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext, '\n') 
    elif Choice == 'Q' or Choice == 'q': 
      print("Have an ordinary day.") 
      Again = False 
    else:
      print('{} is not valid input.\n'.format(Choice))
      continue
      
      
# our entire program: 
main() 
