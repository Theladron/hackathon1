import wikipedia
import random

def get_pagename():
    """
    Wählt zufällig einen Artikel aus der vordefinierten Kategorie-Liste aus.
    """
    categories = [
        "Germany", "USA", "Brasil", "Japan", "France", "England", "Türkiye", "Norway", "Spain", "China",
        "Basketball", "Football", "Tennis", "Rugby football", "Swimming","Bowling","Badminton","Golf","Baseball","Boxing",
        "Lion", "Elephant", "Giraffe", "Penguin", "Tiger", "Kangaroo", "Dolphin", "Zebra", "Monkey", "Bear",
        "Python (programming language)", "Science", "Research", "Computer", "Smartphone","Technology","Algorithm","Database","Cache (computing)","Server (computing)"
    ]

    # Wähle zufällig ein Titel
    pagename = random.choice(categories)
    return pagename


def get_complete_page():
    pagename = get_pagename()
    site = wikipedia.page(pagename, auto_suggest=False)
    return site.content, pagename


def get_page_summary(pagename):
    site = wikipedia.page(pagename, auto_suggest=False)
    return site.summary



