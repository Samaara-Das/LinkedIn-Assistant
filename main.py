
# import modules
from logger_setup import *
from traceback import print_exc
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException

# Set up logger for this file
logger = setup_logger(__name__, INFO)

laptop_init = {'path': 'C:\\Users\\pripuja\\AppData\\Local\\Google\\Chrome\\User Data', 'profile': 'Profile 1'}
desktop_init = {'path': 'C:\\Users\\Puja\\AppData\\Local\\Google\\Chrome\\User Data', 'profile': 'Profile 2'}

inits = [laptop_init, desktop_init]

# class
class Browser:

	def __init__(self, keep_open: bool, headless: bool, init: int =0,) -> None:
		chrome_options = Options() 
		if headless:
			chrome_options.add_argument('--headless') 
		chrome_options.add_experimental_option("detach", keep_open)
		chrome_options.add_argument(f"--profile-directory={inits[init]['profile']}")
		chrome_options.add_argument(f"--user-data-dir={inits[init]['path']}")
		self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

	def open_page(self, url: str):
		'''This opens `url` and maximizes the window'''
		try:
			self.driver.get(url)
			self.driver.maximize_window()
			return True
		except WebDriverException:
			logger.exception(f'Cannot open this url: {url}. Error: ')
			return False 

browser = Browser(True, False)
browser.open_page('https://www.linkedin.com/feed/')