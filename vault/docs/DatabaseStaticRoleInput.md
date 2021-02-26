# DatabaseStaticRoleInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_name** | Option<**String**> | Name of the database this role acts on. | [optional]
**rotation_period** | Option<**i32**> | Period for automatic credential rotation of the given username. Not valid unless used with \"username\". | [optional]
**rotation_statements** | Option<**Vec<String>**> | Specifies the database statements to be executed to rotate the accounts credentials. Not every plugin type will support this functionality. See the plugin's API page for more information on support and formatting for this parameter. | [optional]
**username** | Option<**String**> | Name of the static user account for Vault to manage. Requires \"rotation_period\" to be specified | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


