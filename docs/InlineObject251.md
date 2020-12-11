# InlineObject251

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | Option<**String**> | Algorithm to use (POST body parameter). Valid values are: * sha2-224 * sha2-256 * sha2-384 * sha2-512 Defaults to \"sha2-256\". | [optional][default to sha2-256]
**input** | Option<**String**> | The base64-encoded input data | [optional]
**key_version** | Option<**i32**> | The version of the key to use for generating the HMAC. Must be 0 (for latest) or a value greater than or equal to the min_encryption_version configured on the key. | [optional]
**urlalgorithm** | Option<**String**> | Algorithm to use (POST URL parameter) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


