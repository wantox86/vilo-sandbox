"""Fungsi hitung sederhana."""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("pembagian dengan nol")
    return a / b
