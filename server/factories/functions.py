"""Function Service"""""
import json
import requests

from server.config.functions import AVAILABLE_FUNCTIONS

class FunctionTypeFactory:
    """Function Type Factory"""
    def get_result(self, fn_type, response_message):
        """Get Result"""
        function_args = json.loads(response_message["function_call"]["arguments"])

        if fn_type == "get_word_length":
            function_to_call = AVAILABLE_FUNCTIONS[fn_type]
            return function_to_call(
			    word=function_args.get("word"),
			)
            
        if fn_type == "get_inventory":
            function_to_call = AVAILABLE_FUNCTIONS[fn_type]
            return function_to_call(
                normalTransmission=function_args.get("normalTransmission"),
                normalBodyStyle=function_args.get("normalBodyStyle"),
                odometer=function_args.get("odometer"),
                internetPrice=function_args.get("internetPrice"),
                year=function_args.get("year"),
                normalDriveLine=function_args.get("normalDriveLine"),
                model=function_args.get("model"),
                make=function_args.get("make"),
                compositeType=function_args.get("compositeType"),
                normalExteriorColor=function_args.get("normalExteriorColor")
            )
        
        raise ValueError("Invalid Function type.")
