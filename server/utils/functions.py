import requests

def get_word_length(word: str) -> str:
    """Returns the length of a word."""
    return str(len(word))

def create_event(title, start, end, bgColor=None, location="", description=""):
    """
    Create a calendar event.

    Args:
        title (str): Title of the event.
        start (int): Start time of the event in milliseconds since the Unix epoch.
        end (int): End time of the event in milliseconds since the Unix epoch.
        bgColor (str, optional): Background color for the event. Defaults to None.
        location (str, optional): Location of the event. Defaults to an empty string.
        description (str, optional): Description of the event in Markdown. Defaults to an empty string.

    Returns:
        dict: JSON response from the API.

    Raises:
        Exception: If the API request fails.
    """
    url = "https://api.skrumify.com/api/v1/events"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer $JWT_TOKEN'
      }
    payload = {
        "title": title,
        "start": start,
        "end": end,
        "bgColor": bgColor,
        "location": location,
        "description": description
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 201:
        raise Exception(f"Error: Returned a {response.status_code} status code.")
    print(response.json())
    return str(response.json())