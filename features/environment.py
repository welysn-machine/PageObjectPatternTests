from behave.log_capture import capture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@capture
def before_scenario(context,scenario):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.set_page_load_timeout(20)
    context.driver.maximize_window()


@capture
def after_scenario(context,scenario):
    context.driver.quit()
