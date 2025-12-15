#######################################################################
############################Line Chart#################################
#######################################################################

import matplotlib

matplotlib.use(
    "agg"
)  # Use the 'agg' backend which doesn't require an interactive display

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
file_path = "your_file.csv"  # Replace 'your_file.csv' with your CSV file path
data = pd.read_csv(file_path)

# Filter data for Mixed Reality research (use it when your data contains various research topics)
# mixed_reality_data = data[
#     data["Title"].str.contains("Mixed Reality", case=False, na=False)
# ]
# directly use the original data because it only contains topic on MR
mixed_reality_data = data

# Extract 'Year' and 'Cites' columns
year_cites_data = mixed_reality_data[["Year", "Cites"]].copy()
year_cites_data["Year"] = pd.to_numeric(year_cites_data["Year"], errors="coerce")

# Group by Year and calculate total cites for each year
yearly_cites = year_cites_data.groupby("Year")["Cites"].sum().reset_index()

# Plotting the citation trend
plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_cites, x="Year", y="Cites", marker="o", linewidth=2)
plt.title("Annual Citation Trend of Mixed Reality Research")
plt.xlabel("Year")
plt.ylabel("Total Citations")
plt.grid(True)
plt.xticks(yearly_cites["Year"], rotation=45)
plt.tight_layout()

plt.savefig(
    "citation_trend_line.png"
)  # Save the plot as an image instead of displaying interactively


#######################################################################
#############################Bar Chart#################################
#######################################################################

import matplotlib

matplotlib.use(
    "agg"
)  # Use the 'agg' backend which doesn't require an interactive display

import pandas as pd
import matplotlib.pyplot as plt

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
    "citation_trend_bar.png"
)  # Save the plot as an image instead of displaying interactively
