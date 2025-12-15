import csv
import sys


# Read CSV file and extract data
def read_csv(file_name):
    data = []
    try:
        with open(file_name, "r", encoding="utf-8-sig") as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                citation = {
                    "Cites": row.get("Cites", ""),
                    "Authors": row.get("Authors", ""),
                    "Title": row.get("Title", ""),
                    "Year": row.get("Year", ""),
                    "Source": row.get("Source", ""),
                    "ArticleURL": row.get("ArticleURL", ""),
                    "Abstract": row.get("Abstract", ""),
                }
                data.append(citation)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
    return data


# Sort data by the specified key
def sort_data(data, sort_by="Cites"):
    def convert_to_int(value):
        try:
            return int(value)
        except ValueError:
            return 0  # Assign 0 if the value is not convertible to int

    return sorted(data, key=lambda x: convert_to_int(x[sort_by]), reverse=True)


# Convert data to Markdown format
def generate_markdown(data):
    markdown = ""
    for item in data:
        markdown += f"[{item['Title']}]({item['ArticleURL']})\n"
        markdown += f"  - **Authors:** {item['Authors']}\n"
        markdown += f"  - **Year:** {item['Year']}\n"
        markdown += f"  - **Cites:** {item['Cites']}\n"
        markdown += f"  - **Abstract:** {item['Abstract']}\n\n"
        markdown += f"<br> \n\n"
    return markdown


# Main program
def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = input("Enter the CSV filename: ").strip()
        if not file_name:
            print("Error: No filename provided.")
            sys.exit(1)

    sort_by_input = input("Enter 'Cites' or 'Year' to sort by: ").strip()
    sort_by = sort_by_input.capitalize()
    if sort_by not in ["Cites", "Year"]:
        sort_by = "Cites"
        print("Invalid sort option. Defaulting to 'Cites'.")

    data = read_csv(file_name)
    if not data:
        print("Warning: No data found in the CSV file.")
        return

    sorted_data = sort_data(data, sort_by)
    markdown_content = generate_markdown(sorted_data)

    # Set title and output file name based on sort type
    title = "### Sorted by Year" if sort_by == "Year" else "### Sorted by Citations"
    output_file_name = f"output_sort_by_{sort_by.lower()}.md"

    try:
        with open(output_file_name, "w", encoding="utf-8") as md_file:
            md_file.write(f"{title}\n\n")
            md_file.write(markdown_content)
    except Exception as e:
        print(f"Error writing Markdown file: {e}")
        sys.exit(1)

    print("Markdown file generated successfully.")


if __name__ == "__main__":
    main()