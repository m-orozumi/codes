from scrape_code import retrieve

def test_scraping_function():
    # テストの実装
    url = "https://zdh.stagingbridge.net/?s=AWS"
    result = retrieve(url)
    
    # スクレイピング結果が空でないことを確認
    assert len(result) > 0