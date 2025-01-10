from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests

app = FastAPI()

# Define the message structure
class Message(BaseModel):
    text: str

# Trefle API setup (replace with your actual API key)
TREFLE_API_KEY = "ryrrPrjPYWnHVjWRl5W5eqhsC8DagB3mhb6cDhChTbI"  # Replace with your Trefle API key
TREFLE_API_URL = "https://trefle.io/api/v1/plants"

# Function to get plant suggestions based on season
def get_plant_suggestions(season):
    headers = {
        "Authorization": f"Bearer {TREFLE_API_KEY}"
    }
    
    # Example: Fetch plants based on season (you can extend this logic)
    if season == "summer":
        params = {"filter[q]": "summer"}  # Modify based on Trefle API filtering options
    elif season == "winter":
        params = {"filter[q]": "winter"}
    else:
        return "I don't have data for that season."
    
    # Request data from Trefle API
    response = requests.get(TREFLE_API_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        plants = [plant["common_name"] for plant in data["data"][:5]]  # Limit to top 5 plants
        return f"The best plants for {season} are: " + ", ".join(plants)
    else:
        return "Sorry, I couldn't fetch plant data at the moment."

# Serve the HTML frontend
@app.get("/", response_class=HTMLResponse)
async def get_html():
    with open("index.html", "r") as file:
        return file.read()

# Define the chatbot endpoint
@app.post("/chatbot")
async def chatbot(message: Message):
    user_message = message.text.lower()

    # Bot logic based on season in the message
    if "summer" in user_message:
        response = get_plant_suggestions("summer")
    elif "winter" in user_message:
        response = get_plant_suggestions("winter")
    else:
        response = "Hello! What can I help you with regarding plants today?"

    return {"response": response}
