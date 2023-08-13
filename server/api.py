"App Entrypoint"
import logging
import openai
import os

from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates

from server.models.request import Message
from server.models.response import ResponseStatus, ResponseChat

app = FastAPI(title="🤖 Prompt Engineers AI - Serverless Chat")
os.environ.get('OPENAI_API_KEY')
templates = Jinja2Templates(directory="static")
logger = logging.getLogger("uvicorn.error")

#######################################################################
###  Pages
#######################################################################
@app.get("/", tags=["Pages"], include_in_schema=False)
async def chat_interface(request: Request):
    """Serves the index page."""
    return templates.TemplateResponse(
        "pages/index.html", 
        {"request": request, "current_page": "home"}
    )
    
#######################################################################
###  Status Endpoints
#######################################################################
@app.get("/status", tags=["Status"], response_model=ResponseStatus)
async def get_application_version():
    """Check the application status."""
    try:
        return {
			"version": os.getenv("APP_VERSION", ''),
		}
    except Exception as err:
        logger.exception(err)
        raise HTTPException(status_code=500, detail="Internal Server Error")

#######################################################################
###  API Endpoints
#######################################################################
@app.post("/chat", tags=["Chat"], response_model=ResponseChat)
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