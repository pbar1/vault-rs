# InlineObject14

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr_list** | Option<**Vec<String>**> | Comma separated string or list of CIDR blocks enforcing secret IDs to be used from specific set of IP addresses. If 'bound_cidr_list' is set on the role, then the list of CIDR blocks listed here should be a subset of the CIDR blocks listed on the role. | [optional]
**metadata** | Option<**String**> | Metadata to be tied to the SecretID. This should be a JSON formatted string containing metadata in key value pairs. | [optional]
**secret_id** | Option<**String**> | SecretID to be attached to the role. | [optional]
**token_bound_cidrs** | Option<**Vec<String>**> | Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can use the returned token. Should be a subset of the token CIDR blocks listed on the role, if any. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


