# InlineObject168

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_any_name** | Option<**bool**> | If set, clients can request certificates for any CN they like. See the documentation for more information. | [optional]
**allow_bare_domains** | Option<**bool**> | If set, clients can request certificates for the base domains themselves, e.g. \"example.com\". This is a separate option as in some cases this can be considered a security threat. | [optional]
**allow_glob_domains** | Option<**bool**> | If set, domains specified in \"allowed_domains\" can include glob patterns, e.g. \"ftp*.example.com\". See the documentation for more information. | [optional]
**allow_ip_sans** | Option<**bool**> | If set, IP Subject Alternative Names are allowed. Any valid IP is accepted. | [optional][default to true]
**allow_localhost** | Option<**bool**> | Whether to allow \"localhost\" as a valid common name in a request | [optional][default to true]
**allow_subdomains** | Option<**bool**> | If set, clients can request certificates for subdomains of the CNs allowed by the other role options, including wildcard subdomains. See the documentation for more information. | [optional]
**allowed_domains** | Option<**Vec<String>**> | If set, clients can request certificates for subdomains directly beneath these domains, including the wildcard subdomains. See the documentation for more information. This parameter accepts a comma-separated string or list of domains. | [optional]
**allowed_domains_template** | Option<**bool**> | If set, Allowed domains can be specified using identity template policies. Non-templated domains are also permitted. | [optional][default to false]
**allowed_other_sans** | Option<**Vec<String>**> | If set, an array of allowed other names to put in SANs. These values support globbing and must be in the format <oid>;<type>:<value>. Currently only \"utf8\" is a valid type. All values, including globbing values, must use this syntax, with the exception being a single \"*\" which allows any OID and any value (but type must still be utf8). | [optional]
**allowed_serial_numbers** | Option<**Vec<String>**> | If set, an array of allowed serial numbers to put in Subject. These values support globbing. | [optional]
**allowed_uri_sans** | Option<**Vec<String>**> | If set, an array of allowed URIs to put in the URI Subject Alternative Names. Any valid URI is accepted, these values support globbing. | [optional]
**backend** | Option<**String**> | Backend Type | [optional]
**basic_constraints_valid_for_non_ca** | Option<**bool**> | Mark Basic Constraints valid when issuing non-CA certificates. | [optional]
**client_flag** | Option<**bool**> | If set, certificates are flagged for client auth use. Defaults to true. | [optional][default to true]
**code_signing_flag** | Option<**bool**> | If set, certificates are flagged for code signing use. Defaults to false. | [optional]
**country** | Option<**Vec<String>**> | If set, Country will be set to this value in certificates issued by this role. | [optional]
**email_protection_flag** | Option<**bool**> | If set, certificates are flagged for email protection use. Defaults to false. | [optional]
**enforce_hostnames** | Option<**bool**> | If set, only valid host names are allowed for CN and SANs. Defaults to true. | [optional][default to true]
**ext_key_usage** | Option<**Vec<String>**> | A comma-separated string or list of extended key usages. Valid values can be found at https://golang.org/pkg/crypto/x509/#ExtKeyUsage -- simply drop the \"ExtKeyUsage\" part of the name. To remove all key usages from being set, set this value to an empty list. | [optional][default to []]
**ext_key_usage_oids** | Option<**Vec<String>**> | A comma-separated string or list of extended key usage oids. | [optional]
**generate_lease** | Option<**bool**> | If set, certificates issued/signed against this role will have Vault leases attached to them. Defaults to \"false\". Certificates can be added to the CRL by \"vault revoke <lease_id>\" when certificates are associated with leases. It can also be done using the \"pki/revoke\" endpoint. However, when lease generation is disabled, invoking \"pki/revoke\" would be the only way to add the certificates to the CRL. When large number of certificates are generated with long lifetimes, it is recommended that lease generation be disabled, as large amount of leases adversely affect the startup time of Vault. | [optional]
**key_bits** | Option<**i32**> | The number of bits to use. You will almost certainly want to change this if you adjust the key_type. | [optional][default to 2048]
**key_type** | Option<**String**> | The type of key to use; defaults to RSA. \"rsa\" and \"ec\" are the only valid values. | [optional][default to KeyType_Rsa]
**key_usage** | Option<**Vec<String>**> | A comma-separated string or list of key usages (not extended key usages). Valid values can be found at https://golang.org/pkg/crypto/x509/#KeyUsage -- simply drop the \"KeyUsage\" part of the name. To remove all key usages from being set, set this value to an empty list. | [optional][default to ["DigitalSignature","KeyAgreement","KeyEncipherment"]]
**locality** | Option<**Vec<String>**> | If set, Locality will be set to this value in certificates issued by this role. | [optional]
**max_ttl** | Option<**i32**> | The maximum allowed lease duration | [optional]
**no_store** | Option<**bool**> | If set, certificates issued/signed against this role will not be stored in the storage backend. This can improve performance when issuing large numbers of certificates. However, certificates issued in this way cannot be enumerated or revoked, so this option is recommended only for certificates that are non-sensitive, or extremely short-lived. This option implies a value of \"false\" for \"generate_lease\". | [optional]
**not_before_duration** | Option<**i32**> | The duration before now the cert needs to be created / signed. | [optional][default to 30]
**organization** | Option<**Vec<String>**> | If set, O (Organization) will be set to this value in certificates issued by this role. | [optional]
**ou** | Option<**Vec<String>**> | If set, OU (OrganizationalUnit) will be set to this value in certificates issued by this role. | [optional]
**policy_identifiers** | Option<**Vec<String>**> | A comma-separated string or list of policy oids. | [optional]
**postal_code** | Option<**Vec<String>**> | If set, Postal Code will be set to this value in certificates issued by this role. | [optional]
**province** | Option<**Vec<String>**> | If set, Province will be set to this value in certificates issued by this role. | [optional]
**require_cn** | Option<**bool**> | If set to false, makes the 'common_name' field optional while generating a certificate. | [optional][default to true]
**server_flag** | Option<**bool**> | If set, certificates are flagged for server auth use. Defaults to true. | [optional][default to true]
**street_address** | Option<**Vec<String>**> | If set, Street Address will be set to this value in certificates issued by this role. | [optional]
**ttl** | Option<**i32**> | The lease duration if no specific lease duration is requested. The lease duration controls the expiration of certificates issued by this backend. Defaults to the value of max_ttl. | [optional]
**use_csr_common_name** | Option<**bool**> | If set, when used with a signing profile, the common name in the CSR will be used. This does *not* include any requested Subject Alternative Names. Defaults to true. | [optional][default to true]
**use_csr_sans** | Option<**bool**> | If set, when used with a signing profile, the SANs in the CSR will be used. This does *not* include the Common Name (cn). Defaults to true. | [optional][default to true]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


