import os
import logging
from .registry import FORMAT_REGISTRY


logger = logging.getLogger(__name__)


def convert(input_path: str, output_path: str, target_format: str):

    if target_format not in FORMAT_REGISTRY:
        raise ValueError(f"Unsupported target format: {target_format}")

    os.makedirs(output_path, exist_ok=True)

    if os.path.isfile(input_path):
        files = [input_path]
    elif os.path.isdir(input_path):
        files = [
            os.path.join(input_path, f)
            for f in os.listdir(input_path)
        ]
    else:
        raise ValueError("Invalid input path.")

    for file in files:
        ext = file.split(".")[-1]

        if ext not in FORMAT_REGISTRY:
            logger.warning(f"Skipping unsupported file: {file}")
            continue

        handler = FORMAT_REGISTRY[ext]
        df = handler.read(file)

        output_name = os.path.basename(file).rsplit(".", 1)[0] + f".{target_format}"
        full_output_path = os.path.join(output_path, output_name)

        FORMAT_REGISTRY[target_format].write(df, full_output_path)

        logger.info(f"Converted {file} -> {full_output_path}")
