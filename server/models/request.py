from typing import Any, Optional
from pydantic import BaseModel, Field

#################################################
## ChatGPT
#################################################
class ReqBodyChat(BaseModel): # pylint: disable=too-few-public-methods
    """A message to send to the chatbot."""
    model: str = 'gpt-3.5-turbo'
    messages: Any = []
    temperature: float or int = 0.0

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