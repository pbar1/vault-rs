# InlineObject253

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_plaintext_backup** | Option<**bool**> | Enables taking a backup of the named key in plaintext format. Once set, this cannot be disabled. | [optional]
**context** | Option<**String**> | Base64 encoded context for key derivation. When reading a key with key derivation enabled, if the key type supports public keys, this will return the public key for the given context. | [optional]
**convergent_encryption** | Option<**bool**> | Whether to support convergent encryption. This is only supported when using a key with key derivation enabled and will require all requests to carry both a context and 96-bit (12-byte) nonce. The given nonce will be used in place of a randomly generated nonce. As a result, when the same context and nonce are supplied, the same ciphertext is generated. It is *very important* when using this mode that you ensure that all nonces are unique for a given context. Failing to do so will severely impact the ciphertext's security. | [optional]
**derived** | Option<**bool**> | Enables key derivation mode. This allows for per-transaction unique keys for encryption operations. | [optional]
**exportable** | Option<**bool**> | Enables keys to be exportable. This allows for all the valid keys in the key ring to be exported. | [optional]
**_type** | Option<**String**> | The type of key to create. Currently, \"aes128-gcm96\" (symmetric), \"aes256-gcm96\" (symmetric), \"ecdsa-p256\" (asymmetric), \"ecdsa-p384\" (asymmetric), \"ecdsa-p521\" (asymmetric), \"ed25519\" (asymmetric), \"rsa-2048\" (asymmetric), \"rsa-3072\" (asymmetric), \"rsa-4096\" (asymmetric) are supported. Defaults to \"aes256-gcm96\". | [optional][default to aes256-gcm96]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


