from tkinter import Tk , ttk
from tkinter import *
from PIL import Image, ImageTk
import requests
import json


c1 = "white"
c2 = "black"
c3 = "orange"

window = Tk()
photo = PhotoImage(file = "cur.png")
window.iconphoto(False, photo)
window.geometry("300x320")
window.title("CurrencyConverter")
window.configure(bg = c1)
window.resizable(width = False, height=False)

# tf
top = Frame(window , width = 300 , height = 60 , bg = c3)
top.grid(row = 0, column = 1)
# bf
bottom = Frame(window , width = 300 , height = 260 , bg = c1)
bottom.grid(row = 1, column = 1)
# tf
icon = Image.open('cur.png')
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
app= Label(top , image = icon , compound = LEFT , text = "Curr_Converter" , height = 5 , padx = 13 , pady = 30 , anchor = CENTER , font = ('ivy 15'),bg = c3,fg = "red")
app.place(x = 50,y = 5)
# convert
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency1 = com1.get()
    currency2 = com2.get()
    amount = value.get()
    querystring = {"from":currency1,"to":currency2,"amount":amount}
    if currency2 =="USD":
        symbol = "$"
    elif currency2 =="INR":
        symbol = "₹"
    elif currency2 =="EUR":
        symbol = "€"
    elif currency2 =="BRL":
        symbol = "R$"
    elif currency2 =="CAD":
        symbol = "C$"
    headers = {
	    "X-RapidAPI-Key": "174d598005msh56d898ff6d6ba6dp146f54jsne7c0b2d7c917",
	    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data =json.loads(response.text)
    converted = data["result"]["convertedAmount"]
    formated = symbol +"{: ,.2f}".format(converted)
    op_label['text'] = formated
    print(converted, formated)
# tf
op_label = Label(bottom  ,  text = " " ,relief = "solid", width  = 16 , height = 2, pady = 0 , anchor = CENTER, font = ('ivy 15'),bg =c1 )
op_label.place(x = 50, y = 9)
currency = ['CAD', 'BRL' , 'EUR','INR','USD']
from_label = Label(bottom  ,  text = "From " ,relief = "flat", width  =8, height = 1, pady = 0 , anchor = NW , font = ('ivy 12 bold'),bg =c1 )
from_label.place(x = 50,y = 98)
com1 = ttk.Combobox(bottom , width = 10 , justify = CENTER , font=("arial 10") )
com1['values'] = (currency)
com1.place(x=50, y=118)
# bottom bg

to_label = Label(bottom  ,  text = "To " ,relief = "flat", width  =8, height = 1, pady = 0 , anchor = NW , font = ('ivy 12 bold'),bg =c1 )
to_label.place(x =200,y = 98)
com2 = ttk.Combobox(bottom , width = 10 , justify = CENTER , font=("arial 10") )
com2['values'] = (currency)
com2.place(x=197, y=118)
value = Entry(bottom , width = 26 , justify = CENTER , font=("ivy 12 bold"),relief =SOLID )
value.place(x = 50 , y = 155)
button = Button(bottom , text = "convert it" , width = 22, padx = 5 , height=1, bg = "purple" , fg=c1, font = ("Ivy 12 bold") , relief=SOLID, command = convert)
button.place(x =50, y=200)
window.mainloop()
