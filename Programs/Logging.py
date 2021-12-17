# To generate Logs

import logging
import os
cwd=os.getcwd()

# This will send logs to file
logging.basicConfig(filename=cwd +"\\"+"ProjectFiles"+"\\"+"Logs"+"\\"+"logfile.txt",
                    format='%(asctime)s:  %(levelname)s:  %(message)s',
                    level=logging.DEBUG)

logger=logging.getLogger()
# logger.setLevel(logging.DEBUG)   - we set level here or in basicConfig function

# Printing logs
logger.debug("Debug Message")
logger.info("Info Message")
logger.warning("Warning Message")
logger.error("Error Message")
logger.critical("Critical Message")
