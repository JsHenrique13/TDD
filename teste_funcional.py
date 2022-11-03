from selenium import webdriver

nav = webdriver.Chrome()
nav.get('http://localhost:8000')

assert 'Django' in nav.title
