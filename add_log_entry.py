import json
import sys
from datetime import datetime

# Predefined list of allowed tags
ALLOWED_TAGS = ["development", "life"]

def add_log_entry(data=None, tags=None):
    # Path to the life log file
    log_file = "life-log.json"
    
    # Validate tags if provided
    if tags:
        # Convert to list if a single string is provided
        if isinstance(tags, str):
            tags = [tags]
            
        # Check if all provided tags are in the allowed list
        invalid_tags = [tag for tag in tags if tag not in ALLOWED_TAGS]
        if invalid_tags:
            print(f"Error: The following tags are not allowed: {', '.join(invalid_tags)}")
            print(f"Allowed tags are: {', '.join(ALLOWED_TAGS)}")
            sys.exit(1)
    
    try:
        # Read existing entries
        with open(log_file, 'r') as f:
            entries = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        entries = []
    
    # Prompt for data if not provided
    if data is None:
        data = input("Enter your log entry: ")
    
    # Create new entry
    new_entry = {
        "timestamp": datetime.now().isoformat(),
        "data": data
    }
    
    # Add tags if provided
    if tags:
        new_entry["tags"] = tags
    
    # Add new entry to the list
    entries.append(new_entry)
    
    # Write back to file
    with open(log_file, 'w') as f:
        json.dump(entries, f, indent=2)
        
    print(f"Log entry added successfully!")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Add a new entry to the life log')
    parser.add_argument('--data', '-d', help='The content of the log entry')
    parser.add_argument('--tags', '-t', nargs='+', help='Tags for the entry (must be from the allowed list)')
    
    args = parser.parse_args()
    
    add_log_entry(data=args.data, tags=args.tags)
