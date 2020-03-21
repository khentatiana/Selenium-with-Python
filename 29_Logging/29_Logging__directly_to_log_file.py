import logging

# specify location of the log_file
logging.basicConfig(filename="/Users/tatiana/Desktop/PROJECTS/Selenium_Python_on_Youtube/29_Logging/log_file.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG
                    )

logging.debug("This is DEBUG message")
logging.info("This is INFO message")
logging.warning("This is WARNING message")
logging.error("This is ERROR message")
logging.critical("This is CRITICAL message")