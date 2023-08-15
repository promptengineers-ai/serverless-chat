import openai
from typing import AsyncIterable

from fastapi import HTTPException, Response

from server.utils import logger, token_stream, end_stream


#######################################################
## Open AI Chat GPT
#######################################################
def send_openai_message(
    messages,
    model:str,
    temperature: float or int = 0.0,
    stream: bool = False,
) -> AsyncIterable[str]:
    """Send a message to the chatbot and yield the response."""
    response = openai.ChatCompletion.create(
		model=model,
		messages=messages,
		temperature=temperature,
		stream=stream
    )
    return response
    
#######################################################
## Open AI Chat GPT
#######################################################
async def send_openai_message_stream(
    messages,
    model:str,
    temperature: float or int = 0.0,
    stream: bool = True,
) -> AsyncIterable[str]:
    """Send a message to the chatbot and yield the response."""
    response = openai.ChatCompletion.create(
      model=model,
      messages=messages,
      temperature=temperature,
      stream=stream
    )
    logger.debug('[POST /chat/stream] Stream: %s', str(response))
    for chunk in response:
        ## Would also consider gathering data here
        token = chunk['choices'][0]['delta'].get('content', '')
        yield token_stream(token)
    yield end_stream()