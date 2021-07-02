from tkinter import *
import random
import time
import datetime
  
# creating root object
root = Tk()
# defining size of window
root.geometry("1200x6000")
# setting up the title of window
root.title("Message Saviour")
  
Tops = Frame(root, width = 1400, relief = FLAT)
Tops.pack(side = TOP)
  
f1 = Frame(root, width = 800, height = 700, relief = SUNKEN)
f1.pack(side = LEFT)
  
#TIME
localtime = time.asctime(time.localtime(time.time()))
  
lblInfo = Label(Tops, font = ('Akkurat', 50, 'bold'), text = " SECRET MESSAGING ",
                     fg = "Blue", bd = 1, anchor='center',bg='white')
                       
lblInfo.grid(row = 0, column = 0)
  
lblInfo = Label(Tops, font=('arial', 20, 'bold'),text = localtime, fg = "RED", bd = 10, anchor = 'w')
                          
lblInfo.grid(row = 2, column = 0)
  
rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()
  
# To Close the application window
def qExit():
    root.destroy()
  
# Function to reset the application window
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")
  
lblReference = Label(f1, font = ('Baskerville', 16, 'bold'), text = "NAME", bd = 16, anchor = "w")
lblReference.grid(row = 0, column = 0)
  
txtReference = Entry(f1, font = ('Baskerville', 16, 'bold'), textvariable = rand, bd = 10, insertwidth = 4,
                        bg = "powder blue", justify = 'right')
                          
txtReference.grid(row = 0, column = 1)
  
lblMsg = Label(f1, font = ('Baskerville', 16, 'bold'), text = "MESSAGE", bd = 16, anchor = "w")
           
lblMsg.grid(row = 1, column = 0)
  
txtMsg = Entry(f1, font = ('Baskerville', 16, 'bold'), textvariable = Msg, bd = 10, insertwidth = 4,
                bg = "powder blue", justify = 'right')
                  
txtMsg.grid(row = 1, column = 1)
  
lblkey = Label(f1, font = ('Baskerville', 16, 'bold'), text = "KEY", bd = 16, anchor = "w")
              
lblkey.grid(row = 2, column = 0)
  
txtkey = Entry(f1, font = ('Baskerville', 16, 'bold'), textvariable = key, bd = 10, insertwidth = 4,
               bg = "powder blue", justify = 'right')
                  
txtkey.grid(row = 2, column = 1)
  
lblmode = Label(f1, font = ('Baskerville', 16, 'bold'), text = "MODE(e for encrypt, d for decrypt)",
                bd = 16, anchor = "w")
                                  
lblmode.grid(row = 3, column = 0)
  
txtmode = Entry(f1, font = ('Baskerville', 16, 'bold'), textvariable = mode, bd = 10, insertwidth = 4,
                  bg = "powder blue", justify = 'right')
                    
txtmode.grid(row = 3, column = 1)
  
lblService = Label(f1, font = ('Baskerville', 16, 'bold'), text = "RESULT", bd = 16, anchor = "w")
               
lblService.grid(row = 2, column = 2)
  
txtService = Entry(f1, font = ('Baskerville', 16, 'bold'), textvariable = Result, bd = 10, insertwidth = 4,
                       bg = "powder blue", justify = 'right')
                         
txtService.grid(row = 2, column = 3)
  
""" Background Computation Starts """

import base64
# Function to encrypt
def encode(key, clear):
    enc = []
      
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
  
# Function to decrypt
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
  
def Enc_Dec():
    print("Message= ", (Msg.get()))
  
    clear = Msg.get()
    k = key.get()
    m = mode.get()
  
    if (m == 'e'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))
  
# ENC/DEC button
btnShow = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black",
                  font = ('Alegreya', 16, 'bold'), width = 10,
                  text = "ENC/DEC", bg = "RED",
                  command = Enc_Dec).grid(row = 8, column = 1)
  
# Reset button
btnReset = Button(f1, padx = 16, pady = 8, bd = 16,
                  fg = "white", font = ('Merriweather', 16, 'bold'),
                    width = 10, text = "RESET", bg = "GREEN",
                   command = Reset).grid(row = 8, column = 2)
  
# Exit button
btnExit = Button(f1, padx = 16, pady = 8, bd = 16, 
                 fg = "white", font = ('arvo', 16, 'bold'),
                      width = 10, text = "CLOSE", bg = "BLUE",
                  command = qExit).grid(row = 8, column = 3)
  
#To keep the application window alive
root.mainloop()
