import requests

url = "http://127.0.0.1:8000/sum"

payload = {
    "number1": 5.0,
    "number2": 7.0
}

try:
    response = requests.post(url, json=payload)
    response.raise_for_status()  # Raises HTTPError for 4xx/5xx

    data = response.json()
    print("Sum:", data.get("result"))

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
except ValueError:
    print("Response was not valid JSON")
