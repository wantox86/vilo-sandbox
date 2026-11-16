"""Fungsi teks sederhana."""


def shout(s):
    if s.endswith("!"):
        return s.upper()
    return s.upper() + "!"


def count_words(s):
    return len(s.split())
