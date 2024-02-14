from seleniumrequests import Firefox
from selenium.webdriver.firefox.options import Options

Options = Options()
Options.headless = True

webdriver = Firefox(options=Options)
response = webdriver.request('POST', 'https://www.omdbapi.com/', data={"t": "Superbad", "y": "2007", "plot": "short", "r": "json"})

print(response)
