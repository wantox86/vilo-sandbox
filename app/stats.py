def mean(values):
    """Rata-rata dari values sebagai float.

    Melempar ValueError bila values kosong.
    """
    if not values:
        raise ValueError("mean() butuh minimal satu nilai")
    return sum(values) / len(values)


def median(values):
    """Median dari values.

    Untuk jumlah elemen genap, hasilnya rata-rata dua nilai tengah.
    Melempar ValueError bila values kosong.
    """
    if not values:
        raise ValueError("median() butuh minimal satu nilai")
    ordered = sorted(values)
    count = len(ordered)
    middle = count // 2
    if count % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2
