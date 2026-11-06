def clean_data(data):
    cleaned = []

    for item in data:
        item = item.strip()

        if item:
            cleaned.append(item)

    return cleaned