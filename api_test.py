from seleniumrequests import Firefox

webdriver = Firefox()

GREEN_COLOR = "\033[92m"

#Real Film Case
response = webdriver.request('GET', 'http://www.omdbapi.com/?apikey=5eed1a73&t=Superbad&y=2007&plot=short&r=json')
treated_response = response.json()
assert response.status_code == 200
assert treated_response['Response'] == 'True'
print(f"{GREEN_COLOR}Assertion N 1 passed successfully!")

#Wrong Year
response_2 = webdriver.request('GET', 'http://www.omdbapi.com/?apikey=5eed1a73&t=StarWars&y=2050&plot=short&r=json')
treated_response_2 = response_2.json()
assert response_2.status_code == 200
assert treated_response_2['Response'] == 'False'
print(f"{GREEN_COLOR}Assertion N 2 passed successfully!")

#Wrong Name
response_3 = webdriver.request('GET', 'http://www.omdbapi.com/?apikey=5eed1a73&t=Titanick&y=1997&plot=short&r=json')
treated_response_3 = response_3.json()
assert response_3.status_code == 200
assert treated_response_3['Response'] == 'False'
print(f"{GREEN_COLOR}Assertion N 3 passed successfully!")

#Wrong Parameters
response_4 = webdriver.request('GET', 'http://www.omdbapi.com/?apikey=5eed1a73&p=CidadedeDeus&q=8090&plot=short&r=json')
treated_response_4 = response_4.json()
assert response_4.status_code == 200
assert treated_response_4['Response'] == 'False'
print(f"{GREEN_COLOR}Assertion N 4 passed successfully!")