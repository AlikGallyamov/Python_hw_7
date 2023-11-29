from selene import browser, query
import zipfile, os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

os.mkdir("files")
os.mkdir("resource")

CURRENT_PATH = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_PATH)
source_dir = os.path.join(CURRENT_DIR, "files")
resource_dir = os.path.join(CURRENT_DIR, "resource")
files_name = os.listdir(source_dir)

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": source_dir,
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver


def download_csv():
    browser.open("https://github.com/AlikGallyamov/Python_hw_7/blob/main/original/exampleCSV.csv")
    download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    content = requests.get(url=download_url).content
    with open(os.path.join(source_dir, "exampleCSV.csv"), 'wb') as file:
        file.write(content)



def download_pdf():
    browser.open("https://github.com/AlikGallyamov/Python_hw_7/blob/main/original/examplePdf.pdf")
    browser.element("[data-testid=download-raw-button]").click()
    time.sleep(3)


def download_xlsx():
    browser.open("https://github.com/AlikGallyamov/Python_hw_7/blob/main/original/exampleXLSX.xlsx")
    download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    content = requests.get(url=download_url).content
    with open(os.path.join(source_dir, "exampleXLSX.xlsx"), 'wb') as file:
        file.write(content)



def create_zip_files():

    with zipfile.ZipFile(resource_dir + '/test.zip', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in files_name:
            add_file = os.path.join("files", file)
            zf.write(add_file)



