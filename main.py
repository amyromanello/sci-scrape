#from parser_mpi import fetch_initial_jobs, fetch_more_jobs, get_jobboard_id
from parser_hu import fetch_jobs
from email_template import render_jobs_email
from emailer import send_email
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def main():

    with open("config.json") as f:
        config = json.load(f)

    test_site = config["sites"][3] #HU = 3, MPI = 0
    session = requests.Session()

    #### HU ####
    # fetch all jobs (Static site)
    all_jobs = fetch_jobs(session, test_site["base_url"])
    ##############

    #### MPI ####
    #list_id = get_jobboard_id(session, test_site["base_url"])
    #base_api = f"https://www.mpg.de/jobboard/{list_id}/more_items"
    # # fetch initial jobs
    # initial_jobs = fetch_initial_jobs(session, test_site["base_url"])
    #
    # # fetch more jobs
    # more_jobs = fetch_more_jobs(session, base_api, start_offset=len(initial_jobs), limit=5)
    # all_jobs = initial_jobs + more_jobs
    # print(f"Found {len(all_jobs)} jobs")
    ############

    # Render HTML email
    html_content = render_jobs_email(config["user_name"][0], all_jobs)

    # Send email
    send_email(
        sender_email=os.getenv("SENDER_EMAIL"),
        app_password = os.getenv("APP_PASSWORD"),
        recipient_email=config["user_email"],
        subject="Your Daily SciScrape Digest",
        html_content=html_content
    )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

