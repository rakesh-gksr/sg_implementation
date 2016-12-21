"""
The Desired Capabilities implementation.
"""

class DesiredCapabilities(object):
    """
    Set of default supported desired capabilities.
    Usage Example:
        from selenium import webdriver
        selenium_grid_url = "http://192.168.201.164:4444/wd/hub"
        # Create a desired capabilities object as a starting point.
        capabilities = DesiredCapabilities.FIREFOX()
        capabilities['platform'] = "MAC"
        capabilities['version'] = "46"
        # Instantiate an instance of Remote WebDriver with the desired capabilities.
        driver = webdriver.Remote(desired_capabilities=capabilities,
                                  command_executor=selenium_grid_url)
    """

    FIREFOX = {
        "browserName": "firefox",
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
        "marionette": False,
    }
    CHROME = {
        "browserName": "chrome",
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
    }