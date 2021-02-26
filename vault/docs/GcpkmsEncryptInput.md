# GcpkmsEncryptInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_authenticated_data** | Option<**String**> | Optional base64-encoded data that, if specified, must also be provided to decrypt this payload. | [optional]
**key_version** | Option<**i32**> | Integer version of the crypto key version to use for encryption. If unspecified, this defaults to the latest active crypto key version. | [optional]
**plaintext** | Option<**String**> | Plaintext value to be encrypted. This can be a string or binary, but the size is limited. See the Google Cloud KMS documentation for information on size limitations by key types. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


