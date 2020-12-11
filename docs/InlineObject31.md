# InlineObject31

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | Option<**String**> | AWS Access Key ID for the account used to make AWS API requests. | [optional][default to ]
**allowed_sts_header_values** | Option<**Vec<String>**> | List of additional headers that are allowed to be in AWS STS request headers | [optional]
**endpoint** | Option<**String**> | URL to override the default generated endpoint for making AWS EC2 API calls. | [optional][default to ]
**iam_endpoint** | Option<**String**> | URL to override the default generated endpoint for making AWS IAM API calls. | [optional][default to ]
**iam_server_id_header_value** | Option<**String**> | Value to require in the X-Vault-AWS-IAM-Server-ID request header | [optional][default to ]
**max_retries** | Option<**i32**> | Maximum number of retries for recoverable exceptions of AWS APIs | [optional][default to -1]
**secret_key** | Option<**String**> | AWS Secret Access Key for the account used to make AWS API requests. | [optional][default to ]
**sts_endpoint** | Option<**String**> | URL to override the default generated endpoint for making AWS STS API calls. | [optional][default to ]
**sts_region** | Option<**String**> | The region ID for the sts_endpoint, if set. | [optional][default to ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


