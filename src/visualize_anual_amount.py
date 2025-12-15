#######################################################################
############################Line Chart#################################
#######################################################################

import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.use(
    "agg"
)  # Use the 'agg' backend which doesn't require an interactive display

# Load the CSV file
file_path = "your_file.csv"  # Replace 'your_file.csv' with your CSV file path
data = pd.read_csv(file_path)

# Filter data for Mixed Reality research (use it when your data contains various research topics)
# mixed_reality_data = data[
#     data["Title"].str.contains("Mixed Reality", case=False, na=False)
# ]
# directly use the original data because it only contains topic on MR
mixed_reality_data = data

# Count the number of publications for each year
publication_trend = mixed_reality_data["Year"].value_counts().sort_index()

# Plotting the annual publication trend as a line chart
plt.figure(figsize=(10, 6))
plt.plot(publication_trend.index, publication_trend.values, marker="o", linestyle="-")
plt.title("Annual Publication Trend of Mixed Reality Research")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.xticks(
    range(2003, 2024), rotation=45
)  # Set x-axis ticks for each year from 2003 to 2023
plt.xlim(2002.5, 2023.5)  # Set x-axis limits from 2002.5 to 2023.5 to include margin
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "publication_trend_line.png"
)  # Save the plot as an image instead of displaying interactively


#######################################################################
#############################Bar Chart#################################
#######################################################################

import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.use(
    "agg"
)  # Use the 'agg' backend which doesn't require an interactive display

# Load the CSV file
file_path = "your_file.csv"  # Replace 'your_file.csv' with your CSV file path
data = pd.read_csv(file_path)

# Filter data for Mixed Reality research (use it when your data contains various research topics)
# mixed_reality_data = data[
#     data["Title"].str.contains("Mixed Reality", case=False, na=False)
# ]
# directly use the original data because it only contains topic on MR
mixed_reality_data = data

# Count the number of publications for each year
publication_trend = mixed_reality_data["Year"].value_counts().sort_index()

# Create a bar chart for the annual publication trend
plt.figure(figsize=(10, 6))
plt.bar(publication_trend.index, publication_trend.values, color="skyblue")
plt.title("Annual Publication Trend of Mixed Reality Research")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.xticks(
    range(2002, 2025), rotation=45
)  # Set x-axis ticks from 2002 to 2024 to include margin
plt.xlim(2002.5, 2023.5)  # Set x-axis limits from 2002.5 to 2023.5 to include margin
plt.grid(axis="y")  # Show gridlines on the y-axis
plt.tight_layout()

plt.savefig(
    "publication_trend_bar.png"
)  # Save the plot as an image instead of displaying interactively
