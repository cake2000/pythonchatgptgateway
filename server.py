from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from openai import OpenAI
import uvicorn


# Initialize FastAPI app
app = FastAPI()

# Initialize OpenAI client with a fixed API key
# Note: In production, set the API key via environment variables (e.g., os.environ["OPENAI_API_KEY"])
client = OpenAI(api_key="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")

# Define data models
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    model: str = "gpt-4o"

# Chat endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Define the system message to enforce K-12 appropriateness
        system_message = {
            "role": "system",
            "content": "Make sure your responses are appropriate for K-12 schools, and reject any inappropriate requests."
        }
        # Prepend the system message to the client's messages
        messages = [system_message] + [msg.dict() for msg in request.messages]
        
        # Call the OpenAI API
        completion = client.chat.completions.create(
            model=request.model,
            messages=messages
        )
        assistant_message = completion.choices[0].message
        return {"role": assistant_message.role, "content": assistant_message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)