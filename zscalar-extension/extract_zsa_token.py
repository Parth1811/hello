import sys
import os
import urllib.parse
from urllib.parse import urlparse, parse_qs

def extract_and_print(full_url):
    """
    Extracts query parameters from a URL and constructs a custom protocol URL.
    Only prints output without opening browser.
    
    Args:
        full_url: The complete URL with query parameters
    """
    # Parse the URL
    parsed_url = urlparse(full_url)
    
    # Extract the query string (everything after '?')
    query_string = parsed_url.query
    
    # Construct the custom protocol URL
    if query_string:
        custom_url = f"zsa://token?{query_string}"
    else:
        custom_url = "zsa://token"
    
    return custom_url

# Example usage
if __name__ == "__main__":
    # Your URL
    url = sys.argv[1]
    
    # Extract and print only
    custom_url = extract_and_print(url)
    print(f"Opening Zscaler with token: {custom_url[21:31]}...")
    os.system(f'open -a "Microsoft Edge" --args "file://mac/Home/Documents/open_zscalar.html?url={custom_url}"')
    