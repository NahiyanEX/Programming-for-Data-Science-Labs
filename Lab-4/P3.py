import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = pd.read_csv("train.csv")


# Create scatter plot
plt.scatter(df['Age'], df['Fare'])

# Add title and labels
plt.title('Relationship Between Age and Fare')
plt.xlabel('Passenger Age')
plt.ylabel('Fare')

# Display plot
plt.show()
