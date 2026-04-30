from lxml import etree

# Root structure
envelope = etree.Element("ENVELOPE")

# Header
header = etree.SubElement(envelope, "HEADER")
etree.SubElement(header, "TALLYREQUEST").text = "Import Data"

# Body
body = etree.SubElement(envelope, "BODY")
import_data = etree.SubElement(body, "IMPORTDATA")

# Request Description
request_desc = etree.SubElement(import_data, "REQUESTDESC")
etree.SubElement(request_desc, "REPORTNAME").text = "Vouchers"

# Request Data
request_data = etree.SubElement(import_data, "REQUESTDATA")
tally_message = etree.SubElement(request_data, "TALLYMESSAGE")

# =========================
# VOUCHER START
# =========================

voucher = etree.SubElement(
    tally_message,
    "VOUCHER",
    VCHTYPE="Sales",
    ACTION="Create"
)

# IMPORTANT: BOTH dates required
etree.SubElement(voucher, "DATE").text = "20260405"
etree.SubElement(voucher, "VCHDATE").text = "20260405"

etree.SubElement(voucher, "VOUCHERNUMBER").text = "1"
etree.SubElement(voucher, "PARTYLEDGERNAME").text = "XYZ Enterprises"
etree.SubElement(voucher, "NARRATION").text = "Test Invoice"

# Party Entry (Debit)
ledger1 = etree.SubElement(voucher, "ALLLEDGERENTRIES.LIST")
etree.SubElement(ledger1, "LEDGERNAME").text = "XYZ Enterprises"
etree.SubElement(ledger1, "ISDEEMEDPOSITIVE").text = "Yes"
etree.SubElement(ledger1, "AMOUNT").text = "-1000"

# Sales Entry (Credit)
ledger2 = etree.SubElement(voucher, "ALLLEDGERENTRIES.LIST")
etree.SubElement(ledger2, "LEDGERNAME").text = "Sales"
etree.SubElement(ledger2, "ISDEEMEDPOSITIVE").text = "No"
etree.SubElement(ledger2, "AMOUNT").text = "1000"

# =========================
# SAVE FILE
# =========================

tree = etree.ElementTree(envelope)

with open("invoice.xml", "wb") as f:
    tree.write(f, pretty_print=True, xml_declaration=True, encoding="utf-8")

print("✅ XML file 'invoice.xml' created successfully!")