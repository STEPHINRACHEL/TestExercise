# Test Automation using Python and Selenium
This repository contains a functionality test for verifying an e-commerce site.

### Pre-requisite

Install
- Python3
- Selenium Webdriver
- Chrome / Firefox / Edge / Safari Webdrivers

### How to run

1. Set this optional environment variable if you want to change browser and default browser is set to Chrome.
```
export BROWSER=edge 
```

2. Execute from the root of this repository
```
pytest test_e_shop.py --verbose --capture=no
```
