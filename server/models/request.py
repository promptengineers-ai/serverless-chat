from typing import Any, Optional
from pydantic import BaseModel, Field

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