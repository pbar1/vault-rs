# InlineObject30

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_public_cert** | Option<**String**> | Base64 encoded AWS Public cert required to verify PKCS7 signature of the EC2 instance metadata. | [optional]
**_type** | Option<**String**> | Takes the value of either \"pkcs7\" or \"identity\", indicating the type of document which can be verified using the given certificate. The reason is that the PKCS#7 document will have a DSA digest and the identity signature will have an RSA signature, and accordingly the public certificates to verify those also vary. Defaults to \"pkcs7\". | [optional][default to pkcs7]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


