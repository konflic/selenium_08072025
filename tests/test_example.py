def test_administration_title(browser, base_url):
    browser.get(f"{base_url}/administration/")
    assert "Administration" == browser.title


def test_main_title(browser, base_url):
    browser.get(base_url)
    assert "Your Store" == browser.title
