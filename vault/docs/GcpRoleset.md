# GcpRoleset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bindings** | Option<**String**> | Bindings configuration string. | [optional]
**project** | Option<**String**> | Name of the GCP project that this roleset's service account will belong to. | [optional]
**secret_type** | Option<**String**> | Type of secret generated for this role set. Defaults to 'access_token' | [optional][default to access_token]
**token_scopes** | Option<**Vec<String>**> | List of OAuth scopes to assign to credentials generated under this role set | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


