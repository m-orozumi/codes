from scrape_code import retrieve

def test_scraping_function():
    # テストの実装
    html = "https://zdh.stagingbridge.net/?s=AWS"
    result = retrieve(html)
    assert result is not None