#%%
import datetime
import csv
from  textblob import TextBlob


key = "Dz5yaMjXArC5mR8IKpOVzCQuy8ui1bUY"
from pynytimes import NYTAPI

nyt = NYTAPI(key, parse_dates = True)
companies = ["Delta Airlines", "American Airlines", "Spirit Airlines", "United Airlines", "Jetblue Airlines"]

date_range = {"begin":datetime.datetime(2020,1,1), "end":datetime.datetime(2023,1,1)}


with open("Airlines.csv", "w") as f: 
    f.write("Date, Company, Abstract, Score\n")
    writer = csv.writer(f)
    for company in companies: 
        articles = nyt.article_search(query=company, results=200, dates=date_range)
        for article in articles: 
            abstract = article["abstract"]
            pub_date = article["pub_date"]
            #write code to get the sentiment score
            blob = TextBlob(abstract)
            score = blob.sentiment.polarity
            writer.writerow([pub_date,company,abstract,score])

