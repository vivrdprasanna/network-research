import redditharbor.login as login
import redditharbor.utils.fetch as fetch
import redditharbor.utils.subreddit_collections as collections

# from tqdm import tqdm
# from tqdm.notebook import tqdm
from collections import Counter
from redditharbor.dock.pipeline import collect

SUPABASE_URL = "https://ajebvybwlvcybhsnhdgs.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFqZWJ2eWJ3bHZjeWJoc25oZGdzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwMjA0ODMwMSwiZXhwIjoyMDE3NjI0MzAxfQ.aOeSBfhv3ojr1UPcAPtnM2l9QyHM4tUmavt7Zhbe8ak"

REDDIT_PUBLIC = "9zk3ptJvrNihAEGiiyTYPg"
REDDIT_SECRET = "dpYAGYqjV3jfcdg7bNjXJ9gX99cOuQ"
REDDIT_USER_AGENT = "berkeley:network-analysis (u/stuffingmybrain)"

DB_CONFIG = {
    "user": "test_redditor",
    "submission": "test_submission",
    "comment": "test_comment"
}

    

def main():
    reddit_client = login.reddit(public_key=REDDIT_PUBLIC, secret_key=REDDIT_SECRET, user_agent=REDDIT_USER_AGENT)
    supabase_client = login.supabase(url=SUPABASE_URL, private_key=SUPABASE_KEY)

    subreddits = collections.r_Ideology_top2 # List of specific subreddits
    sort_types = ["hot", "top", "rising", "controversial"]
    limit = None  # Adjust limit as needed
    level = 400   # Depth of comment threads

    collector = collect(reddit_client=reddit_client, supabase_client=supabase_client, db_config=DB_CONFIG)
    collector.subreddit_submission_and_comment(subreddits, sort_types, limit=limit, level=level)

    ### Fetching User Data and Collecting Their Submissions and Comments

    user_fetcher = fetch.user(supabase_client=supabase_client, db_name=DB_CONFIG["user"])
    users = user_fetcher.name(limit=None)  # Fetches all user names from the database

    # Collect Submissions and Comments from these Users
    collector.submission_from_user(users, sort_types, limit=limit)  # Adjust limit as needed
    collector.comment_from_user(users, sort_types, limit=limit)  # Adjust limit as needed
    
main()