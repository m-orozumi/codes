from scrape_code import retrieve

def test_scraping_function():
    # テストの実装
    result = retrieve()
    
    # スクレイピング結果が空でないことを確認
    assert len(result) > 0