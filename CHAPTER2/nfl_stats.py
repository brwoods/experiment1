import csv

# Open the CSV file
with open('D:\\Learn_AI_Assisted_Programming_2ed\\CHAPTER2\\nfl_offensive_stats.csv', mode='r') as file:
    # Read the CSV data
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        print(row)