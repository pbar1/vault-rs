# OpenldapRoleInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_ldif** | **String** | LDIF string used to create new entities within OpenLDAP. This LDIF can be templated. | 
**default_ttl** | Option<**i32**> | Default TTL for dynamic credentials | [optional]
**deletion_ldif** | **String** | LDIF string used to delete entities created within OpenLDAP. This LDIF can be templated. | 
**max_ttl** | Option<**i32**> | Max TTL a dynamic credential can be extended to | [optional]
**rollback_ldif** | Option<**String**> | LDIF string used to rollback changes in the event of a failure to create credentials. This LDIF can be templated. | [optional]
**username_template** | Option<**String**> | The template used to create a username | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


