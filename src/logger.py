from datetime import datetime
import logging.handlers
import logging
import os,sys

class Logger(object):

    def __init__(self):
        # Ensure the folder Path is Valid
        cwd = os.getcwd()
        log_folder = ("/x/logs/")
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        # Set Global Log Path
        self.log_location = ("/x/logs/")

    def log(self):
        current_time = datetime.now()
        current_date = current_time.strftime("%Y-%m-%d")
        file_name = 'zeta-api-' + current_date + '.log'
        file_location = self.log_location + file_name
        with open(file_location, 'a+'):
            pass

        logger = logging.getLogger(__name__)
        format = '[%(asctime)s] [%(levelname)s] %(message)s'
        logging.basicConfig(format=format, filemode='a+',
                            filename=file_location, level=logging.DEBUG)
        return logger
