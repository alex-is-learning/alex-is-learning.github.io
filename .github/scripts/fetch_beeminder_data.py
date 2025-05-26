# ... (import statements and other parts of the script remain the same) ...
import os  
import requests
import json
from datetime import datetime
# --- Configuration ---
BEEMINDER_USERNAME = "alexislearning"
# THIS WILL BECOME A LIST OF YOUR GOAL SLUGS
GOAL_SLUGS_TO_FETCH = [
    "systems--vim",
    "thinking--self-expla",
    "health--stretching",
    "systems--touch-typ",
    "thinking--maths",
    "wellbeing--meditatio",
    "wellbeing--alex-tech",
    "thinking--prediction",
    "thinking--vervaeke",
    "thinking--boyd",
    "thinking--blogs",
    "thinking--matuschak",
    "impact--publc-wrtng",
    "thinking--wrld-model",
    "impact--ai-safety", # This was your original example, '2-ai-safety', I've kept the new slug based on your list
    "thinking--exprt-stdy",
    "thinking--heidegger"
] 
BEEMINDER_AUTH_TOKEN = os.environ.get("BEEMINDER_AUTH_TOKEN")
OUTPUT_FILE_PATH = "assets/data/beeminder_goals_data.json" # Path to the single JSON file

# ... (the rest of the Python script 'ensure_dir', 'fetch_all_goals_data', etc., remains the same as previously provided) ...

if __name__ == "__main__":
    if not GOAL_SLUGS_TO_FETCH:
        print("Please define GOAL_SLUGS_TO_FETCH in the script with your goal slugs.")
    else:
        fetch_all_goals_data()