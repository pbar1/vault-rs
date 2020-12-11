# InlineObject206

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pgp_keys** | Option<**Vec<String>**> | Specifies an array of PGP public keys used to encrypt the output unseal keys. Ordering is preserved. The keys must be base64-encoded from their original binary representation. The size of this array must be the same as `secret_shares`. | [optional]
**recovery_pgp_keys** | Option<**Vec<String>**> | Specifies an array of PGP public keys used to encrypt the output recovery keys. Ordering is preserved. The keys must be base64-encoded from their original binary representation. The size of this array must be the same as `recovery_shares`. | [optional]
**recovery_shares** | Option<**i32**> | Specifies the number of shares to split the recovery key into. | [optional]
**recovery_threshold** | Option<**i32**> | Specifies the number of shares required to reconstruct the recovery key. This must be less than or equal to `recovery_shares`. | [optional]
**root_token_pgp_key** | Option<**String**> | Specifies a PGP public key used to encrypt the initial root token. The key must be base64-encoded from its original binary representation. | [optional]
**secret_shares** | Option<**i32**> | Specifies the number of shares to split the master key into. | [optional]
**secret_threshold** | Option<**i32**> | Specifies the number of shares required to reconstruct the master key. This must be less than or equal secret_shares. If using Vault HSM with auto-unsealing, this value must be the same as `secret_shares`. | [optional]
**stored_shares** | Option<**i32**> | Specifies the number of shares that should be encrypted by the HSM and stored for auto-unsealing. Currently must be the same as `secret_shares`. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


