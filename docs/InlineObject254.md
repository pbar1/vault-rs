# InlineObject254

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_plaintext_backup** | Option<**bool**> | Enables taking a backup of the named key in plaintext format. Once set, this cannot be disabled. | [optional]
**deletion_allowed** | Option<**bool**> | Whether to allow deletion of the key | [optional]
**exportable** | Option<**bool**> | Enables export of the key. Once set, this cannot be disabled. | [optional]
**min_decryption_version** | Option<**i32**> | If set, the minimum version of the key allowed to be decrypted. For signing keys, the minimum version allowed to be used for verification. | [optional]
**min_encryption_version** | Option<**i32**> | If set, the minimum version of the key allowed to be used for encryption; or for signing keys, to be used for signing. If set to zero, only the latest version of the key is allowed. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


