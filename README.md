# Selenium Web Scraper: JF-17 vs Rafale

This project is a simple **Selenium-based web scraping script** that extracts hyperlinks and text content from an article page discussing the comparison between the JF-17 and Rafale fighter jets.

## 📌 Features

- Opens and scrapes a news article using Selenium
- Collects all hyperlinks (`<a>` tags) from the page
- Extracts paragraph text from a specific `div` using XPath
- Saves all extracted links to a `.txt` file
- Takes a screenshot of the page

## 🛠️ Technologies Used

- Python
- Selenium
- Chrome WebDriver

📍 Target Article
Pakistan’s JF-17 Shoots Down Six Rafale Fighters
https://www.eurasiantimes.com/pakistans-jf-17-shoots-down-six-rafale-fighters-during-turkish/

⚠️ Notes & Best Practices
- Make sure your ChromeDriver version matches your Chrome browser.
- Add delays (time.sleep) or explicit waits if elements load slowly.
- Avoid running in headless mode if you encounter CAPTCHA.
- Always respect a site’s robots.txt and Terms of Service.

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install selenium
🧾 Check the outputs in the project folder:
- links.txt — all extracted hyperlinks
- img.png — screenshot of the article

