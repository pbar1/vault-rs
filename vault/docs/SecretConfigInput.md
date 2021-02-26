# SecretConfigInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cas_required** | Option<**bool**> | If true, the backend will require the cas parameter to be set for each write | [optional]
**delete_version_after** | Option<**i32**> | If set, the length of time before a version is deleted. A negative duration disables the use of delete_version_after on all keys. A zero duration clears the current setting. Accepts a Go duration format string. | [optional]
**max_versions** | Option<**i32**> | The number of versions to keep for each key. Defaults to 10 | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


