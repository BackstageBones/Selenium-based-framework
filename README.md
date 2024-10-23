# Pytest-Assignment
Simple pytest based framework used to automate websites using selenium and Page object pattern.

## Content ##
repository consist of three folders:
- tests - which store all pytest tests
- pages - files containing each website page object pattern representation
- locators - dataclasses with websites unique element locators

## Installation guide ##
### Using docker ###
simply run \
`docker compose -f tests-compose.yaml up -d
` \
open http://localhost:5252 to see allure test report


### manual run ###
`pip install -r requirements.txt` \
`pytest --alluredir=/allure-results ./tests` \
allure installation guide: \
https://allurereport.org/docs/install-for-windows/ \
`allure serve ./allure-results`
