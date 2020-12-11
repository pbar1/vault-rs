# InlineObject103

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_entity_aliases** | Option<**Vec<String>**> | String or JSON list of allowed entity aliases. If set, specifies the entity aliases which are allowed to be used during token generation. This field supports globbing. | [optional]
**allowed_policies** | Option<**Vec<String>**> | If set, tokens can be created with any subset of the policies in this list, rather than the normal semantics of tokens being a subset of the calling token's policies. The parameter is a comma-delimited string of policy names. | [optional]
**bound_cidrs** | Option<**Vec<String>**> | Use 'token_bound_cidrs' instead. | [optional]
**disallowed_policies** | Option<**Vec<String>**> | If set, successful token creation via this role will require that no policies in the given list are requested. The parameter is a comma-delimited string of policy names. | [optional]
**explicit_max_ttl** | Option<**i32**> | Use 'token_explicit_max_ttl' instead. | [optional]
**orphan** | Option<**bool**> | If true, tokens created via this role will be orphan tokens (have no parent) | [optional]
**path_suffix** | Option<**String**> | If set, tokens created via this role will contain the given suffix as a part of their path. This can be used to assist use of the 'revoke-prefix' endpoint later on. The given suffix must match the regular expression.\\w[\\w-.]+\\w | [optional]
**period** | Option<**i32**> | Use 'token_period' instead. | [optional]
**renewable** | Option<**bool**> | Tokens created via this role will be renewable or not according to this value. Defaults to \"true\". | [optional][default to true]
**token_bound_cidrs** | Option<**Vec<String>**> | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional]
**token_explicit_max_ttl** | Option<**i32**> | If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed. | [optional]
**token_no_default_policy** | Option<**bool**> | If true, the 'default' policy will not automatically be added to generated tokens | [optional]
**token_num_uses** | Option<**i32**> | The maximum number of times a token may be used, a value of zero means unlimited | [optional]
**token_period** | Option<**i32**> | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \"24h\"). | [optional]
**token_type** | Option<**String**> | The type of token to generate, service or batch | [optional][default to default-service]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


