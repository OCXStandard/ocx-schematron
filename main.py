#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE

import typer

def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)