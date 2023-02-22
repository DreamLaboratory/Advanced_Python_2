import logging

# configure logging
logger = logging.getLogger(__name__)
# set level
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler('error.log')
handler.setLevel(logging.ERROR)

# create a logging format
dest_time = '%Y-%m-%d %H:%M:%S %p'
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt=dest_time)

# add the handlers 
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

def my_logger(original_func):


    def wrapper(*args, **kwargs):
        try:
            result = original_func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(f'Error: {e}')
            return f'Error: {e}'
    return wrapper

