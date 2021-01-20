import socket
import csv
import time
from argparse import ArgumentParser

def main(args):
    with open('results.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')

        with open(args.hosts, 'r') as hostnames:
            hostname = ''
            aliaslist = []
            ip = []

            for host in hostnames:
                host = host.strip()
                if args.ip:
                    try:
                        hostname, aliaslist, ip = socket.gethostbyaddr(host)
                        csvwriter.writerow([host, hostname, ip[0]])
                        print(hostname + '-' + ip[0])
                    except socket.gaierror:
                        ip = 'Unable to resolve'
                        csvwriter.writerow([host, hostname, ip[0]])
                        print(hostname + '-' + ip[0])
                    except socket.herror as e:
                        print(e)
                else:
                    try:
                        hostname, aliaslist, ip = socket.gethostbyname_ex(host)
                        csvwriter.writerow([host, hostname, ip[0]])
                        print(hostname + '-' + ip[0])
                    except socket.gaierror:
                        ip = 'Unable to resolve'
                        csvwriter.writerow([host, hostname, ip])
                        print(hostname + '-' + ip[0])
                    except socket.herror as e:
                        print(e)

if __name__ == '__main__':

    # Parse command-line arguments
    parser = ArgumentParser()
    parser.add_argument('hosts', help='Name of text file that contains single column of hostnames to be looked up.')
    parser.add_argument('-i', '--ip', action='store_true', help="Do a reverse lookup on IP addresses instead of hostnames.")

    args = parser.parse_args()

    main(args)
