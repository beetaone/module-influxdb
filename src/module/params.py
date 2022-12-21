from os import getenv

PARAMS = {
    "BUCKET": getenv("BUCKET", ""),
    "ORGANIZATION": getenv("ORGANIZATION", ""),
    "API_TOKEN": getenv("API_TOKEN", ""),
    "URL": getenv("URL", "https://us-west-2-1.aws.cloud2.influxdata.com"),
    "WRITE_PRECISION": getenv("WRITE_PRECISION", "S"),
    "MEASUREMENT_KEY": getenv("MEASUREMENT_KEY", ""),
    "TIMESTAMP_KEY": getenv("TIMESTAMP_KEY", ""),
    "TAG_KEYS": getenv("TAG_KEYS", ""),
    "FIELD_KEYS": getenv("FIELD_KEYS", "")
}
