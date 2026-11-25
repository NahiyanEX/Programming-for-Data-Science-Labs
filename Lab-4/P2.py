import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("train.csv")

# Calculate average fare by passenger class
avg_fare = df.groupby('Pclass')['Fare'].mean()

# Create line plot
plt.plot(avg_fare.index, avg_fare.values, marker='o')

# Add title and labels
plt.title('Average Fare by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Average Fare')

# Display plot
plt.show()
