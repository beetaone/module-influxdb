# InfluxDB

|           |                                                                         |
| --------- | ----------------------------------------------------------------------- |
| Name      | InfluxDB                                                                |
| Version   | v2.0.1                                                                  |
| DockerHub | [beetaone/influxdb](https://hub.docker.com/r/beetaone/influxdb) |
| Authors   | Jakub Grzelak                                                           |

- [InfluxDB](#influxdb)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Example](#example)
    - [Set by the beetaone Agent on the edge-node](#set-by-the-beetaone-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Write data to a selected InfluxDB bucket.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on beetaone platform:

| Name            | Environment Variables | type   | Description                                                                                                                                                                                 |
| --------------- | --------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL             | URL                   | string | URL of your InfluxDB instance.                                                                                                                                                              |
| Organization    | ORGANIZATION          | string | Organization name. Used to uniquely identify the bucket.                                                                                                                                    |
| Bucket          | BUCKET                | string | Bucket name to write data to.                                                                                                                                                               |
| API Token       | API_TOKEN             | string | API token with Write permissions to the selected bucket.                                                                                                                                    |
| Write Precision | WRITE_PRECISION       | string | Sets the precision for the supplied time values (options: S, MS, US, NS).                                                                                                                   |
| Field Keys      | FIELD_KEYS            | string | List of comma (,) separated JSON keys, corresponding to the measurement data values. The same keys will be used as field names in InfluxDB.                                                 |
| Timestamp Key   | TIMESTAMP_KEY         | string | JSON key of the timestamp. If not specified (left empty), then InfluxDB will generate timestamp for data.                                                                                   |
| Tag Keys        | TAG_KEYS              | string | List of comma (,) separated JSON keys, corresponding to the tag values. The same keys will be used as tag names in InfluxDB. Can be left empty if you don't have tags in the incoming data. |
| Measurement Key | MEASUREMENT_NAME      | string | A static name to group the measured data by. If left empty, it will be generated automatically by concatenating the field names, using '_' as separator.                                                   |

### Example

If your incoming data looks like this
```JSON
{
    "location": "warehouse_125",
    "version": "2021.06.05.5874",
    "pressure": 125,
    "temperature": 10,
    "created": 1632208639,
}
```

you might want to set the parameters to
```
FIELD_KEYS=pressure,temperature
TIMESTAMP_KEY=created
TAG_KEYS=location,version
MEASUREMENT_NAME=roomConditions
```


### Set by the beetaone Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by beetaone agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle==0.12.21
influxdb-client==1.35.0
```

## Input

Input to this module is:

-   JSON body single object, example:

```json
{
    "label-1": 12,
    "label-2": "speed"
}
```

-   array of JSON body objects, example:

```json
[
    {
        "label-1": 12,
        "label-2": "speed"
    },
    {
        "label-1": 15,
        "label-2": "volume"
    }
]
```

## Output

Output of this module is input data written to the InfluxDB bucket.