import matplotlib.pyplot as plt
import numpy as np

# Data for each chart

# 1. Gender Distribution in Tech Layoffs (2022-2023)
gender_labels = ["Women", "Men", "They/Them"]
gender_distribution = [56, 43.8, 0.2]

# 2. Leadership Representation of Women in Tech Over Time
years = [1984, 2022, 2023]
leadership_percentage = [35, 32, 28]

# 3. Attrition Rate Comparison by Gender
attrition_labels = ["Women", "Men"]
attrition_rate = [145, 100]  # Using 100 as a baseline for men to show 45% higher attrition for women

# 4. Reemployment Rates of Laid-Off Tech Employees by Gender
reemployment_labels = ["Women (URL 5)", "Men (URL 5)", "Women (URL 6)", "Men (URL 6)"]
reemployment_rate = [31, 38, 36, 38]

# 5. Comparison of Earnings Losses and Unemployment Risks Post-Layoff
risk_labels = ["Earnings Loss Higher for Women", "Unemployment Risk Higher for Women"]
risk_values = [35, 45]

# Plotting each chart
fig, axs = plt.subplots(3, 2, figsize=(15, 15))
fig.suptitle("Visualizations for Tech Layoffs Data Analysis", fontsize=16)

# 1. Gender Distribution in Tech Layoffs
axs[0, 0].bar(gender_labels, gender_distribution, color=['purple', 'blue', 'gray'])
axs[0, 0].set_title("Gender Distribution in Tech Layoffs (2022-2023)")
axs[0, 0].set_ylabel("Percentage (%)")

# 2. Leadership Representation of Women in Tech Over Time
axs[0, 1].plot(years, leadership_percentage, marker='o', color='orange')
axs[0, 1].set_title("Leadership Representation of Women in Tech Over Time")
axs[0, 1].set_xlabel("Year")
axs[0, 1].set_ylabel("Percentage (%)")

# 3. Attrition Rate Comparison by Gender
axs[1, 0].bar(attrition_labels, attrition_rate, color=['pink', 'lightblue'])
axs[1, 0].set_title("Attrition Rate Comparison by Gender")
axs[1, 0].set_ylabel("Relative Attrition Rate (%)")

# 4. Reemployment Rates of Laid-Off Tech Employees by Gender
axs[1, 1].bar(reemployment_labels, reemployment_rate, color=['coral', 'teal', 'coral', 'teal'])
axs[1, 1].set_title("Reemployment Rates of Laid-Off Tech Employees by Gender")
axs[1, 1].set_ylabel("Reemployment Rate (%)")

# 5. Comparison of Earnings Losses and Unemployment Risks Post-Layoff
axs[2, 0].bar(risk_labels, risk_values, color=['red', 'brown'])
axs[2, 0].set_title("Earnings Losses and Unemployment Risks Post-Layoff for Women")
axs[2, 0].set_ylabel("Percentage (%)")

# Remove the last empty subplot
fig.delaxes(axs[2, 1])

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
