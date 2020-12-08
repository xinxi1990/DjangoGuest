from playwright import sync_playwright

def run(playwright):
    browser = playwright.webkit.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input[name="wd"]
    page.click("input[name=\"wd\"]")

    # Fill input[name="wd"]
    page.fill("input[name=\"wd\"]", "ce")

    # Click text="测网速"
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%B5%8B%E7%BD%91%E9%80%9F&fenlei=256&rsv_pq=96c31f9f00069c6c&rsv_t=38cetvYKzJMOmZeqcJhCp5VbMk1qL1Eg5IMq5pa%2F7oJqsoWWd%2BBJdLzQtfs&rqlang=cn&rsv_enter=1&rsv_dl=ts_2&rsv_sug3=3&rsv_sug1=1&rsv_sug7=100&rsv_sug2=1&rsv_btype=i&prefixsug=ce&rsp=2&inputT=4700&rsv_sug4=7171"):
    with page.expect_navigation():
        page.click("text=\"测网速\"")

    # Click text="测速网"
    # with page.expect_navigation(url="https://www.speedtest.cn/"):
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.click("text=\"测速网\"")
        page1 = popup_info.value

    # Close page
    page.close()

    # Close page
    page1.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)