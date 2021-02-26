# AzureRole

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_object_id** | Option<**String**> | Application Object ID to use for static service principal credentials. | [optional]
**azure_groups** | Option<**String**> | JSON list of Azure groups to add the service principal to. | [optional]
**azure_roles** | Option<**String**> | JSON list of Azure roles to assign. | [optional]
**max_ttl** | Option<**i32**> | Maximum time a service principal. If not set or set to 0, will use system default. | [optional]
**ttl** | Option<**i32**> | Default lease for generated credentials. If not set or set to 0, will use system default. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


