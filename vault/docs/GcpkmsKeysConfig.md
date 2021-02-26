# GcpkmsKeysConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_version** | Option<**i32**> | Maximum allowed crypto key version. If set to a positive value, key versions greater than the given value are not permitted to be used. If set to 0 or a negative value, there is no maximum key version. | [optional]
**min_version** | Option<**i32**> | Minimum allowed crypto key version. If set to a positive value, key versions less than the given value are not permitted to be used. If set to 0 or a negative value, there is no minimum key version. This value only affects encryption/re-encryption, not decryption. To restrict old values from being decrypted, increase this value and then perform a trim operation. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


