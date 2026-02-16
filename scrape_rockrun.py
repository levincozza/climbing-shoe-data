#!/usr/bin/env python3
"""
Scrape climbing shoe sizing data from RockRun website.
"""

import requests
from bs4 import BeautifulSoup
import csv
import json


def scrape_shoe_sizing_table(url):
    """
    Scrape the shoe sizing table from the RockRun blog post.
    
    Args:
        url: The URL of the sizing guide page
        
    Returns:
        list: List of dictionaries containing shoe data
    """
    # Fetch the webpage
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    # Parse HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all tables on the page
    tables = soup.find_all('table')
    
    # The main sizing table is the largest one - find it
    main_table = None
    max_rows = 0
    
    for table in tables:
        rows = table.find_all('tr')
        if len(rows) > max_rows:
            max_rows = len(rows)
            main_table = table
    
    if not main_table:
        raise ValueError("Could not find the sizing table")
    
    # Extract data from the table
    shoe_data = []
    rows = main_table.find_all('tr')
    
    # Skip the header row (first row)
    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        
        if len(cells) >= 7:  # Ensure we have all columns
            shoe_info = {
                'rock_shoe_model': cells[0].get_text(strip=True),
                'category_a': cells[1].get_text(strip=True),
                'category_b': cells[2].get_text(strip=True),
                'category_c': cells[3].get_text(strip=True),
                'category_d': cells[4].get_text(strip=True),
                'foot_volume': cells[5].get_text(strip=True),
                'foot_type': cells[6].get_text(strip=True)
            }
            
            # Only add if the model name is not empty
            if shoe_info['rock_shoe_model']:
                shoe_data.append(shoe_info)
    
    return shoe_data


def save_to_csv(data, filename='rockrun_shoe_sizing.csv'):
    """Save scraped data to CSV file."""
    if not data:
        print("No data to save")
        return
    
    keys = data[0].keys()
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} records to {filename}")


def save_to_json(data, filename='rockrun_shoe_sizing.json'):
    """Save scraped data to JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved {len(data)} records to {filename}")


def main():
    """Main function to run the scraper."""
    url = 'https://rockrun.com/blogs/the-flash-rock-run-blog/rock-climbing-shoe-sizing-guide'
    
    print(f"Scraping data from: {url}")
    
    try:
        # Scrape the data
        shoe_data = scrape_shoe_sizing_table(url)
        
        print(f"Successfully scraped {len(shoe_data)} shoe models")
        
        # Save to both CSV and JSON formats
        save_to_csv(shoe_data)
        save_to_json(shoe_data)
        
        # Print first few entries as sample
        print("\nSample data (first 3 entries):")
        for i, shoe in enumerate(shoe_data[:3], 1):
            print(f"\n{i}. {shoe['rock_shoe_model']}")
            print(f"   Category A: {shoe['category_a']}")
            print(f"   Category B: {shoe['category_b']}")
            print(f"   Category C: {shoe['category_c']}")
            print(f"   Category D: {shoe['category_d']}")
            print(f"   Foot Volume: {shoe['foot_volume']}")
            print(f"   Foot Type: {shoe['foot_type']}")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
