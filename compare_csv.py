from tld import get_tld, get_fld
import pandas as pd

if __name__ == '__main__':

    with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/EasyList.csv', 'r') as t1, open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/Under:Over Blocking/Stateful/URLS blocked by extensions/urls_blocked_by_abp_stateful.csv', 'r') as t2:
            easylist_csv = t1.readlines()
            extension_csv = t2.readlines()

    # print(len(easylist_csv))
    # print(len(extension_csv))

    with open ('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/HTTP Response Analysis/Stateful/ABP/responses_abp_stateful.csv', 'r') as testfile:
        for line1 in testfile:
            print(line1[url])
            break
            if "url" not in line1:
                print(get_tld(line1[2]))

    # def fix_url_protocol(url):
    #     if not (url.startswith('http://') or url.startswith('https://')):
    #         url = 'http://{}'.format(url)
    #     return url

    # with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/Under:Over Blocking/Stateful/All HTTP Responses Hosts/abp_stateful_responses_hosts.csv', 'r') as t1:
    #     extension_csv = t1.readlines()

    #     for line in extension_csv:
    #         if line is not "":
    #             #print(line)
    #             new_url = fix_url_protocol(line)
    #             print(new_url)
    #             fld = get_fld(new_url)
    #             first_level_domains.append(fld)

    # print(first_level_domains)

