# Load the new background image
background_image_path = '/mnt/data/image.png'
bg_img = mpimg.imread(background_image_path)

# Plotting each chart with the new background image
fig, axs = plt.subplots(3, 2, figsize=(15, 15))
fig.suptitle("Visualizations for Tech Layoffs Data Analysis", fontsize=16)

# Helper function to set the background image for each subplot
def set_background(ax):
    # Display the background image in the axis
    ax.imshow(bg_img, aspect='auto', extent=ax.get_xlim() + ax.get_ylim(), alpha=0.3, zorder=0)

# 1. Gender Distribution in Tech Layoffs
axs[0, 0].bar(gender_labels, gender_distribution, color=['purple', 'blue', 'gray'], zorder=1)
axs[0, 0].set_title("Gender Distribution in Tech Layoffs (2022-2023)")
axs[0, 0].set_ylabel("Percentage (%)")
set_background(axs[0, 0])

# 2. Leadership Representation of Women in Tech Over Time
axs[0, 1].plot(years, leadership_percentage, marker='o', color='orange', zorder=1)
axs[0, 1].set_title("Leadership Representation of Women in Tech Over Time")
axs[0, 1].set_xlabel("Year")
axs[0, 1].set_ylabel("Percentage (%)")
set_background(axs[0, 1])

# 3. Attrition Rate Comparison by Gender
axs[1, 0].bar(attrition_labels, attrition_rate, color=['pink', 'lightblue'], zorder=1)
axs[1, 0].set_title("Attrition Rate Comparison by Gender")
axs[1, 0].set_ylabel("Relative Attrition Rate (%)")
set_background(axs[1, 0])

# 4. Reemployment Rates of Laid-Off Tech Employees by Gender
axs[1, 1].bar(reemployment_labels, reemployment_rate, color=['coral', 'teal', 'coral', 'teal'], zorder=1)
axs[1, 1].set_title("Reemployment Rates of Laid-Off Tech Employees by Gender")
axs[1, 1].set_ylabel("Reemployment Rate (%)")
set_background(axs[1, 1])

# 5. Comparison of Earnings Losses and Unemployment Risks Post-Layoff
axs[2, 0].bar(risk_labels, risk_values, color=['red', 'brown'], zorder=1)
axs[2, 0].set_title("Earnings Losses and Unemployment Risks Post-Layoff for Women")
axs[2, 0].set_ylabel("Percentage (%)")
set_background(axs[2, 0])

# Remove the last empty subplot
fig.delaxes(axs[2, 1])

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
