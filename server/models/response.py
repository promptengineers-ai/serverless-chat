from typing import Any, Optional, List
from pydantic import BaseModel, Field


class ResponseStatus(BaseModel):
    version: str = Field(default='v0.0.15')
    
#################################################
## ChatGPT
#################################################

class ResponseChat(BaseModel):
    # data: ChatCompletion
    
	class Config: # pylint: disable=too-few-public-methods
		"""A message to send to the chatbot."""
		json_schema_extra = {
			"example": {
				"chat": {
					"id": "chatcmpl-7myaL...",
					"object": "chat.completion",
					"created": 1691906989,
					"model": "gpt-3.5-turbo-0613",
					"choices": [
						{
							"index": 0,
							"message": {
								"role": "assistant",
								"content": "The Arizona Diamondbacks had Randy Johnson and Curt Schilling as their primary pitchers during the 2001 World Series. Both pitchers had exceptional performances throughout the series."
							},
							"finish_reason": "stop"
						}
					],
					"usage": {
						"prompt_tokens": 52,
						"completion_tokens": 32,
						"total_tokens": 84
					}
				}
			}
		}


class ResponseChatStream(BaseModel):
    sender: str = Field(default='assistant')
    message: str = Field(default='Dialog started.')
    type: str = Field(default='stream')