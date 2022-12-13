"""
Created on Sun Aug 7 2022

@author: Sayan A Ghosh
"""
# Copyright 2021, 2022. Kyndryl All Rights Reserved.
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# # https://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.
# #


import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    if "x-forwarded-for" in req.headers:
        source_ip = req.headers["x-forwarded-for"].split(':')[0]
    logging.info('MyIP HTTP trigger function processed a request from: '+source_ip)

    return func.HttpResponse(source_ip, status_code=200)