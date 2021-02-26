# GcpkmsSignInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | Option<**String**> | Digest to sign. This digest must use the same SHA algorithm as the underlying Cloud KMS key. The digest must be the base64-encoded binary value. This field is required. | [optional]
**key_version** | Option<**i32**> | Integer version of the crypto key version to use for signing. This field is required. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


