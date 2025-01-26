# Pytest-Assignment
Simple pytest based framework used to automate websites using selenium and Page object pattern.

## Content ##
repository consist of three folders:
- tests - which store all pytest tests
- pages - files containing each website page object pattern representation
- locators - dataclasses with websites unique element locators

## Installation guide ##
### Using docker ###

Step 1: Build the Docker image
 docker build -t selenium-tests . 

Step 2: Run the Docker container
docker run --rm -p 4040:4040 selenium-tests


### manual run ###
`pip install -r requirements.txt` \
`pytest --alluredir=/allure-results ./tests` \
allure installation guide: \
https://allurereport.org/docs/install-for-windows/ \
`allure serve ./allure-results`
