# InlineObject8

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_request_headers** | Option<**String**> | The request headers. This must include the headers over which AliCloud has included a signature. | [optional]
**identity_request_url** | Option<**String**> | Base64-encoded full URL against which to make the AliCloud request. | [optional]
**role** | Option<**String**> | Name of the role against which the login is being attempted. If 'role' is not specified, then the login endpoint looks for a role name in the ARN returned by the GetCallerIdentity request. If a matching role is not found, login fails. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


