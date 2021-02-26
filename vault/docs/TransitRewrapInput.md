# TransitRewrapInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | Option<**String**> | Ciphertext value to rewrap | [optional]
**context** | Option<**String**> | Base64 encoded context for key derivation. Required for derived keys. | [optional]
**key_version** | Option<**i32**> | The version of the key to use for encryption. Must be 0 (for latest) or a value greater than or equal to the min_encryption_version configured on the key. | [optional]
**nonce** | Option<**String**> | Nonce for when convergent encryption is used | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


