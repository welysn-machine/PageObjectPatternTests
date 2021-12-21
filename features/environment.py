from behave.log_capture import capture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

@capture
def before_scenario(context,scenario):

    os.environ['GH_TOKEN'] = "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"
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    print(scenario.name)
    context.driver.implicitly_wait(20)
    context.driver.set_page_load_timeout(40)
    context.driver.maximize_window()


@capture
def after_scenario(context,scenario):
    context.driver.quit()
