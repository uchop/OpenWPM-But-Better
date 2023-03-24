import json
from datetime import datetime
import sqlite3
import csv 

from pandas import read_sql_query

def get_host_from_url(url):
    return strip_scheme_www_and_query(url).split("/", 1)[0]

def strip_scheme_www_and_query(url):
    """Remove the scheme and query section of a URL."""
    if url:
        return url.split("//")[-1].split("?")[0].lstrip("www.")
    else:
        return ""

if __name__ == '__main__':
    http_response_hosts = []
    with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/HTTP Response Analysis/Stateless/Ghostery/responses_ghostery_stateless.csv','r') as csvfile:
        for url in csvfile:
            if "visit_id" not in url:
                hostname = get_host_from_url(url)
                #print(hostname)
                http_response_hosts.append(hostname)

    # with open('ghostery_stateless_repsonses_hosts.csv', 'w') as outFile:
    #         for val in http_response_hosts:
    #             outFile.write(val)

    with open('ghostery_stateless_repsonses_hosts.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile)
     wr.writerows([c.strip() for c in r.strip(', ').split(',')] for r in http_response_hosts)