import requests
from bs4 import BeautifulSoup
import re

MAIN_URL = "https://haushalt-und-personal.hu-berlin.de/de/personal/stellenausschreibungen"
HEADERS = {"User-Agent": "Mozilla/5.0",
           "X-Requested-With": "XMLHttpRequest"
           }

# def get_jobboard_id(session, MAIN_URL):
#     response = session.get(MAIN_URL, headers=HEADERS)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     button = soup.select_one("a#more-job-offers")
#
#     if not button or not button.has_attr('href'):
#         raise ValueError("Could not find jobboard link")
#
#     href = button['href']
#     match = re.match(r"/jobboard/(\d+)/", href)
#     if not match:
#         raise ValueError("Could not extract jobboard id from href")
#
#     return match.group(1)
#
#
# def fetch_initial_jobs(session, MAIN_URL):
#     response = session.get(MAIN_URL, headers=HEADERS)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     job_items = soup.select("li.teaser")
#
#     jobs = []
#     for item in job_items:
#         title_element = item.select_one("h3 a")
#         if not title_element:
#             continue
#
#         title = title_element.get_text(strip=True)
#         link = "https://www.mpg.de" + title_element.get("href")
#         date = item.select_one(".date").get_text(strip=True)
#         institution = item.select("div")[-1].get_text(strip=True)
#
#         jobs.append({
#             "title": title,
#             "link": link,
#             "date": date,
#             "institution": institution,
#         })
#
#     return jobs
#
#
# def fetch_more_jobs(session, base_api, start_offset=5, limit=5):
#     offset = start_offset
#     more_jobs = []
#
#     while True:
#         params = {
#             "region": "",
#             "subject": "",
#             "job_type": "",
#             "context": "jobs",
#             "limit": limit,
#             "offset": offset,
#         }
#
#         response = session.get(base_api, headers=HEADERS, params=params)
#         html = response.text.strip()
#         print(response.url)
#         print(base_api)
#
#         if not html:
#             print("No more jobs")
#             break
#
#         soup = BeautifulSoup(html, 'lxml')
#         job_items = soup.select("li.teaser")
#         if not job_items:
#             print("No more jobs")
#             break
#
#         for item in job_items:
#             title_element = item.select_one("h3 a")
#             if not title_element:
#                 continue
#
#             title = title_element.get_text(strip=True)
#             print(title)
#             link = "https://www.mpg.de" + title_element.get("href")
#             date = item.select_one(".date").get_text(strip=True)
#             institution = item.select("div")[-1].get_text(strip=True) if item.select("div") else ""
#
#             more_jobs.append({
#                 "title": title,
#                 "link": link,
#                 "date": date,
#                 "institution": institution,
#             })
#
#         offset += limit
#
#     return more_jobs

def fetch_jobs(session, MAIN_URL):
    response = session.get(MAIN_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_items = soup.select("#content-core > div > div > dl > dt:nth-child(11) dd")
    # content-core > div > div > dl > dd:nth-child(12)
    jobs = []

    for item in job_items:
        title_element = item.select_one("h3 a")
        if not title_element:
            continue

        title = title_element.get_text(strip=True)
        link = "https://www.mpg.de" + title_element.get("href")
        date = item.select_one(".date").get_text(strip=True)
        institution = item.select("div")[-1].get_text(strip=True)

        jobs.append({
            "title": title,
            "link": link,
            "date": date,
            "institution": institution,
        })

    return jobs


def main():
    session = requests.Session()

    # fetch all jobs (Static site)
    jobs = fetch_jobs(session, MAIN_URL)

    #list_id = get_jobboard_id(session, MAIN_URL)
    #base_api = f"https://www.mpg.de/jobboard/{list_id}/more_items"

    # fetch initial jobs
    #initial_jobs = fetch_initial_jobs(session, f"{MAIN_URL}")

    # fetch more jobs
    #more_jobs = fetch_more_jobs(session, base_api, start_offset=len(initial_jobs), limit=5)



    all_jobs = initial_jobs + more_jobs
    print(f"Found {len(all_jobs)} jobs")


if __name__ == "__main__":
    main()