import time


##Terminar depois

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    nav = p.firefox.launch(headless=False)
    pg = nav.new_page()
    pg.goto('https://www.youtube.com')
    time.sleep(3)
    pg.locator('xpath=//*[@id="search"]').click()
    pg.fill('xpath=/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/div/div[2]/input', "pão")
    pg.locator('xpath=/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/div/div[2]/input').click()
    time.sleep(20)