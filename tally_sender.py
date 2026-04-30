import requests

def send_to_tally(xml_file):
    url = "http://localhost:9000"
    
    with open(xml_file, "r") as f:
        xml_data = f.read()

    headers = {"Content-Type": "application/xml"}

    response = requests.post(url, data=xml_data, headers=headers)

    print("Status:", response.status_code)
    print("Response:", response.text)


# 🔥 TEST
if __name__ == "__main__":
    send_to_tally("invoice.xml")