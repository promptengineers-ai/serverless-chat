"""Functions configuration file."""

from server.utils.functions import get_word_length, create_event

AVAILABLE_FUNCTIONS = {
	"get_word_length": get_word_length,
	"create_event": create_event
}

FUNCTIONS = [
	{
		"name": "get_word_length",
		"description": "Returns the length of a word.",
		"parameters": {
			"type": "object",
			"properties": {
				"word": {
					"type": "string",
					"description": "The word whose length needs to be determined."
				}
			},
			"required": ["word"]
		}
	},
	{
		"name": "create_event",
		"description": "Create a calendar event.",
		"parameters": {
			"type": "object",
			"properties": {
				"title": {
					"type": "string",
					"description": "Title of the event."
				},
				"start": {
					"type": "integer",
					"description": "Start time of the event in milliseconds since the Unix epoch."
				},
				"end": {
					"type": "integer",
					"description": "End time of the event in milliseconds since the Unix epoch."
				},
				"bgColor": {
					"type": "string",
					"description": "Background color for the event. Optional, default is None.",
					"default": None
				},
				"location": {
					"type": "string",
					"description": "Location of the event. Optional, default is an empty string.",
					"default": ""
				},
				"description": {
					"type": "string",
					"description": "Description of the event in Markdown. Optional, default is an empty string.",
					"default": ""
				}
			},
			"required": ["title", "start", "end"]
		}
	}
]
