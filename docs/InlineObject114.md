# InlineObject114

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | Option<**String**> | Use role_arns or policy_arns instead. | [optional]
**credential_type** | Option<**String**> | Type of credential to retrieve. Must be one of assumed_role, iam_user, or federation_token | [optional]
**default_sts_ttl** | Option<**i32**> | Default TTL for assumed_role and federation_token credential types when no TTL is explicitly requested with the credentials | [optional]
**iam_groups** | Option<**Vec<String>**> | Names of IAM groups that generated IAM users will be added to. For a credential type of assumed_role or federation_token, the policies sent to the corresponding AWS call (sts:AssumeRole or sts:GetFederation) will be the policies from each group in iam_groups combined with the policy_document and policy_arns parameters. | [optional]
**max_sts_ttl** | Option<**i32**> | Max allowed TTL for assumed_role and federation_token credential types | [optional]
**permissions_boundary_arn** | Option<**String**> | ARN of an IAM policy to attach as a permissions boundary on IAM user credentials; only valid when credential_type isiam_user | [optional]
**policy** | Option<**String**> | Use policy_document instead. | [optional]
**policy_arns** | Option<**Vec<String>**> | ARNs of AWS policies. Behavior varies by credential_type. When credential_type is iam_user, then it will attach the specified policies to the generated IAM user. When credential_type is assumed_role or federation_token, the policies will be passed as the PolicyArns parameter, acting as a filter on permissions available. | [optional]
**policy_document** | Option<**String**> | JSON-encoded IAM policy document. Behavior varies by credential_type. When credential_type is iam_user, then it will attach the contents of the policy_document to the IAM user generated. When credential_type is assumed_role or federation_token, this will be passed in as the Policy parameter to the AssumeRole or GetFederationToken API call, acting as a filter on permissions available. | [optional]
**role_arns** | Option<**Vec<String>**> | ARNs of AWS roles allowed to be assumed. Only valid when credential_type is assumed_role | [optional]
**user_path** | Option<**String**> | Path for IAM User. Only valid when credential_type is iam_user | [optional][default to /]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


