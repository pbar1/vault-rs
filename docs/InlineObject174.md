# InlineObject174

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_names** | Option<**String**> | The requested Subject Alternative Names, if any, in a comma-delimited list. If email protection is enabled for the role, this may contain email addresses. | [optional]
**common_name** | Option<**String**> | The requested common name; if you want more than one, specify the alternative names in the alt_names map. If email protection is enabled in the role, this may be an email address. | [optional]
**csr** | Option<**String**> | PEM-format CSR to be signed. | [optional][default to ]
**exclude_cn_from_sans** | Option<**bool**> | If true, the Common Name will not be included in DNS or Email Subject Alternate Names. Defaults to false (CN is included). | [optional][default to false]
**format** | Option<**String**> | Format for returned data. Can be \"pem\", \"der\", or \"pem_bundle\". If \"pem_bundle\" any private key and issuing cert will be appended to the certificate pem. Defaults to \"pem\". | [optional][default to Format_Pem]
**ip_sans** | Option<**Vec<String>**> | The requested IP SANs, if any, in a comma-delimited list | [optional]
**other_sans** | Option<**Vec<String>**> | Requested other SANs, in an array with the format <oid>;UTF8:<utf8 string value> for each entry. | [optional]
**private_key_format** | Option<**String**> | Format for the returned private key. Generally the default will be controlled by the \"format\" parameter as either base64-encoded DER or PEM-encoded DER. However, this can be set to \"pkcs8\" to have the returned private key contain base64-encoded pkcs8 or PEM-encoded pkcs8 instead. Defaults to \"der\". | [optional][default to PrivateKeyFormat_Der]
**serial_number** | Option<**String**> | The requested serial number, if any. If you want more than one, specify alternative names in the alt_names map using OID 2.5.4.5. | [optional]
**ttl** | Option<**i32**> | The requested Time To Live for the certificate; sets the expiration date. If not specified the role default, backend default, or system default TTL is used, in that order. Cannot be larger than the role max TTL. | [optional]
**uri_sans** | Option<**Vec<String>**> | The requested URI SANs, if any, in a comma-delimited list. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


