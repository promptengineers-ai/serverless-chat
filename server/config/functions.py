"""Functions configuration file."""

from server.utils.functions import get_word_length, get_inventory

AVAILABLE_FUNCTIONS = {
	"get_word_length": get_word_length,
 "get_inventory": get_inventory,
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
		"name": "get_inventory",
		"description": "Query Inventory for Vehicles.",
		"parameters": {
			"type": "object",
			"properties": {
				"normalTransmission": {
					"type": "string",
					"description": "Transmission type for the vehicle."
				},
				"normalBodyStyle": {
					"type": "string",
					"description": "Body style of the vehicle."
				},
				"odometer": {
					"type": "integer",
					"description": "Odometer reading of the vehicle."
				},
				"internetPrice": {
					"type": "number",
					"description": "Internet price of the vehicle."
				},
				"year": {
					"type": "integer",
					"description": "Year of manufacture of the vehicle."
				},
				"normalDriveLine": {
					"type": "string",
					"description": "Drive line type for the vehicle."
				},
				"model": {
					"type": "string",
					"description": "Model of the vehicle."
				},
				"make": {
					"type": "string",
					"description": "Make of the vehicle."
				},
				"compositeType": {
					"type": "string",
					"description": "Composite type of the vehicle."
				},
				"normalExteriorColor": {
					"type": "string",
					"description": "Exterior color of the vehicle."
				}
			}
		}
	}
]
