"""
Development by George Sued
github: http://github.com/GeorgeSued14
Created At 28-02-2021

"""
import socket as s
import sys
import re

host = sys.argv[1]
custom_domain = sys.argv[2:]

DOMAINS = [".com", ".org", ".net"]


def get_hostname():

    if (len(custom_domain) > 0):
        DOMAINS.append(custom_domain[0])
    for i in DOMAINS:
        if not re.search(f"{i}$", host):
            continue
        else:
            try:
                hostName = s.gethostbyname(host)
                print("IP of the host {} is: {}".format(host, hostName))
                break
            except s.gaierror:
                print("No address found for name '{}'".format(host))
                break
    else:
        print(
            "\nURL invalid (format valid: example.[com|br|org|net] or insert a custom domain in argument.\n")
        print("Example:'python get_hostname.py test.xyz .xyz'")


get_hostname()
