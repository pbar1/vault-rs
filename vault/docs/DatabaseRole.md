# DatabaseRole

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_statements** | Option<**Vec<String>**> | Specifies the database statements executed to create and configure a user. See the plugin's API page for more information on support and formatting for this parameter. | [optional]
**db_name** | Option<**String**> | Name of the database this role acts on. | [optional]
**default_ttl** | Option<**i32**> | Default ttl for role. | [optional]
**max_ttl** | Option<**i32**> | Maximum time a credential is valid for | [optional]
**renew_statements** | Option<**Vec<String>**> | Specifies the database statements to be executed to renew a user. Not every plugin type will support this functionality. See the plugin's API page for more information on support and formatting for this parameter. | [optional]
**revocation_statements** | Option<**Vec<String>**> | Specifies the database statements to be executed to revoke a user. See the plugin's API page for more information on support and formatting for this parameter. | [optional]
**rollback_statements** | Option<**Vec<String>**> | Specifies the database statements to be executed rollback a create operation in the event of an error. Not every plugin type will support this functionality. See the plugin's API page for more information on support and formatting for this parameter. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


