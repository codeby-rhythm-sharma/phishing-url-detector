<div align="center">

# Phishing URL Detector

### Lightweight URL Threat Analysis Framework for Phishing Detection & Web Security Research

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=21&pause=2600&color=FF4D4D&center=true&vCenter=true&width=950&lines=Phishing+URL+Threat+Analysis;Heuristic-Based+URL+Inspection;Web+Security+%7C+Threat+Detection;Suspicious+Domain+Analysis;Built+for+Cybersecurity+Learning" />

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Cybersecurity](https://img.shields.io/badge/Web-Security-FF4D4D?style=for-the-badge)
![Threat Analysis](https://img.shields.io/badge/Threat-Detection-black?style=for-the-badge)
![MIT License](https://img.shields.io/badge/License-MIT-1E1E1E?style=for-the-badge)

</div>

---

# Overview

Phishing URL Detector is a lightweight cybersecurity-focused threat analysis framework designed to identify potentially malicious and phishing-oriented URLs using heuristic-based security inspection techniques.

The project analyzes suspicious URL characteristics including malicious keywords, URL shorteners, IP-based URLs, excessive subdomains, suspicious top-level domains (TLDs), and deceptive URL structures commonly associated with phishing campaigns and social-engineering attacks.

Designed as an educational web-security project, the framework demonstrates how lightweight detection workflows can be implemented for basic phishing analysis and suspicious-link identification.

---

# Threat Detection Highlights

| Capability                  | Detection Logic                     |
| --------------------------- | ----------------------------------- |
| Suspicious Keyword Analysis | Detects phishing-oriented keywords  |
| URL Shortener Detection     | Identifies shortened/masked URLs    |
| IP-Based URL Detection      | Flags direct IP-address usage       |
| Suspicious TLD Analysis     | Detects high-risk domain extensions |
| Subdomain Inspection        | Detects excessive nested subdomains |
| URL Structure Validation    | Identifies deceptive URL patterns   |

---

# Detection Workflow

<div align="center">

```text
User URL
   ↓
URL Validation
   ↓
Threat Indicator Analysis
   ↓
Heuristic Scoring Engine
   ↓
Risk Classification
   ↓
Threat Assessment Output
```

</div>

---

# Core Detection Mechanisms

## Suspicious Keyword Analysis

The detector identifies phishing-oriented keywords commonly used in credential-harvesting campaigns and social-engineering attacks.

Examples include:

* login
* verify
* secure
* update
* confirm
* banking
* password

---

## URL Shortener Detection

The framework detects shortened URLs that may conceal malicious destinations or deceptive redirect chains.

Supported checks include:

* bit.ly
* tinyurl
* goo.gl
* ow.ly
* t.co

---

## IP-Based URL Detection

Direct IP-address URLs are analyzed as potential phishing indicators because attackers frequently bypass legitimate domain registration workflows using raw IP addresses.

Example:

```text
http://192.168.1.1/login
```

---

## Suspicious TLD Inspection

The detector flags high-risk or frequently abused top-level domains often associated with phishing infrastructure and disposable malicious websites.

Examples include:

* .tk
* .xyz
* .top
* .ml
* .gq

---

## Subdomain Analysis

The framework identifies excessive nested subdomains commonly used to impersonate legitimate services and create deceptive URL structures.

Example:

```text
secure.login.verify.paypal.account.example.com
```

---

# Risk Classification System

| Risk Score | Classification |
| ---------- | -------------- |
| 0 – 2      | LOW RISK       |
| 3 – 5      | MEDIUM RISK    |
| 6+         | HIGH RISK      |

The final threat level is determined using heuristic scoring based on detected indicators.

---

# Example Detection Output

```text
Enter URL:
https://bit.ly/free-bank-login

Detection Results
----------------------------------------

[!] URL shortening service detected
[!] Suspicious keyword detected: login
[!] Suspicious keyword detected: banking

Risk Level: HIGH RISK
```

---

# Technology Stack

## Core Technologies

* Python
* URL Parsing
* Heuristic Threat Analysis
* Rule-Based Detection

## Security Concepts

* Web Security
* Phishing Detection
* URL Threat Analysis
* Social Engineering Indicators
* Suspicious Domain Inspection

---

# Repository Structure

```text
phishing-url-detector/
│
├── detector.py
├── rules.py
├── SECURITY.md
├── SECURITY-NOTES.md
├── requirements.txt
└── README.md
```

---

# Installation

```bash
git clone https://github.com/codeby-rhythm-sharma/phishing-url-detector.git

cd phishing-url-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Run the detector:

```bash
python detector.py
```

Enter URLs for threat analysis directly through the terminal interface.

---

# Security Notes

This project is intended for:

* Cybersecurity learning
* Threat-analysis experimentation
* Educational phishing detection workflows
* Beginner-friendly security research

This project is NOT intended to replace enterprise-grade phishing-detection systems or production security infrastructure.

---

# Future Enhancements

* Domain reputation analysis
* WHOIS-based domain-age inspection
* Machine-learning phishing classification
* Real-time blacklist integration
* Browser-extension support
* Batch URL scanning
* Threat-intelligence feed integration

---

# Open Source & Contributions

Contributions are welcome for:

* Improved threat-detection rules
* Better URL normalization workflows
* Additional phishing heuristics
* Detection optimization
* CLI improvements
* Security-focused enhancements

---

# License

Licensed under the MIT License.

---

<div align="center">

### Building Lightweight Threat-Detection Workflows for Safer Web Navigation

<br>

<a href="https://github.com/codeby-rhythm-sharma">
<img src="https://img.shields.io/badge/More%20Security%20Projects-FF4D4D?style=for-the-badge&logo=github&logoColor=white"/>
</a>

</div>
