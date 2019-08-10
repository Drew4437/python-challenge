# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "C:/Users/Drew's Surface/Documents/PythonStuff/PyPoll/election_data.csv")
csvpath = "C:/Users/Drew's Surface/Documents/PythonStuff/PyPoll/election_data.csv"

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    pypoll = []
    
    counter = 0
    for row in csvreader:
        pypoll.append(int(row[0])) 
        counter = counter + 1
    print(counter)

    khan_counter = 0
    correy_counter = 0
    li_counter = 0
    otool_counter = 0
    candadite = row(2)
    for row in csvreader:
        if (candadite == "Khan"):   
            khan_counter = khan_counter + 1
        elif (candadite == "Li"):
            li_counter = li_counter+ 1
        elif (candadite == "Correy"):
            correy_counter = correy_counter + 1
        elif (candadite == "O'Tool"):
            otool_counter = otool_counter +1
    winner = max(khan_counter,correy_counter,li_counter,otool_counter)
    total_sum = khan_counter + correy_counter + li_counter + otool_counter
    k_perc = khan_counter / total_sum *100
    c_perc = correy_counter / total_sum *100
    l_perc = li_counter / total_sum *100
    o_perc = otool_counter / total_sum *100

  
  # Printing output:
    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: {counter}')
    print("----------------------------")
    print(f'Khan: {k_perc}% {kahn_counter}')
    print(f'Correy: {c_perc}% {correy_counter}')
    print(f'Li: {l_perc}% {li_counter}')
    print(f'OTooley: {o_perc}% {otool_counter}')
    print(f'Winner: {winner}')
    print("----------------------------")
  
    filename = 'output results pypoll.txt' 
    with open(filename, 'w') as textfile: 
        textfile.write("Election Results")
        x = ("----------------------------",
        "\n",
        f'Total Votes: {counter}',
        "----------------------------",
        f'Khan: {k_perc}% {kahn_counter}',
        f'Correy: {c_perc}% {correy_counter}',
        f'Li: {l_perc}% {li_counter}',
        f'OTooley: {o_perc}% {otool_counter}',
        f'Winner: {winner}',
        "----------------------------")
        textfile.writelines(x)
        textfile.close()