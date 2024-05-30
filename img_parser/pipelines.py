from itertools import product
import logging
from time import sleep
from tqdm import tqdm
from img_parser.actors import ImagesToTensorFileLoader, ImgsLinkSearcher
from img_parser.constants import FilePathes, SearchParams
from img_parser.save_search_hist import add_searched_param_to_search_hist


def search_links_pipline(search_param: str, k=10, max_next_count: int=10):
    ils = ImgsLinkSearcher(search_param)
    for j, i in tqdm(product(range(max_next_count), range(k)), desc=f'load {search_param} images', total=max_next_count*k):
        ils.scroll_down(k=i + k*j)
        sleep(1)
    if not ils.get_more():
        return ils.get_images()
    return ils.get_images()


def full_search_pipline(searching_param):
    if not searching_param in SearchParams.searched_params:
        data = search_links_pipline(searching_param)
        logging.info(f'Get {len(data)} hrefs for images')
        ImagesToTensorFileLoader(data).load()
        add_searched_param_to_search_hist(searching_param)
