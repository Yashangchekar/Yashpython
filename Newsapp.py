import requests

def fetch_news(api_key, category):
    url = "https://newsapi.org/v2/top-headlines"
    url1= "https://newsapi.org/v2/everything?q=tesla&from=2023-05-16&sortBy=publishedAt&apiKey=954b1d6765164deda0505fae8f4f0e96"
    params = {
        "country": "in",
        "category": category,
        "apiKey": "954b1d6765164deda0505fae8f4f0e96"
    }

    response = requests.get(url, params=params)
    response1 = requests.get(url1, params=params)

    if response.status_code == 200 or response1.status_code==200:
        data = response.json()
        articles = data["articles"]
        return articles
    else:
        print("Error:", response.status_code)
        return []

def display_news(articles):
    for article in articles:
        title = article["title"]
        source = article["source"]["name"]
        description = article["description"]
        url = article["url"]

        print("Title:", title)
        print("Source:", source)
        print("Description:", description)
        print("URL:", url)
        print()

# Set your NewsAPI key here
api_key = "954b1d6765164deda0505fae8f4f0e96"

# Prompt the user to enter the category
category = input("Enter the news category (e.g., general, sports, technology,business): ")

# Fetch and display news articles for the specified category
print(f"Fetching {category.capitalize()} news:")
articles = fetch_news(api_key, category)
display_news(articles)
