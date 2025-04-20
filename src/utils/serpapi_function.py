from serpapi import GoogleSearch

def get_events_for_artist(artist_name, api_key):
    """
    Args:
        artist_name (str): The name of the artist to search for.
        api_key (str): Your SerpAPI key.
    Returns:
        list: A list of events for the specified artist.
    """
    params = {
        "api_key": {api_key},
        "engine": "google_events",
        "q": {artist_name},
        "hl": "en",
        "gl": "us",
        "htichips": "concerts"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    events = results.get("events_results", [])
    # drop 2 last columns from list
    for event in events:
        event.pop("thumbnail", None)
        event.pop("image", None)
        event.pop("event_location_map", None)

    events_str = "\n\n\nEVENT\n".join(
        "\n".join(f"{key}: {value}" for key, value in event.items()) for event in events[:3]
        )
    return events_str