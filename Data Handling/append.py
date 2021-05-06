import os
import pandas as pd
 
#Setting up path
path = r"\\bosch.com\dfsrb\dfsbr\LOC\Ca1\Pur\Cp_la\tsc\PMQ-CP\Safe Launch\Production"
os.chdir(path)
 
#delete old appended file (from last run)
if os.path.exists("full_dataframe.xlsx"):
    os.remove("full_dataframe.xlsx")
 
#Creating new data frame to append data
newDF = pd.DataFrame(columns=['Part Number','Supplier Name', 'Quantity Productive Parts', 'Quantity Claimed Parts', 'Date'])
 
#looping through each file in folder
file_name = os.listdir(path)
 
for file in file_name:
    #Reading data frame
    df = pd.read_excel(file)
    
    #concat two dataframes
    newDF = pd.concat([df, newDF])
    print(newDF)
 
#Exporting full Dataframe to excel
    newDF.to_excel("full_dataframe.xlsx", index=False)