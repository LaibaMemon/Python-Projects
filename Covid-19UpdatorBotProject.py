import requests
from win10toast import ToastNotifier
import json #its an Api that returns the Data into a json fromat
import time #library

def update():
	r=requests.get(' https://coronavirus-19-api.herokuapp.com/all')
	data=r.json()
	text=f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}' #The data that we are getting grom json it will convert to string f

	while True:
		toast=ToastNotifier()
		toast.show_toast("Covid-19 Updates",text,duration=20)
		time.sleep(60)

update()
