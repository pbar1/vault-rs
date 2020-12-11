# InlineObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymous_group_search** | Option<**bool**> | Use anonymous binds when performing LDAP group searches (if true the initial credentials will still be used for the initial connection test). | [optional][default to false]
**binddn** | Option<**String**> | LDAP DN for searching for the user DN (optional) | [optional]
**bindpass** | Option<**String**> | LDAP password for searching for the user DN (optional) | [optional]
**case_sensitive_names** | Option<**bool**> | If true, case sensitivity will be used when comparing usernames and groups for matching policies. | [optional]
**certificate** | Option<**String**> | CA certificate to use when verifying LDAP server certificate, must be x509 PEM encoded (optional) | [optional]
**client_tls_cert** | Option<**String**> | Client certificate to provide to the LDAP server, must be x509 PEM encoded (optional) | [optional]
**client_tls_key** | Option<**String**> | Client certificate key to provide to the LDAP server, must be x509 PEM encoded (optional) | [optional]
**deny_null_bind** | Option<**bool**> | Denies an unauthenticated LDAP bind request if the user's password is empty; defaults to true | [optional][default to true]
**discoverdn** | Option<**bool**> | Use anonymous bind to discover the bind DN of a user (optional) | [optional]
**formatter** | Option<**String**> | Text to insert the password into, ex. \"customPrefix{{PASSWORD}}customSuffix\". | [optional]
**groupattr** | Option<**String**> | LDAP attribute to follow on objects returned by <groupfilter> in order to enumerate user group membership. Examples: \"cn\" or \"memberOf\", etc. Default: cn | [optional][default to cn]
**groupdn** | Option<**String**> | LDAP search base to use for group membership search (eg: ou=Groups,dc=example,dc=org) | [optional]
**groupfilter** | Option<**String**> | Go template for querying group membership of user (optional) The template can access the following context variables: UserDN, Username Example: (&(objectClass=group)(member:1.2.840.113556.1.4.1941:={{.UserDN}})) Default: (|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}})) | [optional][default to (|(memberUid={{.Username}})(member={{.UserDN}})(uniqueMember={{.UserDN}}))]
**insecure_tls** | Option<**bool**> | Skip LDAP server SSL Certificate verification - VERY insecure (optional) | [optional]
**last_rotation_tolerance** | Option<**i32**> | The number of seconds after a Vault rotation where, if Active Directory shows a later rotation, it should be considered out-of-band. | [optional][default to 5]
**length** | Option<**i32**> | The desired length of passwords that Vault generates. | [optional][default to 64]
**max_ttl** | Option<**i32**> | In seconds, the maximum password time-to-live. | [optional]
**password_policy** | Option<**String**> | Name of the password policy to use to generate passwords. | [optional]
**request_timeout** | Option<**i32**> | Timeout, in seconds, for the connection when making requests against the server before returning back an error. | [optional]
**starttls** | Option<**bool**> | Issue a StartTLS command after establishing unencrypted connection (optional) | [optional]
**tls_max_version** | Option<**String**> | Maximum TLS version to use. Accepted values are 'tls10', 'tls11', 'tls12' or 'tls13'. Defaults to 'tls12' | [optional][default to TlsMaxVersion_Tls12]
**tls_min_version** | Option<**String**> | Minimum TLS version to use. Accepted values are 'tls10', 'tls11', 'tls12' or 'tls13'. Defaults to 'tls12' | [optional][default to TlsMinVersion_Tls12]
**ttl** | Option<**i32**> | In seconds, the default password time-to-live. | [optional]
**upndomain** | Option<**String**> | Enables userPrincipalDomain login with [username]@UPNDomain (optional) | [optional]
**url** | Option<**String**> | LDAP URL to connect to (default: ldap://127.0.0.1). Multiple URLs can be specified by concatenating them with commas; they will be tried in-order. | [optional][default to ldap://127.0.0.1]
**use_pre111_group_cn_behavior** | Option<**bool**> | In Vault 1.1.1 a fix for handling group CN values of different cases unfortunately introduced a regression that could cause previously defined groups to not be found due to a change in the resulting name. If set true, the pre-1.1.1 behavior for matching group CNs will be used. This is only needed in some upgrade scenarios for backwards compatibility. It is enabled by default if the config is upgraded but disabled by default on new configurations. | [optional]
**use_token_groups** | Option<**bool**> | If true, use the Active Directory tokenGroups constructed attribute of the user to find the group memberships. This will find all security groups including nested ones. | [optional][default to false]
**userattr** | Option<**String**> | Attribute used for users (default: cn) | [optional][default to cn]
**userdn** | Option<**String**> | LDAP domain to use for users (eg: ou=People,dc=example,dc=org) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


