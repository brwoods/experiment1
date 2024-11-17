import csv

# Open the CSV file
with open('D:\\Learn_AI_Assisted_Programming_2ed\\CHAPTER2\\nfl_offensive_stats.csv', mode='r') as file:
    # Read the CSV data
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        print(row)
        # Initialize a variable to store the total passing yards
        total_passing_yards = 0

        # Check if the player position is "QB"
        if row[2] == "QB":
            # Add the passing yards to the total
            total_passing_yards += int(row[7])

        # Print the total passing yards for all QBs
        print(f"Total passing yards for QBs: {total_passing_yards}")
        # Create a dictionary to store passing yards by player
        passing_yards_by_player = {}

        # Reset the file pointer to the beginning of the file
        file.seek(0)

        # Skip the header row
        next(csv_reader)

        # Iterate over each row in the CSV file again
        for row in csv_reader:
            # Check if the player position is "QB"
            if row[2] == "QB":
                player_name = row[1]
                passing_yards = int(row[7])
                
                # Add the passing yards to the player's total
                if player_name in passing_yards_by_player:
                    passing_yards_by_player[player_name] += passing_yards
                else:
                    passing_yards_by_player[player_name] = passing_yards

        # Sort the players by total passing yards in descending order
        sorted_passing_yards = sorted(passing_yards_by_player.items(), key=lambda x: x[1], reverse=True)

        # Print the sorted passing yards
        for player, yards in sorted_passing_yards:
            print(f"{player}: {yards} passing yards")