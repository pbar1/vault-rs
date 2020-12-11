# InlineObject7

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline_policies** | Option<**String**> | JSON of policies to be dynamically applied to users of this role. | [optional]
**max_ttl** | Option<**i32**> | The maximum allowed lifetime of tokens issued using this role. | [optional]
**remote_policies** | Option<**Vec<String>**> | The name and type of each remote policy to be applied. Example: \"name:AliyunRDSReadOnlyAccess,type:System\". | [optional]
**role_arn** | Option<**String**> | ARN of the role to be assumed. If provided, inline_policies and remote_policies should be blank. At creation time, this role must have configured trusted actors, and the access key and secret that will be used to assume the role (in /config) must qualify as a trusted actor. | [optional]
**ttl** | Option<**i32**> | Duration in seconds after which the issued token should expire. Defaults to 0, in which case the value will fallback to the system/mount defaults. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


