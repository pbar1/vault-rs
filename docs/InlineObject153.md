# InlineObject153

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | Option<**String**> | Signing algorithm to use. This will default to RS256. | [optional][default to RS256]
**allowed_client_ids** | Option<**Vec<String>**> | Comma separated string or array of role client ids allowed to use this key for signing. If empty no roles are allowed. If \"*\" all roles are allowed. | [optional]
**rotation_period** | Option<**i32**> | How often to generate a new keypair. | [optional]
**verification_ttl** | Option<**i32**> | Controls how long the public portion of a key will be available for verification after being rotated. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


