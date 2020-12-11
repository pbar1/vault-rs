# InlineObject130

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_key** | Option<**String**> | Full resource ID of the crypto key including the project, location, key ring, and crypto key like \"projects/%s/locations/%s/keyRings/%s/cryptoKeys/%s\". This crypto key must already exist in Google Cloud KMS unless verify is set to \"false\". | [optional]
**verify** | Option<**bool**> | Verify that the given Google Cloud KMS crypto key exists and is accessible before creating the storage entry in Vault. Set this to \"false\" if the key will not exist at creation time. | [optional][default to true]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


