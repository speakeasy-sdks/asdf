# BeaconUserData

A Beacon User's data and resulting analysis when checked against duplicate records and the Beacon Fraud Network.


## Fields

| Field                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                      | Example                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `additional_properties`                                                                                                                                                                                                                          | Dict[str, *Any*]                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                  |
| `address`                                                                                                                                                                                                                                        | [BeaconUserAddress](../../models/shared/beaconuseraddress.md)                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                               | Even if an address has been collected, some fields may be null depending on the region's addressing system. For example:<br/><br/><br/>Addresses from the United Kingdom will not include a region<br/><br/><br/>Addresses from Hong Kong will not include a postal code |                                                                                                                                                                                                                                                  |
| `date_of_birth`                                                                                                                                                                                                                                  | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                               | A date in the format YYYY-MM-DD (RFC 3339 Section 5.6).                                                                                                                                                                                          | 1990-05-29                                                                                                                                                                                                                                       |
| `email_address`                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                               | A valid email address.                                                                                                                                                                                                                           | user@example.com                                                                                                                                                                                                                                 |
| `id_number`                                                                                                                                                                                                                                      | [BeaconUserIDNumber](../../models/shared/beaconuseridnumber.md)                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                               | The ID number associated with a Beacon User.                                                                                                                                                                                                     |                                                                                                                                                                                                                                                  |
| `ip_address`                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                               | An IPv4 or IPV6 address.                                                                                                                                                                                                                         | 192.0.2.42                                                                                                                                                                                                                                       |
| `name`                                                                                                                                                                                                                                           | [BeaconUserName](../../models/shared/beaconusername.md)                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                               | The full name for a given Beacon User.                                                                                                                                                                                                           |                                                                                                                                                                                                                                                  |
| `phone_number`                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                               | A phone number in E.164 format.                                                                                                                                                                                                                  | +19876543212                                                                                                                                                                                                                                     |