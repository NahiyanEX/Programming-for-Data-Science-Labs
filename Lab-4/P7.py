import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("train.csv")

# Create figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# First subplot: Age histogram
axes[0].hist(df['Age'].dropna(), bins=20)
axes[0].set_title('Distribution of Passenger Ages')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Frequency')

# Second subplot: Passenger class bar chart
class_count = df['Pclass'].value_counts().sort_index()

axes[1].bar(class_count.index.astype(str), class_count.values)
axes[1].set_title('Passengers in Each Class')
axes[1].set_xlabel('Passenger Class')
axes[1].set_ylabel('Number of Passengers')

# Adjust layout
plt.tight_layout()

# Display figure
plt.show()
