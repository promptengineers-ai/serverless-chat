"App Entrypoint"
import logging
import openai
import json
import os

from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates

from server.models.request import ReqBodyChat, ReqBodyFunctionChat
from server.models.response import ResponseStatus, ResponseChat, ResponseChatStream
from server.services.message_service import send_openai_message, send_openai_message_stream, send_functions_message
from server.utils import logger

app = FastAPI(title="🤖 Prompt Engineers AI - Serverless Chat")
openai.api_key = os.environ.get('OPENAI_API_KEY')
templates = Jinja2Templates(directory="static")
logger = logging.getLogger("uvicorn.error")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:9000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
# #######################################################################
@app.post("/chat", tags=["Chat"], response_model=ResponseChat)
async def chat(body: ReqBodyChat):
    try:
        result = send_openai_message(
            model=body.model,
            messages=body.messages,
            temperature=body.temperature
        )
        logger.debug('[POST /chat] Response: %s', str(result))
        data = json.dumps({
            'chat': result
        })
        return Response(
            content=data,
            media_type='application/json',
            status_code=200
        )
    except HTTPException as err:
        logger.error(err.detail)
        raise
    except Exception as err:
        logger.error(err)
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred. {str(err)}"
        )
        
#######################################################################
###  API Endpoints
#######################################################################
@app.post("/chat/stream", tags=["Chat"], response_model=ResponseChatStream)
def chat_stream(body: ReqBodyChat):
    """Chat endpoint."""
    messages = body.messages or []
    logger.debug('[POST /chat/stream] Query: %s', str(body))
    return StreamingResponse(
        send_openai_message_stream(
            messages,
            body.model,
            body.temperature,
            True
        ),
        media_type="text/event-stream"
    )
    
#######################################################################
###  API Endpoints
#######################################################################
@app.post("/chat/stream/functions", tags=["Chat"], response_model=ResponseChatStream)
def chat_functions_stream(body: ReqBodyFunctionChat):
    """Chat endpoint."""
    logger.debug('[POST /chat/stream/functions] Query: %s', str(body))
    return StreamingResponse(
        send_functions_message(
            body.messages,
            body.model,
            body.temperature,
            body.functions,
        ),
        media_type="text/event-stream"
    )