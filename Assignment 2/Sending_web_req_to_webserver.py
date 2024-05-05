import requests

def send_http_request(url, method='GET', headers=None, params=None, data=None):
    try:
        response = requests.request(method, url, headers=headers, params=params, data=data)
        response.raise_for_status()  # Raise an exception if the request was not successful
        return response.text  # Return the response content
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Example usage
url = "https://www.example.com"
response_text = send_http_request(url)
print(response_text)
