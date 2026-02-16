# SciScrape

**SciScrape** is a work-in-progress Python tool designed to scrape scientific job postings from various institutional job boards and deliver a daily digest directly to your inbox.

##  Description

Finding research positions, especially postdoc jobs relevant to your field, is a tedious process. I spent many hours cycling through the job boards on several university and institute websites during my own job search. As a fun side-project, I decided to create a tool to automate some of this, while also building familiarity with web scraping and deepening my Python skills.  
"SciScrape" was made to help with:
1.  Fetching job listings from configured institutional websites (e.g., Humboldt University, Max Planck Institute).
2.  Filtering and parsing the job data.
3.  Generating a clean, HTML-formatted email digest.
4.  Sending the digest to your email address.

## Features

*   **Automated Scraping**: currently supports parsing for Humboldt University (HU) and Max Planck Institute (MPI) job boards. 
            (At least, it did in late-2025. The HU job board has recently gotten a significant overhaul, so no guarantees there!)
*   **Email Notifications**: Sends a daily summary of new job postings using SMTP.
*   **Configurable**: Easily add new sites or change user details via `config.json`.
*   **HTML Templates**: Uses Jinja2 to render beautiful email reports.

## Setup & Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd SciScrape
    ```

2.  **Install dependencies**:
    Ensure you have Python installed. You will need the following packages:
    *   `requests`
    *   `beautifulsoup4`
    *   `python-dotenv`
    *   `jinja2`
    *   `lxml` (optional, but recommended for BeautifulSoup)

    You can install them via pip:
    ```bash
    pip install requests beautifulsoup4 python-dotenv jinja2 lxml
    ```

3.  **Environment Variables**:
    Create a `.env` file in the root directory to store your email credentials:
    ```env
    SENDER_EMAIL=your_email@gmail.com
    APP_PASSWORD=your_google_app_password
    ```

4.  **Configuration**:
    Update `config.json` with your details and target sites:
    ```json
    {
      "user_name": ["Your Name"],
      "user_email": "your.email@example.com",
      "sites": [  ]
    }
    ```

## Usage

Run the main script to scrape the configured sites and send the email:

```bash
python main.py
```

## Project Structure

*   `main.py`: The entry point of the application. Orchestrates scraping and emailing.
*   `config.json`: Configuration file for user details and site URLs.
*   `parser_hu.py`: Scraper logic for Humboldt University.
*   `parser_mpi.py`: Scraper logic for Max Planck Institute.
*   `emailer.py`: Handles SMTP email sending.
*   `email_template.py`: Generates the HTML email content.

## Work in Progress

This project is currently under (semi-)active development.
*   Support for more institutions (Charité, FU Berlin, TU Berlin) is planned.
*   Refactoring of scraper logic to be more modular.
*   Improved keyword filtering.

---
*Happy job hunting! :)*
