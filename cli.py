import typer
import logging
from data_converter.core import convert

app = typer.Typer()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


@app.command()
def run(
    input_path: str = typer.Option(..., help="Path to file or folder"),
    output_path: str = typer.Option(..., help="Output folder"),
    to: str = typer.Option(..., help="Target format (e.g. csv)")
):
    """
    Universal Data Format Converter
    """
    convert(input_path, output_path, to)


if __name__ == "__main__":
    app()
