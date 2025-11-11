import requests
from bs4 import BeautifulSoup
import re

MAIN_URL = "https://haushalt-und-personal.hu-berlin.de/de/personal/stellenausschreibungen"
HEADERS = {"User-Agent": "Mozilla/5.0",
           "X-Requested-With": "XMLHttpRequest"
           }

def fetch_jobs(session, MAIN_URL):

    response = session.get(MAIN_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    #job_items = soup.select("#content-core > div > div > dl > dt:nth-child(11) dd")
    #job_items = soup.select("#content-core > div > div > dl > dt:nth-child(11) dd")
    job_items = soup.find('dl', class_='jobListing')

    if job_items:
        jobs = []
        scientific_header = job_items.find('dt', string=re.compile(r'Wissenschaftliches Personal'))

        if scientific_header:
            # 3. Iterate through all the individual job blocks (<dd> tags)
            # We use .find_next_siblings() to get the job items that follow the header
            # We stop when we hit the next <dt> tag (the next category)

            for sibling in scientific_header.next_siblings:
                # Skip NavigableString objects (whitespace, newlines)
                if sibling.name is None:
                    continue
                # If the sibling is the next category header (<dt>), break the loop
                if sibling.name == 'dt':
                    break
                if sibling.name == 'dd':
                    item = sibling

                    title_element = item.select_one("a")
                    if not title_element:
                        continue

                    title = title_element.get_text(strip=True)
                    link = title_element.get("href")

                    institution_tag = item.find('p')
                    if institution_tag:
                        # .text gets all the text content, and .strip() cleans up whitespace/newlines
                        institution = institution_tag.text.strip()
                    else:
                        institution = "N/A - Institution not found"

                    for small_tag in item.find_all('small'):
                        # Check if this <small> tag contains the text "Bewerbung bis:"
                        if 'Bewerbung bis:' in small_tag.text:
                            deadline_section = small_tag
                            break
                    else:
                        deadline_section = None  # None if loop finishes without break

                    #  extract the date from nested <span>
                    date = "N/A - Deadline not found"
                    if deadline_section:
                        deadline_span = deadline_section.find('span')
                        if deadline_span:
                            date = deadline_span.text.strip()

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

    all_jobs = jobs
    print(f"Found {len(all_jobs)} jobs")


if __name__ == "__main__":
    main()