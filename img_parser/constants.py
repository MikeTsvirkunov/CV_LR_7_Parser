from json import load
from dataclasses import dataclass
from dotenv import load_dotenv
from os import environ


load_dotenv()


with open('../search_config.json') as f:
    search_config = load(f)
with open('../image_params.json') as f:
    image_params = load(f)
with open('../searched_params.json') as f:
    searched_params = load(f)


dataclass(frozen=True)
class Archive:
    archive_name: str = environ.get('ARCHIVE_NAME')
    archive_type: str = environ.get('ARCHIVE_TYPE')


dataclass(frozen=True)
class S3Storage:
    endpoint_url: str = environ.get('S3_ENDPOINT_URL')
    aws_access_key_id: str = environ.get('S3_AWS_ACCESS_TOKEN_ID')
    aws_secret_access_key: str = environ.get('S3_AWS_ACCESS_KEY')
    bucket_name: str = environ.get('S3_BUCKET_NAME')


dataclass(frozen=True)
class FilePathes:
    driver_path: str = environ.get('DRIVER_PATH')
    logs_path: str = environ.get('LOGS_FILE')
    images_path: str = environ.get('IMAGES_PATH')


dataclass(frozen=True)
class SearchParams:
    root_link: str = search_config['root_link']
    search_params: tuple[str] = search_config['search_params']
    searched_params: tuple[str] = searched_params["searched_params"]


dataclass(frozen=True)
class ImageParams:
    shape: tuple[int, int] = (image_params['image_height'], image_params['image_width'])
    height: int = image_params['image_height']
    width: int = image_params['image_width']


        