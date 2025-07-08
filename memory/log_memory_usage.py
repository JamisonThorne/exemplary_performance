import psutil
from datetime import datetime
import logging

def log_memory_usage(message, logger=None):
    """
    Log memory usage with a custom message.

    Args:
        message (str): Custom message to log.
        logger (logging.Logger, optional): Logger to use. If None, prints to stdout.
    """
    try:
        process = psutil.Process()
        memory_info = process.memory_info()
        memory_mb = memory_info.rss / (1024 * 1024)  # Convert to MB
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"{timestamp} | {message} - Memory usage: {memory_mb:.2f} MB"
        if logger:
            logger.info(log_msg)
        else:
            print(log_msg)
    except Exception as e:
        error_msg = f"Failed to log memory usage: {e}"
        if logger:
            logger.error(error_msg)
        else:
            print(error_msg)