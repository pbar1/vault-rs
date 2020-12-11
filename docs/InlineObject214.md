# InlineObject214

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | Option<[**serde_json::Value**](.md)> | Configuration for this mount, such as default_lease_ttl and max_lease_ttl. | [optional]
**description** | Option<**String**> | User-friendly description for this mount. | [optional]
**external_entropy_access** | Option<**bool**> | Whether to give the mount access to Vault's external entropy. | [optional][default to false]
**local** | Option<**bool**> | Mark the mount as a local mount, which is not replicated and is unaffected by replication. | [optional][default to false]
**options** | Option<[**serde_json::Value**](.md)> | The options to pass into the backend. Should be a json object with string keys and values. | [optional]
**plugin_name** | Option<**String**> | Name of the plugin to mount based from the name registered in the plugin catalog. | [optional]
**seal_wrap** | Option<**bool**> | Whether to turn on seal wrapping for the mount. | [optional][default to false]
**_type** | Option<**String**> | The type of the backend. Example: \"passthrough\" | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


