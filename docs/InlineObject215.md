# InlineObject215

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_response_headers** | Option<**Vec<String>**> | A list of headers to whitelist and allow a plugin to set on responses. | [optional]
**audit_non_hmac_request_keys** | Option<**Vec<String>**> | The list of keys in the request data object that will not be HMAC'ed by audit devices. | [optional]
**audit_non_hmac_response_keys** | Option<**Vec<String>**> | The list of keys in the response data object that will not be HMAC'ed by audit devices. | [optional]
**default_lease_ttl** | Option<**String**> | The default lease TTL for this mount. | [optional]
**description** | Option<**String**> | User-friendly description for this credential backend. | [optional]
**listing_visibility** | Option<**String**> | Determines the visibility of the mount in the UI-specific listing endpoint. Accepted value are 'unauth' and ''. | [optional]
**max_lease_ttl** | Option<**String**> | The max lease TTL for this mount. | [optional]
**options** | Option<[**serde_json::Value**](.md)> | The options to pass into the backend. Should be a json object with string keys and values. | [optional]
**passthrough_request_headers** | Option<**Vec<String>**> | A list of headers to whitelist and pass from the request to the plugin. | [optional]
**token_type** | Option<**String**> | The type of token to issue (service or batch). | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


