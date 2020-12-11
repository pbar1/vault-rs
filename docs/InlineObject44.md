# InlineObject44

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_common_names** | Option<**Vec<String>**> | A comma-separated list of names. At least one must exist in the Common Name. Supports globbing. | [optional]
**allowed_dns_sans** | Option<**Vec<String>**> | A comma-separated list of DNS names. At least one must exist in the SANs. Supports globbing. | [optional]
**allowed_email_sans** | Option<**Vec<String>**> | A comma-separated list of Email Addresses. At least one must exist in the SANs. Supports globbing. | [optional]
**allowed_names** | Option<**Vec<String>**> | A comma-separated list of names. At least one must exist in either the Common Name or SANs. Supports globbing. This parameter is deprecated, please use allowed_common_names, allowed_dns_sans, allowed_email_sans, allowed_uri_sans. | [optional]
**allowed_organizational_units** | Option<**Vec<String>**> | A comma-separated list of Organizational Units names. At least one must exist in the OU field. | [optional]
**allowed_uri_sans** | Option<**Vec<String>**> | A comma-separated list of URIs. At least one must exist in the SANs. Supports globbing. | [optional]
**bound_cidrs** | Option<**Vec<String>**> | Use \"token_bound_cidrs\" instead. If this and \"token_bound_cidrs\" are both specified, only \"token_bound_cidrs\" will be used. | [optional]
**certificate** | Option<**String**> | The public certificate that should be trusted. Must be x509 PEM encoded. | [optional]
**display_name** | Option<**String**> | The display name to use for clients using this certificate. | [optional]
**lease** | Option<**i32**> | Use \"token_ttl\" instead. If this and \"token_ttl\" are both specified, only \"token_ttl\" will be used. | [optional]
**max_ttl** | Option<**i32**> | Use \"token_max_ttl\" instead. If this and \"token_max_ttl\" are both specified, only \"token_max_ttl\" will be used. | [optional]
**period** | Option<**i32**> | Use \"token_period\" instead. If this and \"token_period\" are both specified, only \"token_period\" will be used. | [optional]
**policies** | Option<**Vec<String>**> | Use \"token_policies\" instead. If this and \"token_policies\" are both specified, only \"token_policies\" will be used. | [optional]
**required_extensions** | Option<**Vec<String>**> | A comma-separated string or array of extensions formatted as \"oid:value\". Expects the extension value to be some type of ASN1 encoded string. All values much match. Supports globbing on \"value\". | [optional]
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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


