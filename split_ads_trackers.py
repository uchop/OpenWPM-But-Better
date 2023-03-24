import csv
if __name__ == '__main__':
        
    ads_blocked_by_extension = []
    trackers_blocked_by_extension = []
    with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM Data/500 sites/Ad_Tracker_Blocking/Stateless/Differences/diff_vanilla_ghostery_stateless.csv', 'r') as t1, open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/EasyList.csv', 'r') as t2:
            extensionfile = t1.readlines()
            easylist = t2.readlines()
    with open('ads_blocked_by_ghostery_stateless.csv', 'w') as outFile:
        for line1 in extensionfile:
            flag = False
            l = line1.split('.')
            s = ''
            if len(l) > 1:
                s += l[-2] + '.' + l[-1]
                s = s.strip('\n')
            for line2 in easylist:
                if s in line2:
                    outFile.write(line1)
            
