from tkinter import *
from PIL import ImageTk,Image
import requests
import json

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

key="38cfca025d0b0175d4fdb12591ce1640"
cityname=input("enter city name: ")
main=Tk()
main.title('WEATHER REPORT')
main.iconbitmap('th.ico')
main.geometry("480x320")
try:
    api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+cityname +"&appid="+key)
    api=json.loads(api_request.content)

except Exception as E:
    api='ERROR....'


city_check=Entry(main)
city_check.get(cityname)



label=Label(main).pack()    







main.mainloop()