import requests


def NewsFromBBC():
    # BBC news api
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apikey=0aaa2570f9a240a497b79d459ae63fd4"

    l_news = ""
    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in article:
        l_news+= ("Title: " + i['title'] + "\n" +
              "Description: " + i['description'] + "\n" +
              "URL: " + i['url'] + "\n")


    return l_news

message = NewsFromBBC()
