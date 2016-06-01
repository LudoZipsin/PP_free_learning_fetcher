#! /usr/bin/env python3

# dependencies: robobrowser (pip3 install robobrowser)

from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import requests
import sys

custom_user_agent = "Mozilla/5.0"

url_domain = "https://www.packtpub.com"
url_free_learning = "/packt/offers/free-learning"

pattern_free_ebook = "/freelearning-claim/"

form_id = "packt-user-login-form"

user_mail = "to complete"
user_password = "to complete"


if __name__ == "__main__":

    # init. We make a browser with user agent firefox
    browser = RoboBrowser(user_agent=custom_user_agent, parser="lxml")

    # opening the url
    browser.open(url_domain + url_free_learning)

    # fetching the form and filling it
    login_form = browser.get_form(id=form_id)
    login_form["email"].value = user_mail
    login_form["password"].value = user_password

    # submit the form
    browser.submit_form(login_form)

    # fetching the free ebook claiming url
    response = requests.get(url_domain + url_free_learning, headers={'User-Agent': custom_user_agent})
    soup = BeautifulSoup(response.text, "html.parser")
    url_link = None

    for link in soup.find_all('a'):
        if pattern_free_ebook in str(link.get('href')):
            url_link = link.get('href')

    if url_link is None:
        sys.exit('Unable to fetch free ebook claim link')

    browser.open(url_domain + url_link)
