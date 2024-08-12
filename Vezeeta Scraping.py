# WRITTEN BY SHEHAB AHMED
# CONTACT: contact@shehap.tech
#This is the base code, Use threads to increase performance

import requests
import pandas as pd

# URL for the API endpoint
url = "https://v-gateway.vezeetaservices.com/inventory/api/V2/ProductShapes"

# List to store the product shapes data
product_shapes = []

# Loop through the pages (1 to 29979)
for page in range(1, 29980):
    # Query parameters for the API request
    querystring = {
        "query": "",
        "from": f"{page}",
        "size": "30",
        "pharmacyTypeId": "0",
        "version": "2"
    }

    # Headers for the API request
    headers = {
        "Content-Type": "",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-us",
        "brandkey": "undefined",
        "origin": "https://www.vezeeta.com",
        "priority": "u=1, i",
        "referer": "https://www.vezeeta.com/",
        "^sec-ch-ua": "^\^Google",
        "sec-ch-ua-mobile": "?0",
        "^sec-ch-ua-platform": "^\^Windows^^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    # Make the API request
    response = requests.request("GET", url, headers=headers, params=querystring)

    # Parse the JSON response
    response_json = response.json()
    print(page)  # Print the current page number

    # Append the product shapes data to the list
    for product_shape in response_json["productShapes"]:
        product_shapes.append(product_shape)

# Normalize the JSON data and convert it to a DataFrame
vezeeta_data = pd.json_normalize(product_shapes)

# Save the DataFrame to a CSV file
vezeeta_data.to_csv("Vezeeta_data_all_test4.csv", encoding='utf-8-sig')