# InlineObject65

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_iss_validation** | Option<**bool**> | Disable JWT issuer validation. Allows to skip ISS validation. | [optional][default to false]
**disable_local_ca_jwt** | Option<**bool**> | Disable defaulting to the local CA cert and service account JWT when running in a Kubernetes pod | [optional][default to false]
**issuer** | Option<**String**> | Optional JWT issuer. If no issuer is specified, then this plugin will use kubernetes.io/serviceaccount as the default issuer. | [optional]
**kubernetes_ca_cert** | Option<**String**> | PEM encoded CA cert for use by the TLS client used to talk with the API. | [optional]
**kubernetes_host** | Option<**String**> | Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server. | [optional]
**pem_keys** | Option<**Vec<String>**> | Optional list of PEM-formated public keys or certificates used to verify the signatures of kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kuberentes exposes these keys. | [optional]
**token_reviewer_jwt** | Option<**String**> | A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used for login will be used to access the API. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


