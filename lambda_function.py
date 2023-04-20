import logging as log
import json
import os
import http.client as client

def lambda_handler(event, context=None):
    start_logging()
    # Log event...
    log.info(json.dumps(event))
    subnet_id = os.getenv("subnet_id")
    log.info(subnet_id)
    response = send_post("Jim Brannon", "james.brannon@siemens.com", subnet_id)
    log.info(response)

def send_post(name, email, subnet_id):
    connection = client.HTTPSConnection('ij92qpvpma.execute-api.eu-west-1.amazonaws.com')

    headers = {
        'X-Siemens-Auth': 'd7e289f4-5f91-45bf-a542-bbcc5ac5c2ea',
        'Content-type': 'application/json'
    }

    payload  = {
        "subnet_id": subnet_id,
        "name": name,
        "email": email
    }
    string_payload = json.dumps(payload)

    connection.request('POST', '/candidate-email_serverless_lambda_stage/data', string_payload, headers)

    response = connection.getresponse()
    return response.read().decode()

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