import matplotlib.pyplot as plt

def plot_election_results(total_seats, seats_X, seats_Y, seats_Z):
    parties = ['X', 'Y', 'Z']
    seats = [seats_X, seats_Y, seats_Z]

    plt.figure(figsize=(8, 6))
    plt.bar(parties, seats, color=['green', 'orange', 'red'])
    plt.xlabel('Parties')
    plt.ylabel('Number of Seats')
    plt.title('Election Results in West Bengal')
    plt.xticks(parties)
    plt.grid(axis='y', linestyle='--', alpha=0.2)

    # Add text labels for each bar
    for i, seat in enumerate(seats):
        plt.text(i, seat + 1, str(seat), ha='center')

    plt.show()

# Example usage:
total_seats = int(input("Enter total number of seats: "))
seats_X = int(input("Enter number of seats party X got: "))
seats_Y = int(input("Enter number of seats party Y got: "))
seats_Z = int(input("Enter number of seats party Z got: "))

plot_election_results(total_seats, seats_X, seats_Y, seats_Z)
