import csv
if __name__ == '__main__':
    inFile = open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/trackers_blocked_by_ghostery_stateless.csv','r')
    listLines = []
    for line in inFile:
        if line in listLines:
            continue
        else:
            listLines.append(line)

    with open('trackers_blocked_by_ghostery_stateless_no_dupes.csv', 'w') as myfile:
        wr = csv.writer(myfile, delimiter=",")
        wr.writerows([c.strip() for c in r.strip(', ').split(',')] for r in listLines)