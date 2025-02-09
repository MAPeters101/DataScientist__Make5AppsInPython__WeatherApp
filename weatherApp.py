
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)

#Icon
image_icon = PhotoImage(file="images/logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file="images/Rounded+Rectangle+1.png")
Label(root,image=Round_box,bg='#57adff').place(x=30,y=110)

#Labels
label1 = Label(root,text="Temperature",font=("Helvetica",11),fg="white",bg='#203243')
label1.place(x=50,y=120)

mainloop()




