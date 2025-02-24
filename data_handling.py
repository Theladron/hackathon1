import wikipedia


def get_complete_page():
    site = wikipedia.page("Python")
    return site.content


def get_page_summary(pagename):
    site = wikipedia.page(pagename)
    return site.summary



