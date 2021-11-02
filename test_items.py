import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

locator = r'//button[@class="btn btn-lg btn-primary btn-add-to-basket"]'
def test_guest_should_see_login_link(browser, lang):
    browser.get(link)

    element = WebDriverWait(browser, 35).until(EC.visibility_of_element_located((By.XPATH, locator)))
    actual_text = element.text
    expected = {
        'es': 'Añadir al carrito',
        'fr': 'Ajouter au panier',
        'ru': 'Добавить в корзину'}

    time.sleep(5)
    assert actual_text == expected[lang]
    