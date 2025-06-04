import time
import logging
from Authtication import BUCTAU

def main():
    """Main function to run the script."""
    authenticator = BUCTAU()
    driver = authenticator.init_driver_edge()
    past_time = time.time()
    while True:
        if time.time() - past_time > 10.0:
            if authenticator.detect_net():
                past_time = time.time()
                continue
            else:
                authenticator.login(driver)
                past_time = time.time()
                continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Script interrupted by user. Exiting...")
    except Exception as e:
        logging.error(f"An error occurred: {e}")