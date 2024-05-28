from flask import Flask, render_template, request, url_for, flash, redirect
from requests import get, Response


app= Flask(__name__)

BACKEND_URL = "http://backend:8000"


@app.get("/random")
def random_get(random_max:int=100):
    response = get(f"{BACKEND_URL}/random/")
    if response.status_code == 200:
        print(response)
        return render_template("main.html", **response)
    return(f"Error {response.status_code}")

@app.get("/current_date")
def current_date():
    response = get(f"{BACKEND_URL}/current_time")
    if response.status_code == 200:
        return render_template("main.html", **response)
    return(f"Error {response.status_code}")
        
@app.get("/weather/<city>")
def get_weather(city:str):
    response = get(f"{BACKEND_URL}/weather/{city}")
    if response.status_code == 200:
        return render_template("weather.html", **response)
    return(f"Error {response.status_code}")