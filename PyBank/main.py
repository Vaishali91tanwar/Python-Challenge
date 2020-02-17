import os
import csv

#Declaration of lists and dictionary
months=[]
profit_or_loss=[]
data=[]
data1=[]
combined_data={}
profit=[]
loss=[]

#Calculation of total number of months in the bank records file
def total_months(record):
    months.append(record[0])


#Storing of profit/losses over the entire period   
def amount(row):
    profit_or_loss.append(row[1])

#Calculation of net total amount of profit/losses over the entire period
def net_total_amount(list1):
    total_amount=0
    for i in range(len(list1)):
        total_amount+=int(list1[i])
    return total_amount


#Calculation of average of changes in profit/losses over the entire period    
def average_of_changes(list2):
    sum=0
    for i in range(len(list2)-1):
        change=int(list2[i+1])-int(list2[i])
        data.append(change)
    for j in range(len(data)):
        sum=sum+int(data[j])
    net_average=sum/len(data)
    return net_average

#Combining new data that is month and change in amount over the period
def new_data(list3, list4):
    for i in range(len(list3)-1):
        combined_data[list3[i+1]]=list4[i]  

#Calculation of Greatest increase in profits
def greatest(dict):
    max=0
    for d in dict:
        if int(dict[d])>int(max):
            greatest_month=d
            max=dict[d]
    profit.append(greatest_month)
    profit.append(max)


#Calculation of Greatest decrease in profits
def lowest(dict):
    min=0
    for d in dict:
        if int(dict[d])<int(min):
            lowest_month=d
            min=dict[d]
    loss.append(lowest_month)
    loss.append(min)        


#Reading the file containing bank records
csvpath=os.path.join("C:/Users/Divneet/Desktop/Python_Assignment_3/Python-Challenge/PyBank/03-Python_Instructions_PyBank_Resources_budget_data.csv")
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile)
    csv_header=next(csvreader)
    for row in csvreader:
        total_months(row)
        amount(row)
        
#Calling the functions        
total=net_total_amount(profit_or_loss)        
average=average_of_changes(profit_or_loss)
new_data(months,data)
greatest(combined_data)
lowest(combined_data)

#Printing the results to the terminal       
print("Financial Analysis") 
print("-----------------------------")            
print(f"Total months: {len(months)}")
print(f"Total: ${total}")
print(f"Average change: ${round(average,2)}")
print(f"Greatest Increase in Profits: {profit[0]} (${profit[1]})")
print(f"Greatest Decrease in Profits: {loss[0]} (${loss[1]})")

#Writing the results to the text file textPyBank
file=open("C:/Users/Divneet/Desktop/Python_Assignment_3/Python-Challenge/PyBank/textPyBank.txt","w")
string1="Financial Analysis\n---------------------\nTotal Months: "+str(len(months))+"\nTotal: $"+str(total)+"\nAverage Change: $"+str(round(average,2))+"\nGreatest Increase in Profits: "+str(profit[0])+" $("+str(profit[1])+")\nGreatest Decrease in Profits: "+str(loss[0])+" $("+str(loss[1])+")"
file.write(string1)
file.close()
