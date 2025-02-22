import openai
import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Get OpenAI API Key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client (NEW way)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Define request model
class VoiceInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Voice Assistant API!"}

@app.post("/process_voice")
async def process_voice(input_data: VoiceInput):
    try:
        # Send user input to OpenAI API (NEW way)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": input_data.text}]
        )

        # Extract AI response (NEW format)
        ai_message = response.choices[0].message.content

        return {"response": ai_message}

    except Exception as e:
        return {"error": str(e)}
