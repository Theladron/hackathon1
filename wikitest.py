import wikipedia
import colored_text
import random


WIKI_LANGUAGE = "en"
SUMMARY_SENTENCES = 1       # Number of sentences to retrieve from wikipages´ summary


def find_random_titles(number):
    wikipedia.set_lang(WIKI_LANGUAGE)
    summaries = {}
    titles = []
    title_collection = wikipedia.random(pages = number)
    return title_collection


def add_summaries_to_random_titles(title_collection):
        title_list = []



        request_single_summary(title)
        try:
            for title in title_collection:
                summaries[title] = wikipedia.summary(title)
        except wikipedia.DisambiguationError as e:
            random_title = random.choice(e.options)
            summaries[random_title] = wikipedia.summary(random_title, sentences = 1)
        except wikipedia.exceptions.PageError:
            if len(summaries.keys()) == 0:
                new_title = wikipedia.random(pages = 1)
                summaries[new_title] = wikipedia.summary(new_title, sentences = 1)
            else:
                pass
        for title in summaries.keys():
            title_list.append(title)
        return title_list


def request_single_summary(title):
    try:
        site_summary = wikipedia.summmary(title, sentences = SUMMARY_SENTENCES)
    except wikipedia.DisambiguationError as e:
        random_title = random.choice(e.options)
        site_summary = wikipedia.summary(random_title, sentences = SUMMARY_SENTENCES)
    except wikipedia.exceptions.PageError:
        new_title = wikipedia.random(pages = 1)
        site_summary = wikipedia.summary(new_title, sentences = SUMMARY_SENTENCES)
    return site_summary, title





