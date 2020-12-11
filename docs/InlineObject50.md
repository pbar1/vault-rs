# InlineObject50

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_group_aliases** | Option<**bool**> | If true, will add group aliases to auth tokens generated under this role. This will add the full list of ancestors (projects, folders, organizations) for the given entity's project. Requires IAM permission `resourcemanager.projects.get` on this project. | [optional][default to false]
**allow_gce_inference** | Option<**bool**> | 'iam' roles only. If false, Vault will not not allow GCE instances to login in against this role | [optional][default to true]
**bound_instance_group** | Option<**String**> | Deprecated: use \"bound_instance_groups\" instead. | [optional]
**bound_instance_groups** | Option<**Vec<String>**> | Comma-separated list of permitted instance groups to which the GCE instance must belong. This option only applies to \"gce\" roles. | [optional]
**bound_labels** | Option<**Vec<String>**> | Comma-separated list of GCP labels formatted as\"key:value\" strings that must be present on the GCE instance in order to authenticate. This option only applies to \"gce\" roles. | [optional]
**bound_projects** | Option<**Vec<String>**> | GCP Projects that authenticating entities must belong to. | [optional]
**bound_region** | Option<**String**> | Deprecated: use \"bound_regions\" instead. | [optional]
**bound_regions** | Option<**Vec<String>**> | Comma-separated list of permitted regions to which the GCE instance must belong. If a group is provided, it is assumed to be a regional group. If \"zone\" is provided, this option is ignored. This can be a self-link or region name. This option only applies to \"gce\" roles. | [optional]
**bound_service_accounts** | Option<**Vec<String>**> | Can be set for both 'iam' and 'gce' roles (required for 'iam'). A comma-seperated list of authorized service accounts. If the single value \"*\" is given, this is assumed to be all service accounts under the role's project. If this is set on a GCE role, the inferred service account from the instance metadata token will be used. | [optional]
**bound_zone** | Option<**String**> | Deprecated: use \"bound_zones\" instead. | [optional]
**bound_zones** | Option<**Vec<String>**> | Comma-separated list of permitted zones to which the GCE instance must belong. If a group is provided, it is assumed to be a zonal group. This can be a self-link or zone name. This option only applies to \"gce\" roles. | [optional]
**max_jwt_exp** | Option<**i32**> | Currently enabled for 'iam' only. Duration in seconds from time of validation that a JWT must expire within. | [optional][default to 900]
**max_ttl** | Option<**i32**> | Use \"token_max_ttl\" instead. If this and \"token_max_ttl\" are both specified, only \"token_max_ttl\" will be used. | [optional]
**period** | Option<**i32**> | Use \"token_period\" instead. If this and \"token_period\" are both specified, only \"token_period\" will be used. | [optional]
**policies** | Option<**Vec<String>**> | Use \"token_policies\" instead. If this and \"token_policies\" are both specified, only \"token_policies\" will be used. | [optional]
**project_id** | Option<**String**> | Deprecated: use \"bound_projects\" instead | [optional]
**service_accounts** | Option<**Vec<String>**> | Deprecated: use \"bound_service_accounts\" instead. | [optional]
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
**_type** | Option<**String**> | Type of the role. Currently supported: iam, gce | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


