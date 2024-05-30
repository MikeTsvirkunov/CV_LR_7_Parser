import logging
import sys
sys.path.append("./")
sys.path.append("../")
from img_parser.pipelines import full_search_pipline
from img_parser.push_to_s3 import push_to_s3_storage
from img_parser.constants import Archive, FilePathes, SearchParams
from img_parser.initiators import driver_initiation
import shutil


logging.basicConfig(level=logging.INFO, filename=FilePathes.logs_path,filemode="w")
driver_initiation()


if __name__ == '__main__':
    for param in SearchParams.search_params:
        full_search_pipline(param)
    logging.info('Start of archive creation')
    shutil.make_archive(
        base_name=Archive.archive_name, 
        format=Archive.archive_type, 
        root_dir='../',
        base_dir='images/',
    )
    logging.info('End of archive creation')
    logging.info('Sart pushing to S3 storage')
    push_to_s3_storage()
    logging.info('End pushing to S3 storage')
