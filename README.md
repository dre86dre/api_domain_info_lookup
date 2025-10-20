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

---

## Example Output

```
Enter a domain name (e.g. example.com): example.com

✅ Domain Information:

{
    "WhoisRecord": {
        "domainName": "example.com",
        "createdDate": "1995-08-14T04:00:00Z",
        "updatedDate": "2022-07-02T08:21:44Z",
        "registrarName": "Internet Assigned Numbers Authority",
        "status": "active",
        "nameServers": {
            "rawText": "a.iana-servers.net\nb.iana-servers.net",
            "hostNames": ["a.iana-servers.net", "b.iana-servers.net"]
        }
    }
}
```

---

## Notes

- Do not include http:// or https:// in the domain name.
  - ✅ example.com
  - ❌ https://example.com
- If the API key is invalid or rate limits are reached, the script will display an error message.

---

## License

This project is licensed under the [MIT License](https://github.com/dre86dre/api_domain_info_lookup/blob/main/LICENSE).
