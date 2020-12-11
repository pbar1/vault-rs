# InlineObject263

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | Option<**String**> | Deprecated: use \"hash_algorithm\" instead. | [optional][default to sha2-256]
**context** | Option<**String**> | Base64 encoded context for key derivation. Required if key derivation is enabled; currently only available with ed25519 keys. | [optional]
**hash_algorithm** | Option<**String**> | Hash algorithm to use (POST body parameter). Valid values are: * sha1 * sha2-224 * sha2-256 * sha2-384 * sha2-512 Defaults to \"sha2-256\". Not valid for all key types. | [optional][default to sha2-256]
**hmac** | Option<**String**> | The HMAC, including vault header/key version | [optional]
**input** | Option<**String**> | The base64-encoded input data to verify | [optional]
**marshaling_algorithm** | Option<**String**> | The method by which to unmarshal the signature when verifying. The default is 'asn1' which is used by openssl and X.509; can also be set to 'jws' which is used for JWT signatures in which case the signature is also expected to be url-safe base64 encoding instead of standard base64 encoding. Currently only valid for ECDSA P-256 key types\". | [optional][default to asn1]
**prehashed** | Option<**bool**> | Set to 'true' when the input is already hashed. If the key type is 'rsa-2048', 'rsa-3072' or 'rsa-4096', then the algorithm used to hash the input should be indicated by the 'algorithm' parameter. | [optional]
**signature** | Option<**String**> | The signature, including vault header/key version | [optional]
**signature_algorithm** | Option<**String**> | The signature algorithm to use for signature verification. Currently only applies to RSA key types. Options are 'pss' or 'pkcs1v15'. Defaults to 'pss' | [optional]
**urlalgorithm** | Option<**String**> | Hash algorithm to use (POST URL parameter) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


