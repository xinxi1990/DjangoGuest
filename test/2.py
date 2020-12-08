from playwright import sync_playwright

with sync_playwright() as p:
    print('11')
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        page = browser.newPage()
        page.goto('http://www.baidu.com')
        print('222')
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()

