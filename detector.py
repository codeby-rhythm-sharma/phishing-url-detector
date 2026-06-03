import re
from urllib.parse import urlparse

import tldextract
import validators
from colorama import Fore, Style, init

from rules import (
SHORTENERS,
SUSPICIOUS_KEYWORDS,
SUSPICIOUS_TLDS,
)

init(autoreset=True)

def detect_phishing(url):
score = 0
findings = []

```
if not validators.url(url):
    findings.append("Invalid URL format")
    return score, findings

parsed = urlparse(url)
domain = parsed.netloc.lower()

ip_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"
if re.search(ip_pattern, domain):
    score += 2
    findings.append("IP-based URL detected")

if any(shortener in domain for shortener in SHORTENERS):
    score += 2
    findings.append("URL shortening service detected")

for keyword in SUSPICIOUS_KEYWORDS:
    if keyword in url.lower():
        score += 1
        findings.append(f"Suspicious keyword detected: {keyword}")

extracted = tldextract.extract(url)
subdomains = extracted.subdomain.split(".")

if len(subdomains) > 2:
    score += 2
    findings.append("Excessive subdomains detected")

for tld in SUSPICIOUS_TLDS:
    if domain.endswith(tld):
        score += 1
        findings.append(f"Suspicious TLD detected: {tld}")

if "@" in url:
    score += 2
    findings.append("@ symbol detected in URL")

return score, findings
```

def classify(score):
if score >= 6:
return "HIGH RISK"
elif score >= 3:
return "MEDIUM RISK"
return "LOW RISK"

if **name** == "**main**":
print(Fore.RED + "\nPhishing URL Threat Analyzer\n")

```
while True:
    url = input("Enter URL (or type exit): ")

    if url.lower() == "exit":
        break

    score, findings = detect_phishing(url)

    print("\nDetection Results")
    print("-" * 40)

    if findings:
        for finding in findings:
            print(Fore.YELLOW + f"[!] {finding}")

    risk = classify(score)

    if risk == "HIGH RISK":
        color = Fore.RED
    elif risk == "MEDIUM RISK":
        color = Fore.YELLOW
    else:
        color = Fore.GREEN

    print(color + f"\nRisk Level: {risk}")
    print(Style.RESET_ALL)
```
