import wikipedia

site = wikipedia.page("Berlin")

print(site.content) # page object
print(site.categories)  # list of str
