# Phone Normalizer

A simple Python command-line tool that normalizes messy, human-entered
North American phone numbers (NANP) into a consistent E.164 format.

---

## What this does

People write phone numbers in many different ways:

- 647-555-0199
- (416) 888 1234
- +1 905 555 7788

This tool:
- Cleans the input
- Normalizes it to E.164 format
- Detects NANP numbers automatically
- Optionally looks up the area code location

---

## Features

- Normalizes US/Canada (NANP) phone numbers
- Outputs E.164 format (`+16475550199`)
- Area-code → city/region lookup via JSON
- Interactive CLI (paste numbers directly)
- Clear handling of ambiguous inputs

---

## Usage

Run the CLI:

python cli.py

> 647-555-0199
✔ Valid number
E.164: +16475550199
Plan: NANP
Location: Toronto, ON (Canada)
⚠ Country code assumed (NANP)

---

## Area Code Data

Area-code location data is stored in a separate JSON file:

area_codes.json 

"604": {
  "city": "Vancouver",
  "region": "BC",
  "country": "Canada" }
  
---

## Limitations

Only supports North American phone numbers (NANP)

Area-code dataset is partial

Does not parse extensions (e.g. x204)

Does not infer country beyond NANP

These limitations are intentional to keep the tool focused and reliable.
