"""Function Service"""""
import json

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
            
        if fn_type == "create_event":
            function_to_call = AVAILABLE_FUNCTIONS[fn_type]
            return function_to_call(
                title=function_args.get("title"),
                start=function_args.get("start"),
                end=function_args.get("end"),
                bgColor=function_args.get("bgColor", None),
                location=function_args.get("location", ""),
                description=function_args.get("description", "")
            )
        raise ValueError("Invalid Function type.")
