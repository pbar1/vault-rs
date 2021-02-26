# AdLibrary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_check_in_enforcement** | Option<**bool**> | Disable the default behavior of requiring that check-ins are performed by the entity that checked them out. | [optional][default to false]
**max_ttl** | Option<**i32**> | In seconds, the max amount of time a check-out's renewals should last. Defaults to 24 hours. | [optional][default to 86400]
**service_account_names** | Option<**Vec<String>**> | The username/logon name for the service accounts with which this set will be associated. | [optional]
**ttl** | Option<**i32**> | In seconds, the amount of time a check-out should last. Defaults to 24 hours. | [optional][default to 86400]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


