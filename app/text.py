"""Fungsi teks sederhana."""


def shout(s):
    return s.upper() + "!"


def count_words(s):
    return len(s.split())


def slugify(s):
    s = s.strip().lower()
    s = s.replace(" ", "-").replace("_", "-")
    return "".join(ch for ch in s if (ch.isalnum() and ch.isascii()) or ch == "-")
