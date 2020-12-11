# InlineObject64

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_redirect_uris** | Option<**Vec<String>**> | Comma-separated list of allowed values for redirect_uri | [optional]
**bound_audiences** | Option<**Vec<String>**> | Comma-separated list of 'aud' claims that are valid for login; any match is sufficient | [optional]
**bound_cidrs** | Option<**Vec<String>**> | Use \"token_bound_cidrs\" instead. If this and \"token_bound_cidrs\" are both specified, only \"token_bound_cidrs\" will be used. | [optional]
**bound_claims** | Option<[**serde_json::Value**](.md)> | Map of claims/values which must match for login | [optional]
**bound_claims_type** | Option<**String**> | How to interpret values in the map of claims/values (which must match for login): allowed values are 'string' or 'glob' | [optional][default to string]
**bound_subject** | Option<**String**> | The 'sub' claim that is valid for login. Optional. | [optional]
**claim_mappings** | Option<[**serde_json::Value**](.md)> | Mappings of claims (key) that will be copied to a metadata field (value) | [optional]
**clock_skew_leeway** | Option<**i32**> | Duration in seconds of leeway when validating all claims to account for clock skew. Defaults to 60 (1 minute) if set to 0 and can be disabled if set to -1. | [optional]
**expiration_leeway** | Option<**i32**> | Duration in seconds of leeway when validating expiration of a token to account for clock skew. Defaults to 150 (2.5 minutes) if set to 0 and can be disabled if set to -1. | [optional][default to 150]
**groups_claim** | Option<**String**> | The claim to use for the Identity group alias names | [optional]
**max_ttl** | Option<**i32**> | Use \"token_max_ttl\" instead. If this and \"token_max_ttl\" are both specified, only \"token_max_ttl\" will be used. | [optional]
**not_before_leeway** | Option<**i32**> | Duration in seconds of leeway when validating not before values of a token to account for clock skew. Defaults to 150 (2.5 minutes) if set to 0 and can be disabled if set to -1. | [optional][default to 150]
**num_uses** | Option<**i32**> | Use \"token_num_uses\" instead. If this and \"token_num_uses\" are both specified, only \"token_num_uses\" will be used. | [optional]
**oidc_scopes** | Option<**Vec<String>**> | Comma-separated list of OIDC scopes | [optional]
**period** | Option<**i32**> | Use \"token_period\" instead. If this and \"token_period\" are both specified, only \"token_period\" will be used. | [optional]
**policies** | Option<**Vec<String>**> | Use \"token_policies\" instead. If this and \"token_policies\" are both specified, only \"token_policies\" will be used. | [optional]
**role_type** | Option<**String**> | Type of the role, either 'jwt' or 'oidc'. | [optional]
**token_bound_cidrs** | Option<**Vec<String>**> | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional]
**token_explicit_max_ttl** | Option<**i32**> | If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed. | [optional]
**token_max_ttl** | Option<**i32**> | The maximum lifetime of the generated token | [optional]
**token_no_default_policy** | Option<**bool**> | If true, the 'default' policy will not automatically be added to generated tokens | [optional]
**token_num_uses** | Option<**i32**> | The maximum number of times a token may be used, a value of zero means unlimited | [optional]
**token_period** | Option<**i32**> | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \"24h\"). | [optional]
**token_policies** | Option<**Vec<String>**> | Comma-separated list of policies | [optional]
**token_ttl** | Option<**i32**> | The initial ttl of the token to generate | [optional]
**token_type** | Option<**String**> | The type of token to generate, service or batch | [optional][default to default-service]
**ttl** | Option<**i32**> | Use \"token_ttl\" instead. If this and \"token_ttl\" are both specified, only \"token_ttl\" will be used. | [optional]
**user_claim** | Option<**String**> | The claim to use for the Identity entity alias name | [optional]
**verbose_oidc_logging** | Option<**bool**> | Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive information may be present in OIDC responses. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


