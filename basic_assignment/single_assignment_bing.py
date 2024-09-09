import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# **************  Scraping Bing News with Selenium  **************


def selenium_scraper(search_string):
    chrome_options = Options()
    chrome_options.add_argument(
        "--headless"
    )  # Run headless to avoid opening the browser window
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Go to Bing News
    driver.get("https://www.bing.com/news")

    # Use explicit wait to ensure the <input> is present before interacting
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sb_form_q"))
        )
        search_box.send_keys(search_string)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)
    except Exception as e:
        print("Error: ", e)

    # Wait for the page to load after the search
    time.sleep(5)

    # Scroll down to load more results
    for _ in range(5):  # Scroll 5 times (tune this as needed)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    # Extract article titles and descriptions
    data = []
    try:
        articles = driver.find_elements(By.CLASS_NAME, "title")
        descriptions = driver.find_elements(By.CLASS_NAME, "snippet")

        # Combine titles and descriptions
        for i in range(min(len(articles), len(descriptions))):
            title = articles[i].text
            summary = descriptions[i].text
            data.append(
                {"title": title, "summary": summary, "search_string": search_string}
            )

    except Exception as e:
        print("Error extracting titles or descriptions:", e)

    driver.quit()

    # Convert the data to a DataFrame
    return pd.DataFrame(data)


# **************  Creating 3 tables  **************

# List of search strings
search_strings = ["Artificial Intelligence", "Machine Learning", "Deep Learning"]

# Create individual DataFrames for each search string
df_ai = selenium_scraper(search_strings[0])
df_ml = selenium_scraper(search_strings[1])
df_dl = selenium_scraper(search_strings[2])

# Concatenate the three DataFrames into one
df_all = pd.concat([df_ai, df_ml, df_dl], ignore_index=True)

# Save the concatenated DataFrame to a CSV
df_all.to_csv("results/combined_articles.csv", index=False)

print(f"Combined DataFrame has {len(df_all)} rows.")


# **************  Count Occurrences of Search Strings in Titles  **************

import re


# Count occurrences of each search string in titles
def count_search_strings(df, search_strings):
    counts = {}
    for search_string in search_strings:
        pattern = re.compile(re.escape(search_string), re.IGNORECASE)
        count = df["title"].apply(lambda title: len(pattern.findall(title))).sum()
        counts[search_string] = count
    return counts


counts = count_search_strings(df_all, search_strings)
print(counts)  # Debugging


# **************  Create the Bar Plot  **************

import matplotlib.pyplot as plt


# Create a bar plot
def plot_counts(counts):
    # Create a list of colors, one for each bar
    colors = ["blue", "green", "red"]  # You can add more colors if needed

    # Plot the bars with the specified colors
    plt.bar(counts.keys(), counts.values(), color=colors)

    plt.xlabel("Search Strings")
    plt.ylabel("Occurrences in Titles")
    plt.title("Occurrences of Search Strings in Article Titles")

    # Save the plot
    plt.savefig("results/search_string_counts.png", dpi=300)
    plt.show()


plot_counts(counts)
