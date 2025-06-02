import os
import requests
import json
from datetime import datetime

# --- Configuration ---
BEEMINDER_USERNAME = "alexislearning"
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
    "impact--ai-safety", # Ensure this is the correct current slug for AI Safety
    "thinking--exprt-stdy",
    "thinking--heidegger",
    # New goals below
    "health--weights",
    "heath--jump-rope",
    "impact--blog-post",
    "health--steps",
    # Added new goals
    "impact--operations",
    "impact--systems-thi"
]
# The auth token will be read from GitHub Secrets (environment variable)
BEEMINDER_AUTH_TOKEN = os.environ.get("BEEMINDER_AUTH_TOKEN")
OUTPUT_FILE_PATH = "assets/data/beeminder_goals_data.json" # Relative to repo root

# --- Helper Function to ensure directory exists ---
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory): # Check if directory string is not empty
        os.makedirs(directory)
        print(f"Created directory: {directory}")

# --- Main logic FUNCTION DEFINITION ---
def fetch_all_goals_data():
    if not BEEMINDER_AUTH_TOKEN:
        print("Error: BEEMINDER_AUTH_TOKEN secret not found!")
        return 

    if not GOAL_SLUGS_TO_FETCH:
        print("No goal slugs configured to fetch.")
        return

    all_goals_data = {}  # Initialize as an empty dictionary
    success_count = 0

    for goal_slug in GOAL_SLUGS_TO_FETCH:
        api_url = f"https://www.beeminder.com/api/v1/users/{BEEMINDER_USERNAME}/goals/{goal_slug}.json"
        params = {"auth_token": BEEMINDER_AUTH_TOKEN}
        print(f"Fetching data for goal: {goal_slug} from: {api_url}")
        try:
            response = requests.get(api_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            current_value = data.get("curval") 
            goal_title = data.get("title", goal_slug)
            goal_data = {
                "current_value": current_value,
                "goal_title": goal_title,
                "last_updated_utc": datetime.utcnow().isoformat() + "Z"
            }
            # Special handling for health--steps, impact--blog-post, impact--operations, impact--systems-thi: fetch datapoints and compute average
            if goal_slug in ["health--steps", "impact--blog-post", "impact--operations", "impact--systems-thi"]:
                datapoints_url = f"https://www.beeminder.com/api/v1/users/{BEEMINDER_USERNAME}/goals/{goal_slug}/datapoints.json"
                dp_response = requests.get(datapoints_url, params=params, timeout=10)
                dp_response.raise_for_status()
                datapoints = dp_response.json()
                if datapoints:
                    days = set(dp["daystamp"] for dp in datapoints if float(dp.get("value", 0)) > 0)
                    total = sum(float(dp.get("value", 0)) for dp in datapoints)
                    num_days = len(days)
                    average = total / num_days if num_days > 0 else 0
                    goal_data["average_daily"] = average
                else:
                    goal_data["average_daily"] = None
            all_goals_data[goal_slug] = goal_data
            print(f"Successfully fetched data for {goal_slug}: {current_value}")
            success_count += 1
        except requests.exceptions.Timeout:
            print(f"Error: Timeout while fetching data for goal {goal_slug}")
            all_goals_data[goal_slug] = { "error": "timeout", "last_updated_utc": datetime.utcnow().isoformat() + "Z" }
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for goal {goal_slug}: {e}")
            all_goals_data[goal_slug] = { "error": str(e), "last_updated_utc": datetime.utcnow().isoformat() + "Z" }
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for goal {goal_slug}: {e}. Response: {response.text[:200]}")
            all_goals_data[goal_slug] = { "error": "json_decode_error", "last_updated_utc": datetime.utcnow().isoformat() + "Z" }
        except Exception as e:
            print(f"An unexpected error occurred for goal {goal_slug}: {e}")
            all_goals_data[goal_slug] = { "error": "unexpected_error", "last_updated_utc": datetime.utcnow().isoformat() + "Z" }

    if len(all_goals_data) > 0: 
        ensure_dir(OUTPUT_FILE_PATH)
        try:
            with open(OUTPUT_FILE_PATH, "w") as f:
                json.dump(all_goals_data, f, indent=4)
            print(f"All goals data (partially or fully) saved to {OUTPUT_FILE_PATH}")
        except IOError as e:
            print(f"Error writing data to file {OUTPUT_FILE_PATH}: {e}")
    else:
        print("No data was processed for any goal (all_goals_data dictionary is empty or not created).")

# --- SCRIPT EXECUTION (This calls the function defined above) ---
if __name__ == "__main__":
    if not GOAL_SLUGS_TO_FETCH: # Check if the list is empty
        print("Error: GOAL_SLUGS_TO_FETCH list is empty in the script. Please add goal slugs.")
    elif not BEEMINDER_USERNAME:
         print("Error: BEEMINDER_USERNAME is not set in the script.")
    # BEEMINDER_AUTH_TOKEN is checked inside fetch_all_goals_data as it comes from env
    else:
        fetch_all_goals_data()