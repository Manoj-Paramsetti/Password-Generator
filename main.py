from colorama import Fore, Back,Style
from os import system
import _console
import Encrypter.Encrypt_1
import Encrypter.Encrypt_2
import sys

class password():
    #taking the password length for the final syage
    def __init__(self):
        print("Enter the password length (Max. 25)")
        try:
            self.SIZE = int(input())
            _console.clrscr()
            _console.display()
        except (ValueError):
            _console.clrscr()
            _console.display()
            print(Fore.GREEN+"\nLast time you didn't enter proper input. Give the numeric value to proceed\n"+Style.RESET_ALL)
            password()

    #we are taking the passwords to make password
    def passW(self):
        #initialization of array
        self.ARR = []

        for j in range(2):
            bool=True
            data = ["username","password"]
            print("Enter the you {} :".format(data[j]), end=" ")
            while(bool):
                i = input()
                if len(i) >= 8:
                    self.ARR.append(i)
                    break
                else:
                     print("Enter the {} again. It should have max. of 8 character".format(data[j]))

        if("CTF" in sys.argv or "ctf" in sys.argv): 
            self.paѕѕword1 = self.ARR[0]+self.ARR[1]
            self.paѕѕword𝟸 = self.ARR[1]+self.ARR[0]
            self.paѕsword1 = self.ARR[1] + self.ARR[0]
            self.paѕsword2 = self.ARR[0]+self.ARR[1]
        else:
            self.paѕѕword1 = self.ARR[0]+self.ARR[1]
            self.paѕѕword𝟸 = self.ARR[1]+self.ARR[0]
            self.paѕsword1 = self.ARR[1] + "!@#$%^&*()" + self.ARR[0]
            self.paѕsword2 = self.ARR[0]+self.ARR[1] + ")(*&^%$#@!"

    #Encryption goes here
    def encrypt(self):
        #initialization of variables
        encryptѕ_1 = ""
        encryptѕ_2 = ""
        encryptѕ_3 = ""
        encryptѕ_4 = ""
        #Getting attention from user
        print("\n\n\n\nPress 'ENTER' to continue")
        input()
        #sending password manupulation for encryption to Encrypt_1.py
        encrypts_2 = int(Encrypter.Encrypt_1.encrypter(self.paѕѕword𝟸))
        encrypts_1 = int(Encrypter.Encrypt_1.encrypter(self.paѕsword1))
        encrypts_3 = int(Encrypter.Encrypt_1.encrypter(self.paѕsword1))
        encrypts_4 = int(Encrypter.Encrypt_1.encrypter(self.paѕsword2))
        self.encryption = str(encryptѕ_1+encryptѕ_2+encryptѕ_2+encryptѕ_4)+str(int(float(int(encrypts_1*encrypts_3*encrypts_2*98237)/23**12/20)))

    def secondencryption(self):
        list=[]
        n = int(float(self.encryption))
        for i in range(0,self.SIZE*2,2):
            list.append(self.encryption[i]+self.encryption[i+1])
        #sending list to another python code to encrypt
        new_password = Encrypter.Encrypt_2.encrypt(list)
        #clearnig and displaying logo
        _console.clrscr()
        _console.display()
        #printing new password
        print("\n\nYour new password is")
        print(Fore.MAGENTA+new_password+Style.RESET_ALL)

#Starting area
if __name__ == "__main__":
    #clearnig and displaying logo
    _console.clrscr()
    _console.display()
    #creating object
    obj = password()
    obj.passW()
    obj.encrypt()
    obj.secondencryption()
