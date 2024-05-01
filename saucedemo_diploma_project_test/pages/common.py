import allure
from selene import browser, have

from saucedemo_diploma_project_test.data.products import Product


def select_product(product: Product):
    with allure.step('Select product'):
        browser.element(product.id).click()


def product_details_match_selected_product(product: Product):
    with allure.step('Verify product details match selected product'):
        browser.element('[data-test=inventory-item-name]'
                        ).should(have.text(product.name))
        browser.element('[data-test=inventory-item-price]'
                        ).should(have.text(product.price))