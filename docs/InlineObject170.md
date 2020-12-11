# InlineObject170

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alt_names** | Option<**String**> | The requested Subject Alternative Names, if any, in a comma-delimited list. May contain both DNS names and email addresses. | [optional]
**common_name** | Option<**String**> | The requested common name; if you want more than one, specify the alternative names in the alt_names map. If not specified when signing, the common name will be taken from the CSR; other names must still be specified in alt_names or ip_sans. | [optional]
**country** | Option<**Vec<String>**> | If set, Country will be set to this value. | [optional]
**csr** | Option<**String**> | PEM-format CSR to be signed. | [optional][default to ]
**exclude_cn_from_sans** | Option<**bool**> | If true, the Common Name will not be included in DNS or Email Subject Alternate Names. Defaults to false (CN is included). | [optional][default to false]
**format** | Option<**String**> | Format for returned data. Can be \"pem\", \"der\", or \"pem_bundle\". If \"pem_bundle\" any private key and issuing cert will be appended to the certificate pem. Defaults to \"pem\". | [optional][default to Format_Pem]
**ip_sans** | Option<**Vec<String>**> | The requested IP SANs, if any, in a comma-delimited list | [optional]
**locality** | Option<**Vec<String>**> | If set, Locality will be set to this value. | [optional]
**max_path_length** | Option<**i32**> | The maximum allowable path length | [optional][default to -1]
**organization** | Option<**Vec<String>**> | If set, O (Organization) will be set to this value. | [optional]
**other_sans** | Option<**Vec<String>**> | Requested other SANs, in an array with the format <oid>;UTF8:<utf8 string value> for each entry. | [optional]
**ou** | Option<**Vec<String>**> | If set, OU (OrganizationalUnit) will be set to this value. | [optional]
**permitted_dns_domains** | Option<**Vec<String>**> | Domains for which this certificate is allowed to sign or issue child certificates. If set, all DNS names (subject and alt) on child certs must be exact matches or subsets of the given domains (see https://tools.ietf.org/html/rfc5280#section-4.2.1.10). | [optional]
**postal_code** | Option<**Vec<String>**> | If set, Postal Code will be set to this value. | [optional]
**private_key_format** | Option<**String**> | Format for the returned private key. Generally the default will be controlled by the \"format\" parameter as either base64-encoded DER or PEM-encoded DER. However, this can be set to \"pkcs8\" to have the returned private key contain base64-encoded pkcs8 or PEM-encoded pkcs8 instead. Defaults to \"der\". | [optional][default to PrivateKeyFormat_Der]
**province** | Option<**Vec<String>**> | If set, Province will be set to this value. | [optional]
**serial_number** | Option<**String**> | The requested serial number, if any. If you want more than one, specify alternative names in the alt_names map using OID 2.5.4.5. | [optional]
**street_address** | Option<**Vec<String>**> | If set, Street Address will be set to this value. | [optional]
**ttl** | Option<**i32**> | The requested Time To Live for the certificate; sets the expiration date. If not specified the role default, backend default, or system default TTL is used, in that order. Cannot be larger than the mount max TTL. Note: this only has an effect when generating a CA cert or signing a CA cert, not when generating a CSR for an intermediate CA. | [optional]
**uri_sans** | Option<**Vec<String>**> | The requested URI SANs, if any, in a comma-delimited list. | [optional]
**use_csr_values** | Option<**bool**> | If true, then: 1) Subject information, including names and alternate names, will be preserved from the CSR rather than using values provided in the other parameters to this path; 2) Any key usages requested in the CSR will be added to the basic set of key usages used for CA certs signed by this path; for instance, the non-repudiation flag. | [optional][default to false]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


