
import requests
from bs4 import BeautifulSoup
import webbrowser
import pandas as pd
from google.colab import files

res = requests.get("https://review-of-my-life.blogspot.com/")
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())

a_tags = soup.find_all("h3", {"class": "post-title"})
for tag in a_tags:
    print(tag.a.string)

columns = ['name', 'url']
df = pd.DataFrame(columns=columns)
print(df)

se = pd.Series(['example-1',
                'https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'], columns)

df = df.append(se, columns)


columns = ["Name", "Url"]
df1 = pd.DataFrame(columns=columns)


se = pd.Series(
    ['example-2', 'https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'], columns)
df1 = df1.append(se, columns)
se = pd.Series(['example-3',
                'https://review-of-my-life.blogspot.com/2018/04/sqlite3.html'], columns)
df1 = df1.append(se, columns)
se = pd.Series(['example-4',
                '	https://review-of-my-life.blogspot.com/2018/03/moji-okosi-1.html'], columns)
df1 = df1.append(se, columns)
df1
