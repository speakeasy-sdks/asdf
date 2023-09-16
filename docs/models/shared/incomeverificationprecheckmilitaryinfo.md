# IncomeVerificationPrecheckMilitaryInfo

Data about military info in the income verification precheck.


## Fields

| Field                                                                                                                                                                                    | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `branch`                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                       | If the user is currently serving in the US military, the branch of the military in which they are serving<br/>Valid values: 'AIR FORCE', 'ARMY', 'COAST GUARD', 'MARINES', 'NAVY', 'UNKNOWN' |
| `is_active_duty`                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | Is the user currently active duty in the US military                                                                                                                                     |