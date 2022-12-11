"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from .params import PARAMS

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.write.point import Point
from influxdb_client.domain.write_precision import WritePrecision

log = getLogger("module")

__BUCKET__ = PARAMS["BUCKET"]
__ORG__ = PARAMS["ORGANIZATION"]
__API_TOKEN__ = PARAMS["API_TOKEN"]
__URL__ = PARAMS["URL"]

client = influxdb_client.InfluxDBClient(
   url=__URL__,
   token=__API_TOKEN__,
   org=__ORG__
)

write_api = client.write_api(write_options=SYNCHRONOUS)

write_precision_mapping = {
    "MS": WritePrecision.MS,
    "S": WritePrecision.S,
    "US": WritePrecision.US,
    "NS": WritePrecision.NS
}

__WRITE_PRECISION__ = write_precision_mapping[PARAMS["WRITE_PRECISION"]]
__MEASUREMENT_KEY__ = PARAMS["MEASUREMENT_KEY"]
__TIMESTAMP_KEY__ = PARAMS["TIMESTAMP_KEY"]

__TAG_KEYS__ = [tag.strip() for tag in PARAMS["TAG_KEYS"].split(',')] if PARAMS["TAG_KEYS"] else None
__FIELD_KEYS__ = [field.strip() for field in PARAMS["FIELD_KEYS"].split(',')] if PARAMS["FIELD_KEYS"] else None

def write_data(data):
    log.debug(f"Writing data: {data}")
    # create a Point object - representing a single data record, similar to a row in a SQL database table
    p = Point.from_dict(data,
                    write_precision=__WRITE_PRECISION__,
                    record_measurement_key=__MEASUREMENT_KEY__,
                    record_time_key=__TIMESTAMP_KEY__,
                    record_tag_keys=__TAG_KEYS__,
                    record_field_keys=__FIELD_KEYS__
                )

    # send data to InfluxDB
    write_api.write(bucket=__BUCKET__, org=__ORG__, record=p)

def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Outputting ...")

    try:
        if type(received_data) == list:
            for data in received_data:
                write_data(data)
        else:
            write_data(received_data)

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
