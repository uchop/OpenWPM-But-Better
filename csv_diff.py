from tld import get_tld, get_fld
import pandas as pd

if __name__ == '__main__':
    actual_false_positives = []
    with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM Data/500 sites/Ad_Tracker_Blocking/Stateless/All Responses Hosts/responses_vanilla_stateless_no_dupes.csv', 'r') as t1, open('/Users/payalkulkarni/Documents/GitHub/OpenWPM Data/500 sites/Ad_Tracker_Blocking/Stateless/All Responses Hosts/responses_ghostery_stateless_no_dupes.csv', 'r') as t2:
            fp_el_csv = t1.readlines()
            fp_ep_csv = t2.readlines()

    with open('diff_vanilla_ghostery_stateless.csv', 'w') as outFile:
        # #Actual false positive ads
        # for line1 in fp_el_csv:
        #     if line1 not in fp_ep_csv:
        #         outFile.write(line1)

        #Actual false positive trackers
        for line1 in fp_el_csv:
            if line1 not in fp_ep_csv:
                outFile.write(line1)

