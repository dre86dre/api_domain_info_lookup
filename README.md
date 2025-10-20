# API Domain Info Lookup

A simple Python script to fetch **domain information** using a public API.

---

## Features

- Fetch WHOIS data for any domain name
- Cleanly formatted JSON output
- Interactive terminal input

---

## Requirements

- [Python 3](https://www.python.org/) (v3.6 or higher recommended)
- [requests](https://pypi.org/project/requests/) library

You can install the required [requests](https://pypi.org/project/requests/) package with:

```
pip install requests
```

## API Key Setup

This script uses [WhoisXML API](https://whois.whoisxmlapi.com/) as an example.
You’ll need a **free API key** to use the service.
1. Go to [WhoisXML API](https://whois.whoisxmlapi.com/).
2. Sign up for a free account.
3. Copy your API key.
4. Replace the line in the script:
```
API_KEY = "YOUR_API_KEY"
```
with your actual key:
```
API_KEY = "your-real-api-key-here"
```

---

## How To Use

1. Clone this repository:
```
git clone https://github.com/dre86dre/api_domain_info_lookup.git
```
2. Navigate to the folder:
```
cd api_domain_info_lookup
```
3. Run the script:
```
python api_domain_info_lookup.py
```
4. Enter a domain name when prompted (e.g. ```example.com```).
