# SshSignInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_type** | Option<**String**> | Type of certificate to be created; either \"user\" or \"host\". | [optional][default to user]
**critical_options** | Option<[**serde_json::Value**](.md)> | Critical options that the certificate should be signed for. | [optional]
**extensions** | Option<[**serde_json::Value**](.md)> | Extensions that the certificate should be signed for. | [optional]
**key_id** | Option<**String**> | Key id that the created certificate should have. If not specified, the display name of the token will be used. | [optional]
**public_key** | Option<**String**> | SSH public key that should be signed. | [optional]
**ttl** | Option<**i32**> | The requested Time To Live for the SSH certificate; sets the expiration date. If not specified the role default, backend default, or system default TTL is used, in that order. Cannot be later than the role max TTL. | [optional]
**valid_principals** | Option<**String**> | Valid principals, either usernames or hostnames, that the certificate should be signed for. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


