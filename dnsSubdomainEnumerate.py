import dns.resolver
import sys

domain = sys.argv[1]

def main():
    f = open("subdns.txt", "r")
    #subdomains generally have multiple ip addresses, so we keep a valid value per resolution and discard the others
    subdomain_store = []
    #iterating the subdomains from the file
    for subdomain in f:
        subdomain = subdomain.strip()
        try:
            ip_value = dns.resolver.resolve(f'{subdomain}.{domain}','A')
            if ip_value:
                #adding the valid subdomain value to the store
                subdomain_store.append(f'{subdomain}.{domain}')
                if f"{subdomain}.{domain}" in subdomain_store:
                    print(f'{subdomain}.{domain} is valid')
                else:
                    pass

        #dns no answer error
        except dns.resolver.NoAnswer:
            print(f'{subdomain}.{domain} did not answer')
            pass

        #subdomain not found 
        except dns.resolver.NXDOMAIN:
            print(f'{subdomain}.{domain} not found!')
            pass

        #keyboard interruption
        except KeyboardInterrupt:
            print('Quitting')
            quit()

    f.close()

#running the program
main()
