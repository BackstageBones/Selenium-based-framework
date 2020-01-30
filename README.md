# Pytest-Assignment
a simple selenium based framework used to automate local HTML files
Prepared to run with Chrome browser v.79
in order to run test with different chrome version please replace the file 'chromedriver.exe' inside ENV folder with the one,
suitable for you. You can download appropriate driver from selenium official website here:
https://chromedriver.chromium.org/downloads
You need to replace two file paths inside test_index2.py with your actual absolute path:
test_path = r"PUT YOUR ABSOLUT PATH TO THIS FILE HERE"
chrome_path = r"PUT YOUR ABSOLUT PATH TO THIS FILE HERE"
In future it will be simplified and pytest fixtures will be put in a separete place called conftest.
Also main class Envirenment initialisation will be moved outside test class.
