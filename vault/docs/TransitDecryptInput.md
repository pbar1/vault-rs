# TransitDecryptInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ciphertext** | Option<**String**> | The ciphertext to decrypt, provided as returned by encrypt. | [optional]
**context** | Option<**String**> | Base64 encoded context for key derivation. Required if key derivation is enabled. | [optional]
**nonce** | Option<**String**> | Base64 encoded nonce value used during encryption. Must be provided if convergent encryption is enabled for this key and the key was generated with Vault 0.6.1. Not required for keys created in 0.6.2+. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


