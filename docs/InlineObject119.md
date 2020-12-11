# InlineObject119

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease** | Option<**i32**> | Use ttl instead. | [optional]
**local** | Option<**bool**> | Indicates that the token should not be replicated globally and instead be local to the current datacenter. Available in Consul 1.4 and above. | [optional]
**max_ttl** | Option<**i32**> | Max TTL for the Consul token created from the role. | [optional]
**policies** | Option<**Vec<String>**> | List of policies to attach to the token. Required for Consul 1.4 or above. | [optional]
**policy** | Option<**String**> | Policy document, base64 encoded. Required for 'client' tokens. Required for Consul pre-1.4. | [optional]
**token_type** | Option<**String**> | Which type of token to create: 'client' or 'management'. If a 'management' token, the \"policy\" parameter is not required. Defaults to 'client'. | [optional][default to client]
**ttl** | Option<**i32**> | TTL for the Consul token created from the role. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


