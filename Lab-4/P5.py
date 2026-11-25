import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("train.csv")

# Create histogram
plt.hist(df['Age'].dropna(), bins=20)

# Add title and labels
plt.title('Distribution of Passenger Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Display plot
plt.show()
