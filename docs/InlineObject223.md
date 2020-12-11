# InlineObject223

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_interval** | Option<**i32**> | If set, when a client reaches a rate limit threshold, the client will be prohibited from any further requests until after the 'block_interval' has elapsed. | [optional]
**interval** | Option<**i32**> | The duration to enforce rate limiting for (default '1s'). | [optional]
**path** | Option<**String**> | Path of the mount or namespace to apply the quota. A blank path configures a global quota. For example namespace1/ adds a quota to a full namespace, namespace1/auth/userpass adds a quota to userpass in namespace1. | [optional]
**rate** | Option<[**serde_json::Value**](.md)> | The maximum number of requests in a given interval to be allowed by the quota rule. The 'rate' must be positive. | [optional]
**_type** | Option<**String**> | Type of the quota rule. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


