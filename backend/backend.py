from fastapi import FastAPI
from fastapi.exceptions import HTTPException
import random
from datetime import datetime
import requests




app = FastAPI()
KEY = "5e471357596d2ab9ec8df2d7b11c4ba8"


@app.get("/")
def Main():
    return "Welcome Dmytro, can you give me 5 stars please!!!!!"


@app.get("/random")
def Random_numb(random_max:int=1000000000000000000000000000000000000000000000000000000):
    if random_max > 0:
        return random.randint(1, random_max)
    else:
        raise HTTPException(status_code=400, detail="Invalid Argument")

@app.get("/current_time")
def Current_time():
    return datetime.now()

@app.post("/weather/{city}")
def Weather_w(city):
    try:
        app = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric"
        response = requests.get(app)
        data = response.json()
        weather = data["main"]
        temp = weather["temp"]
        feels = weather["feels_like"]
        humidity = weather["humidity"]
        main = data["weather"][0]["main"]
        descr = "No Information" if data["weather"][0]["description"] == 0 else data["weather"][0]["description"]
        wind = data["wind"]["speed"]
        Weather_data = {"city" : city, "temp" : temp, "feels" : feels, "descr":descr, "humidity" : humidity, "wind" : wind, "main":main}
        return Weather_data
    except:
        raise HTTPException(status_code=400, detail='Invalid Argument')      



