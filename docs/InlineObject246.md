# InlineObject246

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bits** | Option<**i32**> | Number of bits for the key; currently 128, 256, and 512 bits are supported. Defaults to 256. | [optional][default to 256]
**context** | Option<**String**> | Context for key derivation. Required for derived keys. | [optional]
**key_version** | Option<**i32**> | The version of the Vault key to use for encryption of the data key. Must be 0 (for latest) or a value greater than or equal to the min_encryption_version configured on the key. | [optional]
**nonce** | Option<**String**> | Nonce for when convergent encryption v1 is used (only in Vault 0.6.1) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


