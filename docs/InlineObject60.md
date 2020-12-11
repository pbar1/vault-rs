# InlineObject60

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound_issuer** | Option<**String**> | The value against which to match the 'iss' claim in a JWT. Optional. | [optional]
**default_role** | Option<**String**> | The default role to use if none is provided during login. If not set, a role is required during login. | [optional]
**jwks_ca_pem** | Option<**String**> | The CA certificate or chain of certificates, in PEM format, to use to validate connections to the JWKS URL. If not set, system certificates are used. | [optional]
**jwks_url** | Option<**String**> | JWKS URL to use to authenticate signatures. Cannot be used with \"oidc_discovery_url\" or \"jwt_validation_pubkeys\". | [optional]
**jwt_supported_algs** | Option<**Vec<String>**> | A list of supported signing algorithms. Defaults to RS256. | [optional]
**jwt_validation_pubkeys** | Option<**Vec<String>**> | A list of PEM-encoded public keys to use to authenticate signatures locally. Cannot be used with \"jwks_url\" or \"oidc_discovery_url\". | [optional]
**namespace_in_state** | Option<**bool**> | Pass namespace in the OIDC state parameter instead of as a separate query parameter. With this setting, the allowed redirect URL(s) in Vault and on the provider side should not contain a namespace query parameter. This means only one redirect URL entry needs to be maintained on the provider side for all vault namespaces that will be authenticating against it. Defaults to true for new configs. | [optional]
**oidc_client_id** | Option<**String**> | The OAuth Client ID configured with your OIDC provider. | [optional]
**oidc_client_secret** | Option<**String**> | The OAuth Client Secret configured with your OIDC provider. | [optional]
**oidc_discovery_ca_pem** | Option<**String**> | The CA certificate or chain of certificates, in PEM format, to use to validate connections to the OIDC Discovery URL. If not set, system certificates are used. | [optional]
**oidc_discovery_url** | Option<**String**> | OIDC Discovery URL, without any .well-known component (base path). Cannot be used with \"jwks_url\" or \"jwt_validation_pubkeys\". | [optional]
**oidc_response_mode** | Option<**String**> | The response mode to be used in the OAuth2 request. Allowed values are 'query' and 'form_post'. | [optional]
**oidc_response_types** | Option<**Vec<String>**> | The response types to request. Allowed values are 'code' and 'id_token'. Defaults to 'code'. | [optional]
**provider_config** | Option<[**serde_json::Value**](.md)> | Provider-specific configuration. Optional. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


