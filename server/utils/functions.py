import requests

from server.config import CAR_DEALER_API

def get_word_length(word: str) -> str:
    """Returns the length of a word."""
    return str(len(word))

def get_inventory(
    normalTransmission=None,
    normalBodyStyle=None,
    odometer=None,
    internetPrice=None,
    year=None,
    normalDriveLine=None,
    model=None,
    make=None,
    compositeType=None,
    normalExteriorColor=None
):
    """Query Inventory for Vehicles."""
    # Create a dictionary with only the parameters that have values
    params = {k: v for k, v in locals().items() if v is not None and k != "CAR_DEALER_API"}
    response = requests.get(CAR_DEALER_API, params=params)
    data = response.json()

    return str(data)