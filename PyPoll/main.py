#import the os module that will allow us to create file paths across operating systems
import os 

#import module for readiing the csv file
import csv


csvpath = os.path.join(r"C:\Users\marie\Documents\KU_Bootcamp\Python_Challenge\PyPoll\Resources\Election-Data.csv")


#set variables
all_votes = 0 
stockham = 0
degette = 0
doane = 0

# Open csv file to read
with open(csvpath, 'r', newline= '', encoding= 'utf-8') as votes:

    # Store data under the csvreader variable
    csv_reader = csv.reader(votes, delimiter=",") 

    #skip header
    header = next(csv_reader)     

    #navigate through the rows in csv file
    for row in csv_reader: 

        #create variable called all_votes used to count voter id's
        all_votes +=1

        #tally up the number of times the candidates names appears
        if row[2] == "Charles Casper Stockham": 
            stockham +=1
        elif row[2] == "Diana DeGette":
            degette +=1
        elif row[2] == "Raymon Anthony Doane": 
            doane +=1

#use tallys from both lists to find a winner 
votes = [stockham, degette, doane]
contenders = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]

#zip together 
votes_contenders = dict(zip(votes, contenders))
key = max(votes_contenders, key=votes_contenders.get)

#print analysis
s_percent = (stockham/all_votes) *100
d_percent = (degette/all_votes) *100
a_percent = (doane/all_votes) *100

#print out election results
print(f"Election Results")
print(f"-------------------------------")
print(f"Total Votes: {all_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {s_percent:.3f}% ({stockham})")
print(f"Diana DeGette: {d_percent:.3f}% ({degette})")
print(f"Raymon Anthony Doane: {a_percent:.3f}% ({doane})")
print(f"-------------------------------")
print(f"Winner: {key}")
print(f"-------------------------------")

#output 
output = os.path.join(r"C:\Users\marie\Documents\KU_Bootcamp\Python_Challenge\PyPoll\Analysis.txt")
with open(output, "w") as file:


#print the output in Analysis file 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {all_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {s_percent:.3f}% ({stockham})")
    file.write("\n")
    file.write(f"Diana DeGette: {d_percent:.3f}% ({degette})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {a_percent:.3f}% ({doane})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")