from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from typing import Any, Optional
from pydantic import BaseModel, Field

import openai
import os

app = FastAPI()
os.environ.get('OPENAI_API_KEY')

#######################################################################
###  Pages
#######################################################################
@app.get("/", tags=["Pages"])
async def chat_interface(request: Request):
    html_content = """
    <html>
    <head>
        <title>My HTML Page</title>
    </head>
    <body>
        <h1>Welcome to my HTML page!</h1>
        <p>This is the content of my HTML page.</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

#################################################
## ChatGPT
#################################################
class Message(BaseModel): # pylint: disable=too-few-public-methods
    """A message to send to the chatbot."""
    model: Optional[str] = None
    messages: Optional[Any] = None
    temperature: Optional[float or int] = None

    class Config: # pylint: disable=too-few-public-methods
        """A message to send to the chatbot."""
        json_schema_extra = {
            "example": {
    			"model": "gpt-3.5-turbo",
       		 	"temperature": 0.8,	
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": 'Who won the 2001 world series?'},
					{"role": "assistant", "content": 'The arizona diamondbacks won the 2001 world series.'},
                    {"role": "user", "content": 'Who were the pitchers?'},
                ]
            }
        }

@app.post("/chat", tags=["Chat"])
async def chat_endpoint(body: Message):
    try:
        result = openai.ChatCompletion.create(
            model=body.model,
            messages=body.messages,
            temperature=body.temperature
        )
        
        return { 
            "data": result
        }
    except Exception as e:
        return { 
            "error": str(e)
        }