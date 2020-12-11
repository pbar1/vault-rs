# InlineObject217

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | Option<**Vec<String>**> | The args passed to plugin command. | [optional]
**command** | Option<**String**> | The command used to start the plugin. The executable defined in this command must exist in vault's plugin directory. | [optional]
**env** | Option<**Vec<String>**> | The environment variables passed to plugin command. Each entry is of the form \"key=value\". | [optional]
**sha256** | Option<**String**> | The SHA256 sum of the executable used in the command field. This should be HEX encoded. | [optional]
**sha_256** | Option<**String**> | The SHA256 sum of the executable used in the command field. This should be HEX encoded. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


