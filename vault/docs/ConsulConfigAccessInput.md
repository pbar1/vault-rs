# ConsulConfigAccessInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | Option<**String**> | Consul server address | [optional]
**ca_cert** | Option<**String**> | CA certificate to use when verifying Consul server certificate, must be x509 PEM encoded. | [optional]
**client_cert** | Option<**String**> | Client certificate used for Consul's TLS communication, must be x509 PEM encoded and if this is set you need to also set client_key. | [optional]
**client_key** | Option<**String**> | Client key used for Consul's TLS communication, must be x509 PEM encoded and if this is set you need to also set client_cert. | [optional]
**scheme** | Option<**String**> | URI scheme for the Consul address | [optional][default to http]
**token** | Option<**String**> | Token for API calls | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


