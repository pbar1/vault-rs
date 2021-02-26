# GcpConfigInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | Option<**String**> | GCP IAM service account credentials JSON with permissions to create new service accounts and set IAM policies | [optional]
**max_ttl** | Option<**i32**> | Maximum time a service account key is valid for. If <= 0, will use system default. | [optional]
**ttl** | Option<**i32**> | Default lease for generated keys. If <= 0, will use system default. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


