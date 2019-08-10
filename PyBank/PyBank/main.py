# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "C:/Users/Drew's Surface/Documents/python-challenge/PyBank/budget_data.csv")
csvpath = "C:/Users/Drew's Surface/Documents/python-challenge/PyBank/budget_data.csv"
#print (csvpath)

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    profit_loss = []
    dates = []
        
    counter = 0
    pl = 0
    diff = 0
    max_date = str()
    min_date = str()
    for row in csvreader:
        profit_loss.append(int(row[1]))
        dates.append((row[0]))    
        counter = counter + 1
        pl = pl + (int(row[1]))
    change = [profit_loss[i+1] - profit_loss[i] for i in range(len(profit_loss)-1)]
    for row in change:
        diff = row + diff
    average = diff / (len(profit_loss)-1)
    
     
    max_increase = max(change)
    min_increase = min(change)
    
    i = 0
    for row in change:
        i = i+1
        if row == max_increase:
            break
        else: 
            i = i+1
            
    x=0
    for row in dates:
        if x == i:
            max_date = row
        else:
            x=x+1


    a = 0
    for row in change:
        a = a+1
        if row == min_increase:
            break
        else: 
            a = a+1
    print(a)        
    b=0
    for row in dates:
        if b == a:
            min_date = row
        else:
            b=b+1
    
    # Printing output:
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {counter}')
    print(f'Total: ${pl}')
    print(f'Average change: ${round(average,2)}')
    print(f'Greatest Increase in Profits: {max_date} (${max_increase})')
    print(f'Greatest Decrease in Profits: {min_date} (${min_increase})')     

    filename = 'output results.txt' 
    with open(filename, 'w') as textfile: 
        textfile.write("Financial Analysis\n")
        x = ("----------------------------\n",
        "\n",
        f'Total Months: {counter}\n',
        f'Total: ${pl}\n',
        f'Average change: ${round(average,2)}\n',
        f'Greatest Increase in Profits: {max_date} (${max_increase})\n',
        f'Greatest Decrease in Profits: {min_date} (${min_increase})\n')   
        textfile.writelines(x)
        textfile.close()  