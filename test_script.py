from selenium import webdriver
from desired_capabilities import DesiredCapabilities
import pytest



# Specify Hub details and required capabilities, based on the provided capabilities hub will select node
def get_driver():
	browser_name = pytest.config.getoption("--browser").upper()
	capabilities = DesiredCapabilities.FIREFOX
	if browser_name == "CHROME":
		capabilities = DesiredCapabilities.CHROME
	driver = webdriver.Remote(
        command_executor="http://192.168.201.164:4445/wd/hub",
        desired_capabilities=capabilities)
	driver.maximize_window()
	import requests
	vnc_url = "{hub_url}grid/api/testsession?session={session_id}".format(
        hub_url=driver.command_executor._url[:-6],
        session_id=driver.session_id
        )
	req = requests.post(vnc_url)
	node_info = req.json()
	local_ip = node_info['proxyId']
	vnc_address =  "vnc" + local_ip[4:] + "1"
	print ('VNC address is {}').format(vnc_address.split('vnc://')[1])
	return driver

def test_one():
	driver = get_driver()
	driver.get("http://www.python.org")
	driver.quit()

def test_two():
	driver = get_driver()
	driver.get("http://www.google.com")
	driver.quit()
def test_three():
	driver = get_driver()
	driver.get("https://surveymonkey.slack.com")
	driver.quit()
def test_four():
	driver = get_driver()
	driver.get("https://www.monkeytest1.com/")
	driver.quit()

def test_five():
	driver = get_driver()
	driver.get("https://www.monkeytest.com/")
	driver.quit()
