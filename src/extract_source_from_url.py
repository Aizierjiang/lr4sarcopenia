import sys
import os
from urllib.parse import urlparse

def extract_middle_text(url):
    """
    Extracts the middle part of the URL, e.g., 'http://www.google.com/xyz' -> 'google'
    """
    try:
        parsed = urlparse(url.strip())
        netloc = parsed.netloc

        # Remove 'www.' if present
        if netloc.startswith("www."):
            netloc = netloc[4:]
        
        # Take the first part before the first dot
        middle_text = netloc.split('.')[0]
        return middle_text
    except Exception as e:
        print(f"Error processing URL '{url}': {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py inputFile.txt [outputFile.txt]")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) >= 3 else "urls_names.txt"

    # Check if output file exists
    if os.path.exists(output_file):
        overwrite = input(f"File '{output_file}' already exists. Replace? (y/n): ").strip().lower()
        if overwrite not in ["y", "yes"]:
            print("Operation cancelled.")
            return
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            urls = f.readlines()
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
        return

    middle_texts = []
    for url in urls:
        text = extract_middle_text(url)
        if text:
            middle_texts.append(text)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for text in middle_texts:
            f.write(text + "\n")
    
    print(f"Processed {len(middle_texts)} URLs. Output saved to '{output_file}'.")

if __name__ == "__main__":
    main()
