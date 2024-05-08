from scrape_code import retrieve


def test_scraping_function():
    # テストの実装
    url = "https://zdh.stagingbridge.net/"

    result = retrieve(url)

    assert result == {
        'title': ["xxx"],
        'link': ["yyyy"],
    }