import os,sys,logging


LOG_DIR ="logs"
log_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_file_path = os.path.join(LOG_DIR,"running_logs.log")
os.makedirs(LOG_DIR,exist_ok=True)

logging.basicConfig(

    level=logging.INFO,
    format=log_str,
    handlers=[logging.StreamHandler(sys.stdout),
              logging.FileHandler(log_file_path)]
    )

logger = logging.getLogger("textSummarizer")