# DNS-Enumeration
This script serves as a DNS Enumeration tool, developed with Python, that you can use to enumerate real world domains.
It implements DNS resolver (dns toolkit for Python) and handles basic exceptions such as syntax error, domain not found, records not found ...

#usage
python3 dnsEnumerate.py <domainName> 

# DNS-Subdomains-Enumeration
This script serves as a subdomain Enumeration tool, developed with Python, that you can use to enumerate real world subdomains.
It uses a file that contains 100 subdomains and iterates through them to identify which ones are valid and which ones are not valid.

#usage
python3 dnsSubdomainEnumerate.py <domainName> 
