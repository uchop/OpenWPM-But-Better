if __name__ == '__main__':
    list_of_flase_positives = []
    with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/EasyPrivacy.csv', 'r') as t1, open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/Over Blocking/Stateless/URLs blocked by Extensions/urls_blocked_by_ghostery_stateless.csv', 'r') as t2:
            easylist_csv = t1.readlines()
            extension_csv = t2.readlines()
            

            for line1 in extension_csv:
                flag = False
                l = line1.split('.')
                s = ''
                if len(l) >1:
                    s += l[-2] + '.' + l[-1]
                    # print("s before", len(s))
                    s = s.strip('\n')
                    # print("s after", len(s))
                    # print("s:", s)
                for line2 in easylist_csv:
                    if s in line2:
                        #print(s, "is in ", line2)
                        flag = True
                        break
                if not flag:
                    list_of_flase_positives.append(line1)
            #print('list ', list_of_flase_positives)

    with open('potential_false_positives_ghostery_stateless_ep.csv', 'w') as outFile:
            for val in list_of_flase_positives:
                outFile.write(val)


