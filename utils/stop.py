import logging
import threading

stop_event = threading.Event()  # Event to handle graceful shutdown

def signal_handler(signum, frame):
    logging.info("Received termination signal. Exiting gracefully...")
    stop_event.set()  # Signal the loop to stop
