import os
import requests
import json
from datetime import datetime

# --- Configuration ---
# (Your BEEMINDER_USERNAME, GOAL_SLUGS_TO_FETCH, etc. go here)
BEEMINDER_USERNAME = "alexislearning"
GOAL_SLUGS_TO_FETCH = [
    "systems--vim",
    # ... your other slugs ...
    "thinking--heidegger"
] 
BEEMINDER_AUTH_TOKEN = os.environ.get("BEEMINDER_AUTH_TOKEN") 
OUTPUT_FILE_PATH = "assets/data/beeminder_goals_data.json"

# --- Helper Function to ensure directory exists ---
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

# --- Main logic FUNCTION DEFINITION ---
# Make sure this whole block is present and correctly indented
def fetch_all_goals_data(): 
    if not BEEMINDER_AUTH_TOKEN:
        print("Error: BEEMINDER_AUTH_TOKEN secret not found!")
        return

    # ... (all the logic for fetching data for each goal, 
    #      creating all_goals_data dictionary, 
    #      and writing to OUTPUT_FILE_PATH goes here,
    #      as shown in the script from Turn #42) ...
    # For brevity, I'm not repeating the full internal logic of this function here
    # but ensure it's complete in your file.
    # Example of the end of the function:
    if len(all_goals_data) > 0 : # Check if any data was processed
        ensure_dir(OUTPUT_FILE_PATH)
        with open(OUTPUT_FILE_PATH, "w") as f:
            json.dump(all_goals_data, f, indent=4)
        print(f"All goals data (partially or fully) saved to {OUTPUT_FILE_PATH}")
    else:
        print("No data fetched or processed for any goal.")


# --- SCRIPT EXECUTION (This calls the function defined above) ---
if __name__ == "__main__":
    if not GOAL_SLUGS_TO_FETCH:
        print("Please define GOAL_SLUGS_TO_FETCH in the script with your goal slugs.")
    else:
        fetch_all_goals_data() # <--- This is the call to the function