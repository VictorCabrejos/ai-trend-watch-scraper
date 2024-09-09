
# AI-Trend-Watch-Scraper

## Overview
**AI-Trend-Watch-Scraper** is a multi-part Python project aimed at building a comprehensive AI news scraping and analysis tool. This project will scrape AI-related news articles, perform sentiment analysis, and visualize trends in artificial intelligence. Over the course of several live streams, we will start with a basic web scraping assignment and gradually build out more advanced features, including trend tracking and predictive analytics.

**Follow the series on my Facebook page:** [Python Programming, Machine Learning & MLOps and Data Science](https://www.facebook.com/pythonfordatascience)

## Goals
By the end of this project, the AI-Trend-Watch-Scraper will be able to:
- Scrape AI news articles from various sources.
- Analyze sentiment within the articles to determine overall positive, neutral, or negative tones.
- Track trends in AI topics over time.
- Predict future trends based on historical data.
- Provide an interactive dashboard for real-time analysis and visualization.

## Project Structure
The project will evolve in the following steps:
### Step 1: Basic Web Scraping Assignment
- Scrape at least 60 AI-related articles from three separate searches using BeautifulSoup or similar libraries.
- Combine the results into a single dataset and write the data to a CSV file.
- Perform basic analysis to count the occurrences of each search string in the titles.

### Step 2: Sentiment Analysis
- Apply machine learning to perform sentiment analysis on the scraped articles.
- Determine whether the overall tone of AI-related articles is positive, negative, or neutral.

### Step 3: Trend Tracking & Visualization
- Track the frequency of specific AI topics over time (e.g., "machine learning," "GPT models").
- Generate visualizations such as line graphs and bar charts to show the most popular AI trends.

### Step 4: Predictive Analytics
- Build a predictive model to forecast future trends in AI based on historical news data.
- Integrate predictive analytics into the dashboard to provide insights into where AI topics are heading.

### Step 5: Web App & Interactive Dashboard
- Develop a Flask/Streamlit web app to allow users to interact with scraped data and view real-time visualizations.
- Provide features such as keyword searches, trend exploration, and the ability to download datasets.

## Installation & Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VictorCabrejos/ai-trend-watch-scraper.git
   cd ai-trend-watch-scraper
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the basic scraping script** (for Step 1):
   ```bash
   python basic_assignment/scraper.py
   ```

5. **Follow the live series for the next steps** on my [Facebook page](https://www.facebook.com/pythonfordatascience).

## Future Features
- Incorporate more AI-focused news sources to diversify the scraped data.
- Implement deep learning models for more advanced sentiment analysis.
- Add email notifications for users to receive AI news updates based on specific topics.
- Integrate the web app with cloud storage for large-scale data handling.

## Contributing
Contributions are welcome! If you would like to contribute, please create a pull request or submit an issue to discuss potential features or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Follow the Series
- **Facebook**: [Python Programming, Machine Learning & MLOps and Data Science](https://www.facebook.com/pythonfordatascience)
- **GitHub**: [AI-Trend-Watch-Scraper](https://github.com/VictorCabrejos/ai-trend-watch-scraper)
