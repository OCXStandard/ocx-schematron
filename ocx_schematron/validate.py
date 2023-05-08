#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Validate an XML file with a Schematron schema."""
from lxml import etree
from lxml.etree import XMLSyntaxError
from pathlib import Path


class OcxValidator:
    def __init__(self):
        self.__rule: Path = 'schematron.sch'
        self.__model: Path = ''

    def assign_rule(self, schema: Path) -> bool:
        self.__rule= schema
        return self.__rule.exists()

    def assign_model(self, model: Path) -> bool:
        self.__model = model
        return self.__model.exists()

    def validate(self, model: Path, rule: Path) -> bool:
        """Validate the model."""
        # Parse the XML file to be validated
        if self.assign_model(model):
            try:
                xml_doc  = etree.parse(self.__model)
            except XMLSyntaxError as e:
                print(e)
                return False
        else:
            print(f'(The OCX model {model} does not exist')
            return False
        if self.assign_rule(rule):
            # Parse the Schematron schema
            try:
                schematron_doc = etree.parse(self.__rule)
            except XMLSyntaxError as e:
                print(e)
                return False
        else:
            print(f'(The Schematron schema {rule} does not exist')
            return False
        # Create the Schematron validator
        schematron = etree.Schematron(schematron_doc)
        # Validate the XML file against the Schematron schema
        validation_result = schematron.validate(xml_doc)
        if validation_result:
            # Print the validation result
            print(validation_result)
            return True
        else:
            assert (validation_result)