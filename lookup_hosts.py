import socket
import csv
import time
from argparse import ArgumentParser

def main(args):
    with open('hosts.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n')

        with open(args.hostname_file, 'r') as hostnames:
            hostname = ''
            aliaslist = []
            ip = []

            for host in hostnames:
                try:
                    hostname, aliaslist, ip = socket.gethostbyname_ex(host.strip())
                except socket.gaierror:
                    ip = 'Unable to resolve'

                csvwriter.writerow([hostname, aliaslist, ip])

if __name__ == '__main__':

    # Parse command-line arguments
    parser = ArgumentParser()
    parser.add_argument('hosts_filename', help='Name of text file that contains single column of hostnames to be looked up.')

    args = parser.parse_args()

    main(args)