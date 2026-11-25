# Count survived and not survived passengers
survival_count = df['Survived'].value_counts().sort_index()

# Create pie chart
plt.pie(
    survival_count.values,
    labels=['Not Survived', 'Survived'],
    autopct='%1.1f%%'
)

# Add title
plt.title('Passenger Survival Proportion')

# Display plot
plt.show()
