import re

def extract_fields(text):
    data = {}

    # Invoice Number
    inv = re.search(r'Invoice\s*Number[:\-]?\s*(\S+)', text)
    data["invoice_no"] = inv.group(1) if inv else None

    # Date
    date = re.search(r'Date[:\-]?\s*(\d{2}[-/]\d{2}[-/]\d{4})', text)
    data["date"] = date.group(1) if date else None

    # Total Amount
    total = re.search(r'Total\s*Amount[:\-]?\s*(\d+)', text)
    data["total"] = total.group(1) if total else None

    return data


# 🔥 TEST
if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        text = f.read()

    data = extract_fields(text)

    print("\n===== EXTRACTED DATA =====\n")
    print(data)