import wikipedia


moskau = wikipedia.page("Moscow")
summary = wikipedia.WikipediaPage(title="Moscow", pageid=None, redirect=True, preload=False)
print(moskau.title)
print(moskau.url)
print(moskau.content)
