import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("train.csv")

# Create figure with three subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# First subplot: Gender bar chart
gender_count = df['Sex'].value_counts()

axes[0].bar(gender_count.index, gender_count.values)
axes[0].set_title('Passengers by Gender')
axes[0].set_xlabel('Gender')
axes[0].set_ylabel('Number of Passengers')

# Second subplot: Fare histogram
axes[1].hist(df['Fare'].dropna(), bins=20)
axes[1].set_title('Distribution of Passenger Fares')
axes[1].set_xlabel('Fare')
axes[1].set_ylabel('Frequency')

# Third subplot: Survival pie chart
survival_count = df['Survived'].value_counts().sort_index()

axes[2].pie(
    survival_count.values,
    labels=['Not Survived', 'Survived'],
    autopct='%1.1f%%'
)

axes[2].set_title('Passenger Survival Proportion')

# Adjust layout
plt.tight_layout()

# Display figure
plt.show()
