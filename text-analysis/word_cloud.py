from typing import List, Set

from matplotlib import pyplot as plt
from nltk import word_tokenize
from pymorphy2 import MorphAnalyzer
from wordcloud import WordCloud


def tokenize_text(text_: str, special_chars: tuple) -> List[str]:
    """
    Excludes special characters from the text, splits the text into tokens and returns a list of tokens.
    :param text_: source text
    :param special_chars: special characters that should be excluded from the text
    :return: list of tokens
    """

    tokens: List[str] = word_tokenize(''.join([ch for ch in text_ if ch not in special_chars]))

    return tokens


def lemmatize_tokens(tokens_: List[str], u_stopwords: List[str]) -> List[str]:
    """
    Excludes stop words from the list of tokens, convert the remaining tokens to their normal form and returns them.
    :param tokens_: list of tokens
    :param u_stopwords: list of stop words
    :return: list of words in their normal form
    """

    morph: MorphAnalyzer = MorphAnalyzer()

    res: List[str] = [morph.normal_forms(token)[0] for token in tokens_ if token not in u_stopwords]

    return res


def lemma_list_to_text(lemma: List[str]) -> str:
    """
    Collects lemmas into a string and returns it.
    :param lemma: list if lemmas
    :return: string of lemmas
    """

    text_: str = ' '.join(lemma)

    return text_


def make_wordcloud(txt: str, u_stopwords: Set[str], words_qty=100) -> WordCloud:
    """
    Make wordcloud from the text.
    :param txt: text from lemmas
    :param u_stopwords: list of russian stop words
    :param words_qty: max quantity of words
    :return: wordcloud object
    """

    w_cloud: WordCloud = WordCloud(
        width=1600,
        height=800,
        max_words=words_qty,
        min_word_length=4,
        stopwords=u_stopwords,
        collocations=False
    ).generate(txt)

    return w_cloud


def show_figure(w_cloud: WordCloud) -> None:
    """
    Shows the wordcloud figure.
    :param w_cloud: wordcloud of words
    """

    plt.figure(figsize=(20, 10), facecolor='k')
    plt.imshow(w_cloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
