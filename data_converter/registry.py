from .formats.rda import RDAHandler
from .formats.csv import CSVHandler


FORMAT_REGISTRY = {
    "rda": RDAHandler(),
    "csv": CSVHandler(),
}
