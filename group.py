import pandas as pd
#import os
#print(os.getcwd())

df = pd.read_excel('EU_PE_Auction_Database.xlsx', sheet_name = 'Sellers & advisors')

lname = []
ladvisor = []
lseller = []

for name,group in df.groupby('Target'):
    strout1 = ''
    strout2 = ''
    for i in range(0,len(group['Advisor'])):
        #if group['Advisor Type'])[i] != None or  group['Advisor'])[i] != None:
        if strout1 == '':
            strout1 = str(list(group['Advisor Type'])[i]) + ' : '+ str(list(group['Advisor'])[i])
        else:
            strout1 += ', ' + str(list(group['Advisor Type'])[i]) + ' : '+ str(list(group['Advisor'])[i])
            
        if strout2 == '':
            strout2 = str(list(group['Seller'])[i]) 
        else:
            strout2 += ', ' + str(list(group['Advisor Type'])[i]) 
            
    lname.append(name) 
    ladvisor.append(strout1)
    lseller.append(strout2)

dfout = pd.DataFrame({'Target' : lname, 'Advisor' : ladvisor, 'Seller' : lseller})

writer = pd.ExcelWriter('output.xlsx', engine = 'openpyxl')
dfout.to_excel(writer,sheet_name = 'Master Sheet', index = True)
writer.save()
