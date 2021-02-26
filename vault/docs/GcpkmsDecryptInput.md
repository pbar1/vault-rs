# GcpkmsDecryptInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_authenticated_data** | Option<**String**> | Optional data that was specified during encryption of this payload. | [optional]
**ciphertext** | Option<**String**> | Ciphertext to decrypt as previously returned from an encrypt operation. This must be base64-encoded ciphertext as previously returned from an encrypt operation. | [optional]
**key_version** | Option<**i32**> | Integer version of the crypto key version to use for decryption. This is required for asymmetric keys. For symmetric keys, Cloud KMS will choose the correct version automatically. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


