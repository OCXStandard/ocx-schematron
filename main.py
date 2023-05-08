#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE

import typer
from pathlib import Path
from ocx_schematron.validate import OcxValidator
def main(name: str):
    print(f"Hello {name}")

def validate(model: Path, rule:Path):
    validator = OcxValidator()
    validator.validate(model, rule)


if __name__ == "__main__":
    typer.run(validate)