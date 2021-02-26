# TerraformRoleInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_ttl** | Option<**i32**> | Maximum time for role. If not set or set to 0, will use system default. | [optional]
**organization** | Option<**String**> | Name of the Terraform Cloud or Enterprise organization | [optional]
**team_id** | Option<**String**> | ID of the Terraform Cloud or Enterprise team under organization (e.g., settings/teams/team-xxxxxxxxxxxxx) | [optional]
**ttl** | Option<**i32**> | Default lease for generated credentials. If not set or set to 0, will use system default. | [optional]
**user_id** | Option<**String**> | ID of the Terraform Cloud or Enterprise user (e.g., user-xxxxxxxxxxxxxxxx) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


