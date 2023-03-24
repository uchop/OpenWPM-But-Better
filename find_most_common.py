if __name__ == '__main__':
    common_list = []
    final_common_list = []

    with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/ad_hosts_abp_stateful.csv', 'r') as t1, open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/ad_hosts_ublock_stateful.csv', 'r') as t2:
            file1 = t1.readlines()
            file2 = t2.readlines()

            for line1 in file1:
                  if line1 in file2:
                        common_list.append(line1)

    
    with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM-But-Better/ad_hosts_ghostery_stateful.csv', 'r') as t3:
           file3 = t3.readlines()
           for val in common_list:
                  if val in file3:
                         final_common_list.append(val)


    #print(len(final_common_list))
    final_common_list.sort()     
    print(final_common_list)
#     list_set = set(final_common_list)
#     print(len(list_set))
    count_dict = dict()   

#     for ls in list_set:
#         count = 0
#         for x in final_common_list:
#             if ls == x:
#                 count += 1
            
#         count_dict.update({ls:count})

# #print(count_dict)
# sorted_dict = sorted(count_dict.items(), key=lambda x:x[1])

# #print(sorted_dict)

    # for x in final_common_list:
    #     count = 0
    #     for  line1 in file1:
    #             if x == line1:
    #                     count+= 1

    #     for  line2 in file2:
    #             if x == line2:
    #                     count+= 1

    #     for  line3 in file3:
    #             if x == line3:
    #                     count+= 1

    #     count_dict.update({x:count})

    # sorted_dict = sorted(count_dict.items(), key=lambda x:x[1])
    # print(sorted_dict)


    # with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM Data/500 sites/Ad_Tracker_Blocking/Stateful/All Responses Hosts/responses_abp_stateful_no_dupes.csv', 'r') as t4:
    #     file4 = t4.readlines()

    # with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM Data/500 sites/Ad_Tracker_Blocking/Stateful/All Responses Hosts/responses_ublock_stateful_no_dupes.csv', 'r') as t5:
    #     file5 = t5.readlines()

    # with open('/Users/payalkulkarni/Documents/GitHub/OpenWPM Data/500 sites/Ad_Tracker_Blocking/Stateful/All Responses Hosts/responses_abp_stateful_no_dupes.csv', 'r') as t6:
    #     file6 = t6.readlines()
        
    # for x in final_common_list:
    #     count = 0
    #     for  line1 in file4:
    #         if line1 in x:
    #             count+= 1

    #     for  line2 in file5:
    #         if line2 in x:
    #             count+= 1

    #     for  line3 in file6:
    #         if line3 in x:
    #             count+= 1

    #     count_dict.update({x:count})

    # #print(count_dict)
    # sorted_dict = sorted(count_dict.items(), key=lambda x:x[1]) 
    # #print(sorted_dict)

    

