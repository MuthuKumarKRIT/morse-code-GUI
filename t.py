from tkinter import *
from tkinter import messagebox

root = Tk()

variable1 = StringVar(root) 
variable2 = StringVar(root) 


variable1.set("Select-(Language code)") 
variable2.set("Select-(Language code)") 

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 

                    'C':'-.-.', 'D':'-..', 'E':'.', 

                    'F':'..-.', 'G':'--.', 'H':'....', 

                    'I':'..', 'J':'.---', 'K':'-.-', 

                    'L':'.-..', 'M':'--', 'N':'-.', 

                    'O':'---', 'P':'.--.', 'Q':'--.-', 

                    'R':'.-.', 'S':'...', 'T':'-', 

                    'U':'..-', 'V':'...-', 'W':'.--', 

                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 

                    '1':'.----', '2':'..---', '3':'...--', 

                    '4':'....-', '5':'.....', '6':'-....', 

                    '7':'--...', '8':'---..', '9':'----.', 

                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 

                    '?':'..--..', '/':'-..-.', '-':'-....-', 

                    '(':'-.--.', ')':'-.--.-'}

def clear():
    language1_field.delete(1.0,END)

def clear_all() :
    language1_field.delete(1.0, END)
    language2_field.delete(1.0, END)

def encrypt(m):
    cipher_text = '' 
    for letter in m:
        if letter != ' ':
            cipher_text+= MORSE_CODE_DICT[letter] + ' '
        else:
            cipher_text+= ' '
    return cipher_text

def decrypt(m): 
    m += ' '
    decipher_text = '' 
    citext = ''
    for letter in m:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher_text+= ' '
            else:
                decipher_text+= list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT .values()).index(citext)]
                citext = ''
    return decipher_text

def convert() :
    m = language1_field.get("1.0", "end")[:-1]
    if variable1.get() == variable2.get():
        messagebox.showwarning("Warning","Can't perform with same Language")
        messagebox.showinfo("Tip","Try with other choice of language code")
        return
    elif variable1.get() == "Text" and variable2.get() == "Morse code":
        try:
            rslt = encrypt(m.upper())
        except:
            messagebox.showwarning("Warning","Check your input")
            rslt=""
    elif variable1.get() == "Morse code" and variable2.get() == "Text":
        try:
            rslt=decrypt(m)
        except:
            messagebox.showwarning("Warning","Check your input")
            rslt=""
    else :
        messagebox.showerror("Error","Error occurs!!!")
        messagebox.showinfo("Tip","Check your choices...")
        return
    language2_field.insert('end -1 chars', rslt)

if __name__ == "__main__" :

    root.configure(background = 'light blue')
    root.geometry("3840x2160")  
    root.title("Code Translator")
    headlabel = Label(root, text = 'Morse Code Translator',fg = 'black', bg = "Pink",font="castellar 26")  
    headlabel.grid(row = 0, column = 1)  


    language1_field = Text(root.geometry("1080x720"), height = 10, width = 100, font = "calibri 15") 

    language2_field = Text(root.geometry("1080x720"), height = 10, width = 100, font = "calibri 15")

    language1_field.grid(row = 2, column = 1, padx = 10)  

    language2_field.grid(row = 6, column = 1, padx = 10) 


languageCode_list = ["Text", "Morse code","Select-(Language code)"] 


FromLanguage_option = OptionMenu(root, variable1, *languageCode_list) 

ToLanguage_option = OptionMenu(root, variable2, *languageCode_list) 


FromLanguage_option.grid(row = 1, column = 1, ipadx = 10) 

ToLanguage_option.grid(row = 4, column = 1, ipadx = 10) 


button1 = Button(root, text = "Clear", bg = "red", fg = "black", command = clear,font="arial 16") 
button1.grid(row=2, column=2)

button2 = Button(root, text = "Convert", bg = "blue", fg = "black", command = convert,font="arial 16") 
button2.grid(row = 6, column = 2)

button3 = Button(root,text="Clear All",bg="red",fg="black",command=clear_all)
button3.grid(row = 7, column = 1)





