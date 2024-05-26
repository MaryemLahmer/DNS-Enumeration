import dns.resolver
import sys

try:
    #reading the domain input
    domain = sys.argv[1]
except IndexError:
    print('Syntax Error. Command should be: python3 dnsEnumerate.py <domainName> ')
    quit()
#setting up dns records types, for example A is for ipv4 and AAAA is for ipv6
record_types = ['A','AAAA','MX','PTR','SOA','TXT','CNAME']

for records in record_types:
    try:
        answer = dns.resolver.resolve(domain,records)
        print(f'\n{records} Records')
        print('-'*30)
        for server in answer:
            print(server.to_text()) 
    #if domain name does not exist or if there is a typo
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist, check your spelling.')
        quit()
    #if no answer after domain resolving
    except dns.resolver.NoAnswer:
        print(f'{records} Records')
        print('-'*30)
        print('No record found for: ',records+'\n')
        pass  
    #if program gets interrupted
    except KeyboardInterrupt:
        print('Quitting')
        quit()

