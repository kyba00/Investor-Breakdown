from decimal import *

import pandas

getcontext().prec = 4
data_frame = pandas.read_excel("Datasheets\\FR_Input.xlsx")

biglist = data_frame[['Org_Name','MR_USD','INVS_Names']]
db = {}
for index in biglist.index:
    org_name, MR, investors = biglist.Org_Name[index], biglist.MR_USD[index], biglist.INVS_Names[index]
    investors_list = [ele.strip() for ele in investors.split(",")]

    share = round(MR / len(investors_list)) # Be aware of accumulative error
    if org_name not in db:
        db[org_name] = {investor: share for investor in investors_list}
    else:
        for investor in investors_list:
            org = db[org_name]
            if investor not in org:
                org[investor] = share
            else:
                org[investor] += share


f = open("output.csv", 'w')
f.write("Org_Name,Investor,MR\n")

for k, v in db.items():
    org = k
    for investor, MR in v.items():
        f.write(','.join((org, investor, str(MR))))
        f.write('\n')

f.close()



#     if org_name in db:
#         org = db[org_name]
#     else:
#         org = {}
#
#     for investor in investors_list:
#         if investor in org:
#             previous_share = org.get(investor)
#         else:
#             previous_share = 0
#         org[investor] = previous_share + share
#
#     db[org_name] = org
#