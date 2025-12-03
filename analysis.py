
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
satisfaction_scores = [3.99, -0.4, 1.36, 7.64]
industry_target = 4.5

# Calculate the average satisfaction score
average_score = np.mean(satisfaction_scores)

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(quarters, satisfaction_scores, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])

# Add the industry target line
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target})')

# Add labels and title
plt.xlabel('Quarter')
plt.ylabel('Patient Satisfaction Score')
plt.title('Quarterly Patient Satisfaction Scores vs. Industry Target')
plt.legend()

# Add data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom' if yval >= 0 else 'top', ha='center')


# Save the chart
plt.savefig('satisfaction_trend.png')

print(f"Average Patient Satisfaction Score: {average_score:.2f}")
print("Chart saved as satisfaction_trend.png")
