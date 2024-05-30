from io import BytesIO
from itertools import product
from time import sleep
import logging
import ioc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import torch
from tqdm import tqdm
from img_parser.constants import FilePathes, ImageParams, SearchParams
from PIL import Image
import requests
from torchvision.transforms.functional import pil_to_tensor
from uuid import uuid4


class ImgsLinkSearcher:
    def __init__(self, search_param):
        self.search_param = search_param
        self.driver = ioc.require('HH.Registration.WebDrivers.Main')
        self.wait = ioc.require('HH.Registration.Waiters.Std')
        link = self.make_search_imgages(search_param)
        self.driver.get(link)
        logging.info(f'Search on param: {search_param},\tresult link: {link}')

    @staticmethod
    def make_search_imgages(search_param):
        return SearchParams.root_link + search_param

    def get_images(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ContentImage-Image'))
        )
        elements = self.driver.find_elements(By.CLASS_NAME, 'ContentImage-Image')
        return [el.get_attribute('src') for el in tqdm(elements, desc='Searching hrefs')]

    def get_more(self) -> bool:
        try:
            self   .wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'FetchListButton-Button'))
            ).click()
            return True
        except:
            return False

    def scroll_down(self, k=0, h=16000):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ContentImage-Image'))
        )
        self.driver.execute_script(f"window.scrollTo({k*h}, {(k+1)*h})")


class ImagesToTensorFileLoader:
    def __init__(self, links):
        self.links = links
    
    def load(self):
        for link in tqdm(self.links, desc='saving'):
            response = requests.get(link)
            tensor = pil_to_tensor(Image.open(BytesIO(response.content)).resize(ImageParams.shape))
            torch.save(tensor, FilePathes.images_path + str(uuid4()) + '.pt')

