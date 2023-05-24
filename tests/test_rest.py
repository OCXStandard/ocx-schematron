#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Test the REST api"""
# The swagger UI: http://localhost:8080/swagger-ui/index.html
import requests
from requests.exceptions import HTTPError
import base64
import json
import lxml.etree

tb_validate = 'https://www.itb.ec.europa.eu/xml/rest/order/api/validate'
ep_validate = 'http://localhost:8080/rest/ocx/api/validate'  # Validate a single document
ep_info = 'http://localhost:8080/rest/ocx/api/info'
response = requests.get(ep_info)
fname = 'data/box.3docx'

tree = lxml.etree.parse(fname)
root = tree.getroot()
xmlstr = lxml.etree.tostring(root, encoding='ascii', method='xml')

# Decode the bytes object

ocx_model = xmlstr.decode('ascii')

body = [
    ('contentToValidate', ocx_model),
    ('embeddingMethod', 'string'),
    ('validationType', 'ocx.v2.8.6'),
    ('locationAsPath', True),
    ('addInputToReport', True),
    ('wrapReportDataInCDATA', False)
]

body = [
    ('contentToValidate', "https://www.itb.ec.europa.eu/files/samples/xml/sample-invalid.xml"),
    ('validationType', 'basic'),
]

try:
    response = requests.post(ep_validate, headers={'Accept': 'application/xml'}, data = body)
    # response = requests.get(ep_info, headers={'Accept': 'application/xml'})
    # If the response was successful, no Exception will be raised
    print(response.text)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
else:
    print(json.dumps(response.json(),indent=4))

