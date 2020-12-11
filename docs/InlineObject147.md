# InlineObject147

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_entity_ids** | Option<**Vec<String>**> | Entity IDs to be assigned as group members. | [optional]
**member_group_ids** | Option<**Vec<String>**> | Group IDs to be assigned as group members. | [optional]
**metadata** | Option<[**serde_json::Value**](.md)> | Metadata to be associated with the group. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault <command> <path> metadata=key1=value1 metadata=key2=value2 | [optional]
**name** | Option<**String**> | Name of the group. | [optional]
**policies** | Option<**Vec<String>**> | Policies to be tied to the group. | [optional]
**_type** | Option<**String**> | Type of the group, 'internal' or 'external'. Defaults to 'internal' | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


