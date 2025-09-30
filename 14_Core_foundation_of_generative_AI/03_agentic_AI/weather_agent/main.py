from google import genai
import requests



def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code==200:
        return f"Weather in {city} is {response.text}"
    return f"Something went wrong"


client = genai.Client(api_key="AIzaSyBhAWFpLzjiZgrPOWAcFSxz7f9adTqF9PM")

response = client.models.generate_content(
    model="gemini-2.5-flash",contents="what is the current temperature of mumbai right now?"
)


print(get_weather("Pune"))