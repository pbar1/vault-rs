# InlineObject175

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**safety_buffer** | Option<**i32**> | The amount of extra time that must have passed beyond certificate expiration before it is removed from the backend storage and/or revocation list. Defaults to 72 hours. | [optional][default to 259200]
**tidy_cert_store** | Option<**bool**> | Set to true to enable tidying up the certificate store | [optional]
**tidy_revocation_list** | Option<**bool**> | Deprecated; synonym for 'tidy_revoked_certs | [optional]
**tidy_revoked_certs** | Option<**bool**> | Set to true to expire all revoked and expired certificates, removing them both from the CRL and from storage. The CRL will be rotated if this causes any values to be removed. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


