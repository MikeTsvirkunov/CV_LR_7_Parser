from json import load
from dataclasses import dataclass
from dotenv import load_dotenv
from os import environ


load_dotenv()


with open('../search_config.json') as f:
    search_config = load(f)
with open('../image_params.json') as f:
    image_params = load(f)


dataclass(frozen=True)
class FilePathes:
    driver_path: str = environ.get('DRIVER_PATH')
    logs_path: str = environ.get('LOGS_FILE')
    images_path: str = environ.get('IMAGES_PATH')


dataclass(frozen=True)
class SearchParams:
    root_link: str = search_config['root_link']
    search_params: tuple[str] = search_config['search_params']


dataclass(frozen=True)
class ImageParams:
    shape: tuple[int, int] = (image_params['image_height'], image_params['image_width'])
    height: int = image_params['image_height']
    width: int = image_params['image_width']


        