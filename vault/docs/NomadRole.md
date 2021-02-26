# NomadRole

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global** | Option<**bool**> | Boolean value describing if the token should be global or not. Defaults to false. | [optional]
**policies** | Option<**Vec<String>**> | Comma-separated string or list of policies as previously created in Nomad. Required for 'client' token. | [optional]
**_type** | Option<**String**> | Which type of token to create: 'client' or 'management'. If a 'management' token, the \"policies\" parameter is not required. Defaults to 'client'. | [optional][default to client]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


