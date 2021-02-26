# MongodbatlasRole

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr_blocks** | Option<**Vec<String>**> | Whitelist entry in CIDR notation to be added for the API key. Optional for organization and project keys. | [optional]
**ip_addresses** | Option<**Vec<String>**> | IP address to be added to the whitelist for the API key. Optional for organization and project keys. | [optional]
**max_ttl** | Option<**i32**> | The maximum allowed lifetime of credentials issued using this role. | [optional]
**organization_id** | Option<**String**> | Organization ID required for an organization API key | [optional]
**project_id** | Option<**String**> | Project ID the project API key belongs to. | [optional]
**project_roles** | Option<**Vec<String>**> | Roles assigned when an organization API Key is assigned to a project API key | [optional]
**roles** | **Vec<String>** | List of roles that the API Key should be granted. A minimum of one role must be provided. Any roles provided must be valid for the assigned Project, required for organization and project keys. | 
**ttl** | Option<**i32**> | Duration in seconds after which the issued credential should expire. Defaults to 0, in which case the value will fallback to the system/mount defaults. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


