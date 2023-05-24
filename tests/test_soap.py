#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Test  SOAP API."""

import zeep
wsdl = 'http://localhost:8080/api/ocx/validation?wsdl'
client = zeep.Client(wsdl=wsdl)
params = {'input' :  [
        {'type':'ocx'},
        {'xml': 'data/box.3docx'},
        {'embeddingMethod': 'URL'},
        {'locationAsPath': 'false'},
        {'addInputToReport': 'true'},
    ]
    }
