from os import getenv
from logging import getLogger

log = getLogger("params")

PARAMS = {
    "URL": getenv("URL"),
    "ORGANIZATION": getenv("ORGANIZATION"),
    "BUCKET": getenv("BUCKET"),
    "API_TOKEN": getenv("API_TOKEN"),
    "WRITE_PRECISION": getenv("WRITE_PRECISION", "NS"),
    "FIELD_KEYS": getenv("FIELD_KEYS"),
    "TIMESTAMP_KEY": getenv("TIMESTAMP_KEY", ""),
    "TAG_KEYS": getenv("TAG_KEYS", ""),
    "MEASUREMENT_NAME": getenv("MEASUREMENT_NAME", ""),
}

for nonoptionalEnv in ["URL", "ORGANIZATION", "BUCKET", "API_TOKEN", "FIELD_KEYS"]:
    if PARAMS[nonoptionalEnv] is None:
        log.error(f"Non-optional parameter {nonoptionalEnv} not set!")
        exit(1)
