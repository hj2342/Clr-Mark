from pathlib import Path
from openai import OpenAI
from api import generate_content

client = OpenAI(api_key=API_KEY)
def generate_gif(topic):
    params = {
        "api_key": GIPHY_API_KEY,
        "q": topic,
        "limit": 1,
        "offset": 0,
        "rating": "g",
        "lang": "en"
    }

    response = requests.get(URL, params=params)
    data = response.json()
    return data["data"][0]["images"]['downsized_large']['url'] if data["data"] else None

def text_to_speech(text, speech_file_path = "sample.mp3"):
    response = client.audio.speech.create(
      model="tts-1",
      voice="alloy",
      input=text
    )
    response.stream_to_file(speech_file_path)

