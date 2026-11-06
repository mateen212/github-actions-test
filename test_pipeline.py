from pipeline import clean_data


def test_clean_data():
    data = [" Ali ", " Ahmed ", "", "   "]

    result = clean_data(data)

    assert result == ["Ali", "Ahmed"]