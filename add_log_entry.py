import json
from datetime import datetime

def add_log_entry():
    # Path to the life log file
    log_file = "life-log.json"
    
    try:
        # Read existing entries
        with open(log_file, 'r') as f:
            entries = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        entries = []
    
    # Create new entry
    new_entry = {
        "timestamp": datetime.now().isoformat(),
        "data": ""
    }
    
    # Add new entry to the list
    entries.append(new_entry)
    
    # Write back to file
    with open(log_file, 'w') as f:
        json.dump(entries, f, indent=2)

if __name__ == "__main__":
    add_log_entry()
