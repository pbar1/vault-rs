# InlineObject143

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | Option<**bool**> | If set true, tokens tied to this identity will not be able to be used (but will not be revoked). | [optional]
**id** | Option<**String**> | ID of the entity. If set, updates the corresponding existing entity. | [optional]
**metadata** | Option<[**serde_json::Value**](.md)> | Metadata to be associated with the entity. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault <command> <path> metadata=key1=value1 metadata=key2=value2 | [optional]
**policies** | Option<**Vec<String>**> | Policies to be tied to the entity. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


