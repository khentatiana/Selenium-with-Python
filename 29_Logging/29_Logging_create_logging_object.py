import logging

# specify location of the log_file
logging.basicConfig(filename="/Users/tatiana/Desktop/PROJECTS/Selenium_Python_on_Youtube/29_Logging/log_file_2.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    )

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logging.debug("This is DEBUG message from TK")
logging.info("This is INFO message from TK")
logging.warning("This is WARNING message from TK")
logging.error("This is ERROR message from TK")
logging.critical("This is CRITICAL message from TK")