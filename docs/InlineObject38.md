# InlineObject38

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_instance_migration** | Option<**bool**> | If set, allows migration of the underlying instance where the client resides. This keys off of pendingTime in the metadata document, so essentially, this disables the client nonce check whenever the instance is migrated to a new host and pendingTime is newer than the previously-remembered time. Use with caution. | [optional][default to false]
**disallow_reauthentication** | Option<**bool**> | If set, only allows a single token to be granted per instance ID. In order to perform a fresh login, the entry in whitelist for the instance ID needs to be cleared using the 'auth/aws-ec2/identity-whitelist/<instance_id>' endpoint. | [optional][default to false]
**instance_id** | Option<**String**> | Instance ID for which this tag is intended for. If set, the created tag can only be used by the instance with the given ID. | [optional]
**max_ttl** | Option<**i32**> | If set, specifies the maximum allowed token lifetime. | [optional][default to 0]
**policies** | Option<**Vec<String>**> | Policies to be associated with the tag. If set, must be a subset of the role's policies. If set, but set to an empty value, only the 'default' policy will be given to issued tokens. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


