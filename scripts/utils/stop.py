import logging
import threading

event = threading.Event()  # Event to handle graceful shutdown

def signal_handler(signum, frame):
    logging.info("Received termination signal. Exiting gracefully...")
    event.set()  # Signal the loop to stop
