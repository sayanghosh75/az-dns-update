import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    if "x-forwarded-for" in req.headers:
        source_ip = req.headers["x-forwarded-for"].split(':')[0]
    logging.info('MyIP HTTP trigger function processed a request from: '+source_ip)

    return func.HttpResponse(source_ip, status_code=200)