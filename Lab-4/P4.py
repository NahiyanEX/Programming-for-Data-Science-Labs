import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("train.csv")


# Count male and female passengers
gender_count = df['Sex'].value_counts()

# Create bar chart
plt.bar(gender_count.index, gender_count.values)

# Add title and labels
plt.title('Number of Male and Female Passengers')
plt.xlabel('Gender')
plt.ylabel('Number of Passengers')

# Display plot
plt.show()
