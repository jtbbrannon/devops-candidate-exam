import logging as log
import json
import requests
import os

def lambda_handler(event, context=None):
    start_logging()
    # Log event...
    log.info(json.dumps(event))
    subnet_id = os .getenv("subnet_id")
    log.info(subnet_id)

def start_logging(verbose=False):
    if verbose:
        if log.getLogger().hasHandlers():
            log.getLogger().setLevel(log.DEBUG)
        else:
            log.basicConfig(
                format="%(levelname)s: %(message)s", level=log.DEBUG)
            log.info("Verbose output.")
    else:
        if log.getLogger().hasHandlers():
            log.getLogger().setLevel(log.INFO)
        else:
            log.basicConfig(
                format="%(levelname)s: %(message)s", level=log.INFO)