import json
import logging

logger = logging.getLogger("uvicorn.error")

def token_stream(token: str):
    """ Use server-sent-events to stream the response"""
    data = {
      'sender': 'assistant',
      'message': token,
      'type': 'stream'
    }
    logger.debug('[POST /chat] Stream: %s', str(data))
    return f"data: {json.dumps(data)}\n\n"


def end_stream():
    """Send the end of the stream"""
    end_content = {
    	'sender': 'assistant',
    	'message': "",
    	'type': 'end'
    }
    logger.debug('[POST /chat] End: %s', str(end_content))
    return f"data: {json.dumps(end_content)}\n\n"

def retrieve_system_message(messages):
    """Retrieve the system message"""
    try:
        return list(
			filter(lambda message: message['role'] == 'system', messages)
    	)[0]['content']
    except IndexError:
        return None

def retrieve_chat_messages(messages):
    """Retrieve the chat messages"""
    return [
        (msg["content"]) for msg in messages if msg["role"] in ["user", "assistant"]
    ]