import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
import ssl

# Function to check if the website is using HTTPS
def check_https(url):
    response = requests.get(url)
    return response.url.startswith("https")

# Function to check if the website is responsive (mobile-friendly)
def check_responsive(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    return "viewport" in response.text.lower()

# Function to check if the website has an XML sitemap
def check_sitemap(url):
    sitemap_url = urllib.parse.urljoin(url, "sitemap.xml")
    response = requests.get(sitemap_url)
    return response.status_code == 200

# Function to check if the website has a robots.txt file
def check_robots_txt(url):
    robots_url = urllib.parse.urljoin(url, "robots.txt")
    response = requests.get(robots_url)
    return response.status_code == 200

# Function to check if the website uses SSL/TLS
def check_ssl(url):
    try:
        ssl._create_default_https_context = ssl._create_default_https_context  # Ignore SSL certificate errors
        response = requests.get(url)
        return response.url.startswith("https")
    except:
        return False

# Function to check for broken links in the website
def check_broken_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a", href=True)
    broken_links = []
    for link in links:
        try:
            response = requests.get(link["href"])
            if response.status_code != 200:
                broken_links.append(link["href"])
        except:
            broken_links.append(link["href"])
    return broken_links

# Function to check website speed (requires requests and requests_html packages)
def check_website_speed(url):
    from requests_html import HTMLSession
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=2, timeout=30)
    return response.html.html

# Replace "your_wordpress_website_url" with the actual URL of the WordPress website you want to check
wordpress_url = "https://www.w3care.com"

# Perform checks
print("Is the website using HTTPS?", check_https(wordpress_url))
print("Is the website responsive?", check_responsive(wordpress_url))
print("Does the website have an XML sitemap?", check_sitemap(wordpress_url))
print("Does the website have a robots.txt file?", check_robots_txt(wordpress_url))
print("Is the website using SSL/TLS?", check_ssl(wordpress_url))
#print("Broken links in the website:", check_broken_links(wordpress_url))
print("Website speed analysis:", check_website_speed(wordpress_url))  # Uncomment this line if you have the required packages

