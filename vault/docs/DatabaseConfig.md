# DatabaseConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_roles** | Option<**Vec<String>**> | Comma separated string or array of the role names allowed to get creds from this database connection. If empty no roles are allowed. If \"*\" all roles are allowed. | [optional]
**password_policy** | Option<**String**> | Password policy to use when generating passwords. | [optional]
**plugin_name** | Option<**String**> | The name of a builtin or previously registered plugin known to vault. This endpoint will create an instance of that plugin type. | [optional]
**root_rotation_statements** | Option<**Vec<String>**> | Specifies the database statements to be executed to rotate the root user's credentials. See the plugin's API page for more information on support and formatting for this parameter. | [optional]
**verify_connection** | Option<**bool**> | If true, the connection details are verified by actually connecting to the database. Defaults to true. | [optional][default to true]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


