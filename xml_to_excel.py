import xml.etree.ElementTree as ET
import pandas as pd

# Load XML file
tree = ET.parse("invoice.xml")
root = tree.getroot()

data = []

# Loop through vouchers
for voucher in root.findall(".//VOUCHER"):
    date = voucher.findtext("DATE")
    narration = voucher.findtext("NARRATION")

    for entry in voucher.findall(".//ALLLEDGERENTRIES.LIST"):
        ledger = entry.findtext("LEDGERNAME")
        amount = entry.findtext("AMOUNT")

        data.append({
            "Date": date,
            "Ledger": ledger,
            "Amount": amount,
            "Narration": narration
        })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("output.xlsx", index=False)

print("✅ Excel file created successfully!")