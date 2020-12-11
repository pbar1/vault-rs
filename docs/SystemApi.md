# \SystemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sys_audit_path**](SystemApi.md#delete_sys_audit_path) | **delete** /sys/audit/{path} | Disable the audit device at the given path.
[**delete_sys_auth_path**](SystemApi.md#delete_sys_auth_path) | **delete** /sys/auth/{path} | Disable the auth method at the given auth path
[**delete_sys_config_auditing_request_headers_header**](SystemApi.md#delete_sys_config_auditing_request_headers_header) | **delete** /sys/config/auditing/request-headers/{header} | Disable auditing of the given request header.
[**delete_sys_config_cors**](SystemApi.md#delete_sys_config_cors) | **delete** /sys/config/cors | Remove any CORS settings.
[**delete_sys_config_ui_headers_header**](SystemApi.md#delete_sys_config_ui_headers_header) | **delete** /sys/config/ui/headers/{header} | Remove a UI header.
[**delete_sys_generate_root**](SystemApi.md#delete_sys_generate_root) | **delete** /sys/generate-root | Cancels any in-progress root generation attempt.
[**delete_sys_generate_root_attempt**](SystemApi.md#delete_sys_generate_root_attempt) | **delete** /sys/generate-root/attempt | Cancels any in-progress root generation attempt.
[**delete_sys_mounts_path**](SystemApi.md#delete_sys_mounts_path) | **delete** /sys/mounts/{path} | Disable the mount point specified at the given path.
[**delete_sys_plugins_catalog_name**](SystemApi.md#delete_sys_plugins_catalog_name) | **delete** /sys/plugins/catalog/{name} | Remove the plugin with the given name.
[**delete_sys_plugins_catalog_type_name**](SystemApi.md#delete_sys_plugins_catalog_type_name) | **delete** /sys/plugins/catalog/{type}/{name} | Remove the plugin with the given name.
[**delete_sys_policies_acl_name**](SystemApi.md#delete_sys_policies_acl_name) | **delete** /sys/policies/acl/{name} | Delete the ACL policy with the given name.
[**delete_sys_policies_password_name**](SystemApi.md#delete_sys_policies_password_name) | **delete** /sys/policies/password/{name} | Delete a password policy.
[**delete_sys_policy_name**](SystemApi.md#delete_sys_policy_name) | **delete** /sys/policy/{name} | Delete the policy with the given name.
[**delete_sys_quotas_rate_limit_name**](SystemApi.md#delete_sys_quotas_rate_limit_name) | **delete** /sys/quotas/rate-limit/{name} | 
[**delete_sys_raw**](SystemApi.md#delete_sys_raw) | **delete** /sys/raw | Delete the key with given path.
[**delete_sys_raw_path**](SystemApi.md#delete_sys_raw_path) | **delete** /sys/raw/{path} | Delete the key with given path.
[**delete_sys_rekey_backup**](SystemApi.md#delete_sys_rekey_backup) | **delete** /sys/rekey/backup | Delete the backup copy of PGP-encrypted unseal keys.
[**delete_sys_rekey_init**](SystemApi.md#delete_sys_rekey_init) | **delete** /sys/rekey/init | Cancels any in-progress rekey.
[**delete_sys_rekey_recovery_key_backup**](SystemApi.md#delete_sys_rekey_recovery_key_backup) | **delete** /sys/rekey/recovery-key-backup | Allows fetching or deleting the backup of the rotated unseal keys.
[**delete_sys_rekey_verify**](SystemApi.md#delete_sys_rekey_verify) | **delete** /sys/rekey/verify | Cancel any in-progress rekey verification operation.
[**get_sys_audit**](SystemApi.md#get_sys_audit) | **get** /sys/audit | List the enabled audit devices.
[**get_sys_auth**](SystemApi.md#get_sys_auth) | **get** /sys/auth | List the currently enabled credential backends.
[**get_sys_auth_path_tune**](SystemApi.md#get_sys_auth_path_tune) | **get** /sys/auth/{path}/tune | Reads the given auth path's configuration.
[**get_sys_config_auditing_request_headers**](SystemApi.md#get_sys_config_auditing_request_headers) | **get** /sys/config/auditing/request-headers | List the request headers that are configured to be audited.
[**get_sys_config_auditing_request_headers_header**](SystemApi.md#get_sys_config_auditing_request_headers_header) | **get** /sys/config/auditing/request-headers/{header} | List the information for the given request header.
[**get_sys_config_cors**](SystemApi.md#get_sys_config_cors) | **get** /sys/config/cors | Return the current CORS settings.
[**get_sys_config_state_sanitized**](SystemApi.md#get_sys_config_state_sanitized) | **get** /sys/config/state/sanitized | Return a sanitized version of the Vault server configuration.
[**get_sys_config_ui_headers**](SystemApi.md#get_sys_config_ui_headers) | **get** /sys/config/ui/headers/ | Return a list of configured UI headers.
[**get_sys_config_ui_headers_header**](SystemApi.md#get_sys_config_ui_headers_header) | **get** /sys/config/ui/headers/{header} | Return the given UI header's configuration
[**get_sys_generate_root**](SystemApi.md#get_sys_generate_root) | **get** /sys/generate-root | Read the configuration and progress of the current root generation attempt.
[**get_sys_generate_root_attempt**](SystemApi.md#get_sys_generate_root_attempt) | **get** /sys/generate-root/attempt | Read the configuration and progress of the current root generation attempt.
[**get_sys_health**](SystemApi.md#get_sys_health) | **get** /sys/health | Returns the health status of Vault.
[**get_sys_host_info**](SystemApi.md#get_sys_host_info) | **get** /sys/host-info | Information about the host instance that this Vault server is running on.
[**get_sys_init**](SystemApi.md#get_sys_init) | **get** /sys/init | Returns the initialization status of Vault.
[**get_sys_internal_counters_activity**](SystemApi.md#get_sys_internal_counters_activity) | **get** /sys/internal/counters/activity | Report the client count metrics, for this namespace and all child namespaces.
[**get_sys_internal_counters_config**](SystemApi.md#get_sys_internal_counters_config) | **get** /sys/internal/counters/config | Read the client count tracking configuration.
[**get_sys_internal_specs_openapi**](SystemApi.md#get_sys_internal_specs_openapi) | **get** /sys/internal/specs/openapi | Generate an OpenAPI 3 document of all mounted paths.
[**get_sys_internal_ui_mounts**](SystemApi.md#get_sys_internal_ui_mounts) | **get** /sys/internal/ui/mounts | Lists all enabled and visible auth and secrets mounts.
[**get_sys_internal_ui_mounts_path**](SystemApi.md#get_sys_internal_ui_mounts_path) | **get** /sys/internal/ui/mounts/{path} | Return information about the given mount.
[**get_sys_key_status**](SystemApi.md#get_sys_key_status) | **get** /sys/key-status | Provides information about the backend encryption key.
[**get_sys_leader**](SystemApi.md#get_sys_leader) | **get** /sys/leader | Returns the high availability status and current leader instance of Vault.
[**get_sys_leases_lookup**](SystemApi.md#get_sys_leases_lookup) | **get** /sys/leases/lookup/ | Returns a list of lease ids.
[**get_sys_leases_lookup_prefix**](SystemApi.md#get_sys_leases_lookup_prefix) | **get** /sys/leases/lookup/{prefix} | Returns a list of lease ids.
[**get_sys_metrics**](SystemApi.md#get_sys_metrics) | **get** /sys/metrics | Export the metrics aggregated for telemetry purpose.
[**get_sys_monitor**](SystemApi.md#get_sys_monitor) | **get** /sys/monitor | 
[**get_sys_mounts**](SystemApi.md#get_sys_mounts) | **get** /sys/mounts | List the currently mounted backends.
[**get_sys_mounts_path_tune**](SystemApi.md#get_sys_mounts_path_tune) | **get** /sys/mounts/{path}/tune | Tune backend configuration parameters for this mount.
[**get_sys_plugins_catalog**](SystemApi.md#get_sys_plugins_catalog) | **get** /sys/plugins/catalog | Lists all the plugins known to Vault
[**get_sys_plugins_catalog_name**](SystemApi.md#get_sys_plugins_catalog_name) | **get** /sys/plugins/catalog/{name} | Return the configuration data for the plugin with the given name.
[**get_sys_plugins_catalog_type**](SystemApi.md#get_sys_plugins_catalog_type) | **get** /sys/plugins/catalog/{type} | List the plugins in the catalog.
[**get_sys_plugins_catalog_type_name**](SystemApi.md#get_sys_plugins_catalog_type_name) | **get** /sys/plugins/catalog/{type}/{name} | Return the configuration data for the plugin with the given name.
[**get_sys_policies_acl**](SystemApi.md#get_sys_policies_acl) | **get** /sys/policies/acl | List the configured access control policies.
[**get_sys_policies_acl_name**](SystemApi.md#get_sys_policies_acl_name) | **get** /sys/policies/acl/{name} | Retrieve information about the named ACL policy.
[**get_sys_policies_password_name**](SystemApi.md#get_sys_policies_password_name) | **get** /sys/policies/password/{name} | Retrieve an existing password policy.
[**get_sys_policies_password_name_generate**](SystemApi.md#get_sys_policies_password_name_generate) | **get** /sys/policies/password/{name}/generate | Generate a password from an existing password policy.
[**get_sys_policy**](SystemApi.md#get_sys_policy) | **get** /sys/policy | List the configured access control policies.
[**get_sys_policy_name**](SystemApi.md#get_sys_policy_name) | **get** /sys/policy/{name} | Retrieve the policy body for the named policy.
[**get_sys_pprof**](SystemApi.md#get_sys_pprof) | **get** /sys/pprof/ | Returns an HTML page listing the available profiles.
[**get_sys_pprof_cmdline**](SystemApi.md#get_sys_pprof_cmdline) | **get** /sys/pprof/cmdline | Returns the running program's command line.
[**get_sys_pprof_goroutine**](SystemApi.md#get_sys_pprof_goroutine) | **get** /sys/pprof/goroutine | Returns stack traces of all current goroutines.
[**get_sys_pprof_heap**](SystemApi.md#get_sys_pprof_heap) | **get** /sys/pprof/heap | Returns a sampling of memory allocations of live object.
[**get_sys_pprof_profile**](SystemApi.md#get_sys_pprof_profile) | **get** /sys/pprof/profile | Returns a pprof-formatted cpu profile payload.
[**get_sys_pprof_symbol**](SystemApi.md#get_sys_pprof_symbol) | **get** /sys/pprof/symbol | Returns the program counters listed in the request.
[**get_sys_pprof_trace**](SystemApi.md#get_sys_pprof_trace) | **get** /sys/pprof/trace | Returns the execution trace in binary form.
[**get_sys_quotas_config**](SystemApi.md#get_sys_quotas_config) | **get** /sys/quotas/config | 
[**get_sys_quotas_rate_limit**](SystemApi.md#get_sys_quotas_rate_limit) | **get** /sys/quotas/rate-limit | 
[**get_sys_quotas_rate_limit_name**](SystemApi.md#get_sys_quotas_rate_limit_name) | **get** /sys/quotas/rate-limit/{name} | 
[**get_sys_raw**](SystemApi.md#get_sys_raw) | **get** /sys/raw | Read the value of the key at the given path.
[**get_sys_raw_path**](SystemApi.md#get_sys_raw_path) | **get** /sys/raw/{path} | Read the value of the key at the given path.
[**get_sys_rekey_backup**](SystemApi.md#get_sys_rekey_backup) | **get** /sys/rekey/backup | Return the backup copy of PGP-encrypted unseal keys.
[**get_sys_rekey_init**](SystemApi.md#get_sys_rekey_init) | **get** /sys/rekey/init | Reads the configuration and progress of the current rekey attempt.
[**get_sys_rekey_recovery_key_backup**](SystemApi.md#get_sys_rekey_recovery_key_backup) | **get** /sys/rekey/recovery-key-backup | Allows fetching or deleting the backup of the rotated unseal keys.
[**get_sys_rekey_verify**](SystemApi.md#get_sys_rekey_verify) | **get** /sys/rekey/verify | Read the configuration and progress of the current rekey verification attempt.
[**get_sys_replication_status**](SystemApi.md#get_sys_replication_status) | **get** /sys/replication/status | 
[**get_sys_seal_status**](SystemApi.md#get_sys_seal_status) | **get** /sys/seal-status | Check the seal status of a Vault.
[**get_sys_wrapping_lookup**](SystemApi.md#get_sys_wrapping_lookup) | **get** /sys/wrapping/lookup | Look up wrapping properties for the requester's token.
[**post_sys_audit_hash_path**](SystemApi.md#post_sys_audit_hash_path) | **post** /sys/audit-hash/{path} | The hash of the given string via the given audit backend
[**post_sys_audit_path**](SystemApi.md#post_sys_audit_path) | **post** /sys/audit/{path} | Enable a new audit device at the supplied path.
[**post_sys_auth_path**](SystemApi.md#post_sys_auth_path) | **post** /sys/auth/{path} | Enables a new auth method.
[**post_sys_auth_path_tune**](SystemApi.md#post_sys_auth_path_tune) | **post** /sys/auth/{path}/tune | Tune configuration parameters for a given auth path.
[**post_sys_capabilities**](SystemApi.md#post_sys_capabilities) | **post** /sys/capabilities | Fetches the capabilities of the given token on the given path.
[**post_sys_capabilities_accessor**](SystemApi.md#post_sys_capabilities_accessor) | **post** /sys/capabilities-accessor | Fetches the capabilities of the token associated with the given token, on the given path.
[**post_sys_capabilities_self**](SystemApi.md#post_sys_capabilities_self) | **post** /sys/capabilities-self | Fetches the capabilities of the given token on the given path.
[**post_sys_config_auditing_request_headers_header**](SystemApi.md#post_sys_config_auditing_request_headers_header) | **post** /sys/config/auditing/request-headers/{header} | Enable auditing of a header.
[**post_sys_config_cors**](SystemApi.md#post_sys_config_cors) | **post** /sys/config/cors | Configure the CORS settings.
[**post_sys_config_ui_headers_header**](SystemApi.md#post_sys_config_ui_headers_header) | **post** /sys/config/ui/headers/{header} | Configure the values to be returned for the UI header.
[**post_sys_generate_root**](SystemApi.md#post_sys_generate_root) | **post** /sys/generate-root | Initializes a new root generation attempt.
[**post_sys_generate_root_attempt**](SystemApi.md#post_sys_generate_root_attempt) | **post** /sys/generate-root/attempt | Initializes a new root generation attempt.
[**post_sys_generate_root_update**](SystemApi.md#post_sys_generate_root_update) | **post** /sys/generate-root/update | Enter a single master key share to progress the root generation attempt.
[**post_sys_init**](SystemApi.md#post_sys_init) | **post** /sys/init | Initialize a new Vault.
[**post_sys_internal_counters_config**](SystemApi.md#post_sys_internal_counters_config) | **post** /sys/internal/counters/config | Enable or disable collection of client count, set retention period, or set default reporting period.
[**post_sys_leases_lookup**](SystemApi.md#post_sys_leases_lookup) | **post** /sys/leases/lookup | Retrieve lease metadata.
[**post_sys_leases_renew**](SystemApi.md#post_sys_leases_renew) | **post** /sys/leases/renew | Renews a lease, requesting to extend the lease.
[**post_sys_leases_renew_url_lease_id**](SystemApi.md#post_sys_leases_renew_url_lease_id) | **post** /sys/leases/renew/{url_lease_id} | Renews a lease, requesting to extend the lease.
[**post_sys_leases_revoke**](SystemApi.md#post_sys_leases_revoke) | **post** /sys/leases/revoke | Revokes a lease immediately.
[**post_sys_leases_revoke_force_prefix**](SystemApi.md#post_sys_leases_revoke_force_prefix) | **post** /sys/leases/revoke-force/{prefix} | Revokes all secrets or tokens generated under a given prefix immediately
[**post_sys_leases_revoke_prefix_prefix**](SystemApi.md#post_sys_leases_revoke_prefix_prefix) | **post** /sys/leases/revoke-prefix/{prefix} | Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.
[**post_sys_leases_revoke_url_lease_id**](SystemApi.md#post_sys_leases_revoke_url_lease_id) | **post** /sys/leases/revoke/{url_lease_id} | Revokes a lease immediately.
[**post_sys_leases_tidy**](SystemApi.md#post_sys_leases_tidy) | **post** /sys/leases/tidy | This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.
[**post_sys_mounts_path**](SystemApi.md#post_sys_mounts_path) | **post** /sys/mounts/{path} | Enable a new secrets engine at the given path.
[**post_sys_mounts_path_tune**](SystemApi.md#post_sys_mounts_path_tune) | **post** /sys/mounts/{path}/tune | Tune backend configuration parameters for this mount.
[**post_sys_plugins_catalog_name**](SystemApi.md#post_sys_plugins_catalog_name) | **post** /sys/plugins/catalog/{name} | Register a new plugin, or updates an existing one with the supplied name.
[**post_sys_plugins_catalog_type_name**](SystemApi.md#post_sys_plugins_catalog_type_name) | **post** /sys/plugins/catalog/{type}/{name} | Register a new plugin, or updates an existing one with the supplied name.
[**post_sys_plugins_reload_backend**](SystemApi.md#post_sys_plugins_reload_backend) | **post** /sys/plugins/reload/backend | Reload mounted plugin backends.
[**post_sys_policies_acl_name**](SystemApi.md#post_sys_policies_acl_name) | **post** /sys/policies/acl/{name} | Add a new or update an existing ACL policy.
[**post_sys_policies_password_name**](SystemApi.md#post_sys_policies_password_name) | **post** /sys/policies/password/{name} | Add a new or update an existing password policy.
[**post_sys_policy_name**](SystemApi.md#post_sys_policy_name) | **post** /sys/policy/{name} | Add a new or update an existing policy.
[**post_sys_quotas_config**](SystemApi.md#post_sys_quotas_config) | **post** /sys/quotas/config | 
[**post_sys_quotas_rate_limit_name**](SystemApi.md#post_sys_quotas_rate_limit_name) | **post** /sys/quotas/rate-limit/{name} | 
[**post_sys_raw**](SystemApi.md#post_sys_raw) | **post** /sys/raw | Update the value of the key at the given path.
[**post_sys_raw_path**](SystemApi.md#post_sys_raw_path) | **post** /sys/raw/{path} | Update the value of the key at the given path.
[**post_sys_rekey_init**](SystemApi.md#post_sys_rekey_init) | **post** /sys/rekey/init | Initializes a new rekey attempt.
[**post_sys_rekey_update**](SystemApi.md#post_sys_rekey_update) | **post** /sys/rekey/update | Enter a single master key share to progress the rekey of the Vault.
[**post_sys_rekey_verify**](SystemApi.md#post_sys_rekey_verify) | **post** /sys/rekey/verify | Enter a single new key share to progress the rekey verification operation.
[**post_sys_remount**](SystemApi.md#post_sys_remount) | **post** /sys/remount | Move the mount point of an already-mounted backend.
[**post_sys_renew**](SystemApi.md#post_sys_renew) | **post** /sys/renew | Renews a lease, requesting to extend the lease.
[**post_sys_renew_url_lease_id**](SystemApi.md#post_sys_renew_url_lease_id) | **post** /sys/renew/{url_lease_id} | Renews a lease, requesting to extend the lease.
[**post_sys_revoke**](SystemApi.md#post_sys_revoke) | **post** /sys/revoke | Revokes a lease immediately.
[**post_sys_revoke_force_prefix**](SystemApi.md#post_sys_revoke_force_prefix) | **post** /sys/revoke-force/{prefix} | Revokes all secrets or tokens generated under a given prefix immediately
[**post_sys_revoke_prefix_prefix**](SystemApi.md#post_sys_revoke_prefix_prefix) | **post** /sys/revoke-prefix/{prefix} | Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.
[**post_sys_revoke_url_lease_id**](SystemApi.md#post_sys_revoke_url_lease_id) | **post** /sys/revoke/{url_lease_id} | Revokes a lease immediately.
[**post_sys_rotate**](SystemApi.md#post_sys_rotate) | **post** /sys/rotate | Rotates the backend encryption key used to persist data.
[**post_sys_seal**](SystemApi.md#post_sys_seal) | **post** /sys/seal | Seal the Vault.
[**post_sys_step_down**](SystemApi.md#post_sys_step_down) | **post** /sys/step-down | Cause the node to give up active status.
[**post_sys_tools_hash**](SystemApi.md#post_sys_tools_hash) | **post** /sys/tools/hash | Generate a hash sum for input data
[**post_sys_tools_hash_urlalgorithm**](SystemApi.md#post_sys_tools_hash_urlalgorithm) | **post** /sys/tools/hash/{urlalgorithm} | Generate a hash sum for input data
[**post_sys_tools_random**](SystemApi.md#post_sys_tools_random) | **post** /sys/tools/random | Generate random bytes
[**post_sys_tools_random_urlbytes**](SystemApi.md#post_sys_tools_random_urlbytes) | **post** /sys/tools/random/{urlbytes} | Generate random bytes
[**post_sys_unseal**](SystemApi.md#post_sys_unseal) | **post** /sys/unseal | Unseal the Vault.
[**post_sys_wrapping_lookup**](SystemApi.md#post_sys_wrapping_lookup) | **post** /sys/wrapping/lookup | Look up wrapping properties for the given token.
[**post_sys_wrapping_rewrap**](SystemApi.md#post_sys_wrapping_rewrap) | **post** /sys/wrapping/rewrap | Rotates a response-wrapped token.
[**post_sys_wrapping_unwrap**](SystemApi.md#post_sys_wrapping_unwrap) | **post** /sys/wrapping/unwrap | Unwraps a response-wrapped token.
[**post_sys_wrapping_wrap**](SystemApi.md#post_sys_wrapping_wrap) | **post** /sys/wrapping/wrap | Response-wraps an arbitrary JSON object.



## delete_sys_audit_path

> delete_sys_audit_path(path)
Disable the audit device at the given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | The name of the backend. Cannot be delimited. Example: \"mysql\" | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_auth_path

> delete_sys_auth_path(path)
Disable the auth method at the given auth path

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | The path to mount to. Cannot be delimited. Example: \"user\" | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_config_auditing_request_headers_header

> delete_sys_config_auditing_request_headers_header(header)
Disable auditing of the given request header.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**header** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_config_cors

> delete_sys_config_cors()
Remove any CORS settings.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_config_ui_headers_header

> delete_sys_config_ui_headers_header(header)
Remove a UI header.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**header** | **String** | The name of the header. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_generate_root

> delete_sys_generate_root()
Cancels any in-progress root generation attempt.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_generate_root_attempt

> delete_sys_generate_root_attempt()
Cancels any in-progress root generation attempt.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_mounts_path

> delete_sys_mounts_path(path)
Disable the mount point specified at the given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | The path to mount to. Example: \"aws/east\" | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_plugins_catalog_name

> delete_sys_plugins_catalog_name(name)
Remove the plugin with the given name.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the plugin | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_plugins_catalog_type_name

> delete_sys_plugins_catalog_type_name(name, _type)
Remove the plugin with the given name.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the plugin | [required] |
**_type** | **String** | The type of the plugin, may be auth, secret, or database | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_policies_acl_name

> delete_sys_policies_acl_name(name)
Delete the ACL policy with the given name.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the policy. Example: \"ops\" | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_policies_password_name

> delete_sys_policies_password_name(name)
Delete a password policy.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the password policy. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_policy_name

> delete_sys_policy_name(name)
Delete the policy with the given name.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the policy. Example: \"ops\" | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_quotas_rate_limit_name

> delete_sys_quotas_rate_limit_name(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the quota rule. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_raw

> delete_sys_raw()
Delete the key with given path.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_raw_path

> delete_sys_raw_path(path)
Delete the key with given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_rekey_backup

> delete_sys_rekey_backup()
Delete the backup copy of PGP-encrypted unseal keys.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_rekey_init

> delete_sys_rekey_init()
Cancels any in-progress rekey.

This clears the rekey settings as well as any progress made. This must be called to change the parameters of the rekey. Note: verification is still a part of a rekey. If rekeying is canceled during the verification flow, the current unseal keys remain valid.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_rekey_recovery_key_backup

> delete_sys_rekey_recovery_key_backup()
Allows fetching or deleting the backup of the rotated unseal keys.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_sys_rekey_verify

> delete_sys_rekey_verify()
Cancel any in-progress rekey verification operation.

This clears any progress made and resets the nonce. Unlike a `DELETE` against `sys/rekey/init`, this only resets the current verification operation, not the entire rekey atttempt.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_audit

> get_sys_audit()
List the enabled audit devices.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_auth

> get_sys_auth()
List the currently enabled credential backends.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_auth_path_tune

> get_sys_auth_path_tune(path)
Reads the given auth path's configuration.

This endpoint requires sudo capability on the final path, but the same functionality can be achieved without sudo via `sys/mounts/auth/[auth-path]/tune`.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Tune the configuration parameters for an auth path. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_config_auditing_request_headers

> get_sys_config_auditing_request_headers()
List the request headers that are configured to be audited.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_config_auditing_request_headers_header

> get_sys_config_auditing_request_headers_header(header)
List the information for the given request header.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**header** | **String** |  | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_config_cors

> get_sys_config_cors()
Return the current CORS settings.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_config_state_sanitized

> get_sys_config_state_sanitized()
Return a sanitized version of the Vault server configuration.

The sanitized output strips configuration values in the storage, HA storage, and seals stanzas, which may contain sensitive values such as API tokens. It also removes any token or secret fields in other stanzas, such as the circonus_api_token from telemetry.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_config_ui_headers

> get_sys_config_ui_headers(list)
Return a list of configured UI headers.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_config_ui_headers_header

> get_sys_config_ui_headers_header(header)
Return the given UI header's configuration

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**header** | **String** | The name of the header. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_generate_root

> get_sys_generate_root()
Read the configuration and progress of the current root generation attempt.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_generate_root_attempt

> get_sys_generate_root_attempt()
Read the configuration and progress of the current root generation attempt.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_health

> get_sys_health()
Returns the health status of Vault.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_host_info

> get_sys_host_info()
Information about the host instance that this Vault server is running on.

Information about the host instance that this Vault server is running on.   The information that gets collected includes host hardware information, and CPU,   disk, and memory utilization

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_init

> get_sys_init()
Returns the initialization status of Vault.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_internal_counters_activity

> get_sys_internal_counters_activity()
Report the client count metrics, for this namespace and all child namespaces.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_internal_counters_config

> get_sys_internal_counters_config()
Read the client count tracking configuration.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_internal_specs_openapi

> get_sys_internal_specs_openapi()
Generate an OpenAPI 3 document of all mounted paths.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_internal_ui_mounts

> get_sys_internal_ui_mounts()
Lists all enabled and visible auth and secrets mounts.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_internal_ui_mounts_path

> get_sys_internal_ui_mounts_path(path)
Return information about the given mount.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | The path of the mount. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_key_status

> get_sys_key_status()
Provides information about the backend encryption key.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_leader

> get_sys_leader()
Returns the high availability status and current leader instance of Vault.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_leases_lookup

> get_sys_leases_lookup(list)
Returns a list of lease ids.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_leases_lookup_prefix

> get_sys_leases_lookup_prefix(prefix, list)
Returns a list of lease ids.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**prefix** | **String** | The path to list leases under. Example: \"aws/creds/deploy\" | [required] |
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_metrics

> get_sys_metrics(format)
Export the metrics aggregated for telemetry purpose.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**format** | Option<**String**> | Format to export metrics into. Currently accepts only \"prometheus\". |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_monitor

> get_sys_monitor(log_level)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**log_level** | Option<**String**> | Log level to view system logs at. Currently supported values are \"trace\", \"debug\", \"info\", \"warn\", \"error\". |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_mounts

> get_sys_mounts()
List the currently mounted backends.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_mounts_path_tune

> get_sys_mounts_path_tune(path)
Tune backend configuration parameters for this mount.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | The path to mount to. Example: \"aws/east\" | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_plugins_catalog

> get_sys_plugins_catalog()
Lists all the plugins known to Vault

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_plugins_catalog_name

> get_sys_plugins_catalog_name(name)
Return the configuration data for the plugin with the given name.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the plugin | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_plugins_catalog_type

> get_sys_plugins_catalog_type(_type, list)
List the plugins in the catalog.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**_type** | **String** | The type of the plugin, may be auth, secret, or database | [required] |
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_plugins_catalog_type_name

> get_sys_plugins_catalog_type_name(name, _type)
Return the configuration data for the plugin with the given name.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the plugin | [required] |
**_type** | **String** | The type of the plugin, may be auth, secret, or database | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_policies_acl

> get_sys_policies_acl(list)
List the configured access control policies.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_policies_acl_name

> get_sys_policies_acl_name(name)
Retrieve information about the named ACL policy.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the policy. Example: \"ops\" | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_policies_password_name

> get_sys_policies_password_name(name)
Retrieve an existing password policy.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the password policy. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_policies_password_name_generate

> get_sys_policies_password_name_generate(name)
Generate a password from an existing password policy.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the password policy. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_policy

> get_sys_policy(list)
List the configured access control policies.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_policy_name

> get_sys_policy_name(name)
Retrieve the policy body for the named policy.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the policy. Example: \"ops\" | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_pprof

> get_sys_pprof()
Returns an HTML page listing the available profiles.

Returns an HTML page listing the available  profiles. This should be mainly accessed via browsers or applications that can  render pages.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_pprof_cmdline

> get_sys_pprof_cmdline()
Returns the running program's command line.

Returns the running program's command line, with arguments separated by NUL bytes.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_pprof_goroutine

> get_sys_pprof_goroutine()
Returns stack traces of all current goroutines.

Returns stack traces of all current goroutines.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_pprof_heap

> get_sys_pprof_heap()
Returns a sampling of memory allocations of live object.

Returns a sampling of memory allocations of live object.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_pprof_profile

> get_sys_pprof_profile()
Returns a pprof-formatted cpu profile payload.

Returns a pprof-formatted cpu profile payload. Profiling lasts for duration specified in seconds GET parameter, or for 30 seconds if not specified.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_pprof_symbol

> get_sys_pprof_symbol()
Returns the program counters listed in the request.

Returns the program counters listed in the request.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_pprof_trace

> get_sys_pprof_trace()
Returns the execution trace in binary form.

Returns  the execution trace in binary form. Tracing lasts for duration specified in seconds GET parameter, or for 1 second if not specified.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_quotas_config

> get_sys_quotas_config()


### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_quotas_rate_limit

> get_sys_quotas_rate_limit(list)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_quotas_rate_limit_name

> get_sys_quotas_rate_limit_name(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the quota rule. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_raw

> get_sys_raw(list)
Read the value of the key at the given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_raw_path

> get_sys_raw_path(path, list)
Read the value of the key at the given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** |  | [required] |
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_rekey_backup

> get_sys_rekey_backup()
Return the backup copy of PGP-encrypted unseal keys.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_rekey_init

> get_sys_rekey_init()
Reads the configuration and progress of the current rekey attempt.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_rekey_recovery_key_backup

> get_sys_rekey_recovery_key_backup()
Allows fetching or deleting the backup of the rotated unseal keys.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_rekey_verify

> get_sys_rekey_verify()
Read the configuration and progress of the current rekey verification attempt.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_replication_status

> get_sys_replication_status()


### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_seal_status

> get_sys_seal_status()
Check the seal status of a Vault.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_sys_wrapping_lookup

> get_sys_wrapping_lookup()
Look up wrapping properties for the requester's token.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_audit_hash_path

> post_sys_audit_hash_path(path, inline_object193)
The hash of the given string via the given audit backend

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | The name of the backend. Cannot be delimited. Example: \"mysql\" | [required] |
**inline_object193** | Option<[**InlineObject193**](InlineObject193.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_audit_path

> post_sys_audit_path(path, inline_object194)
Enable a new audit device at the supplied path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | The name of the backend. Cannot be delimited. Example: \"mysql\" | [required] |
**inline_object194** | Option<[**InlineObject194**](InlineObject194.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_auth_path

> post_sys_auth_path(path, inline_object195)
Enables a new auth method.

After enabling, the auth method can be accessed and configured via the auth path specified as part of the URL. This auth path will be nested under the auth prefix.  For example, enable the \"foo\" auth method will make it accessible at /auth/foo.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | The path to mount to. Cannot be delimited. Example: \"user\" | [required] |
**inline_object195** | Option<[**InlineObject195**](InlineObject195.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_auth_path_tune

> post_sys_auth_path_tune(path, inline_object196)
Tune configuration parameters for a given auth path.

This endpoint requires sudo capability on the final path, but the same functionality can be achieved without sudo via `sys/mounts/auth/[auth-path]/tune`.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Tune the configuration parameters for an auth path. | [required] |
**inline_object196** | Option<[**InlineObject196**](InlineObject196.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_capabilities

> post_sys_capabilities(inline_object197)
Fetches the capabilities of the given token on the given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object197** | Option<[**InlineObject197**](InlineObject197.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_capabilities_accessor

> post_sys_capabilities_accessor(inline_object198)
Fetches the capabilities of the token associated with the given token, on the given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object198** | Option<[**InlineObject198**](InlineObject198.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_capabilities_self

> post_sys_capabilities_self(inline_object199)
Fetches the capabilities of the given token on the given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object199** | Option<[**InlineObject199**](InlineObject199.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_config_auditing_request_headers_header

> post_sys_config_auditing_request_headers_header(header, inline_object200)
Enable auditing of a header.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**header** | **String** |  | [required] |
**inline_object200** | Option<[**InlineObject200**](InlineObject200.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_config_cors

> post_sys_config_cors(inline_object201)
Configure the CORS settings.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object201** | Option<[**InlineObject201**](InlineObject201.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_config_ui_headers_header

> post_sys_config_ui_headers_header(header, inline_object202)
Configure the values to be returned for the UI header.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**header** | **String** | The name of the header. | [required] |
**inline_object202** | Option<[**InlineObject202**](InlineObject202.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_generate_root

> post_sys_generate_root(inline_object203)
Initializes a new root generation attempt.

Only a single root generation attempt can take place at a time. One (and only one) of otp or pgp_key are required.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object203** | Option<[**InlineObject203**](InlineObject203.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_generate_root_attempt

> post_sys_generate_root_attempt(inline_object204)
Initializes a new root generation attempt.

Only a single root generation attempt can take place at a time. One (and only one) of otp or pgp_key are required.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object204** | Option<[**InlineObject204**](InlineObject204.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_generate_root_update

> post_sys_generate_root_update(inline_object205)
Enter a single master key share to progress the root generation attempt.

If the threshold number of master key shares is reached, Vault will complete the root generation and issue the new token. Otherwise, this API must be called multiple times until that threshold is met. The attempt nonce must be provided with each call.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object205** | Option<[**InlineObject205**](InlineObject205.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_init

> post_sys_init(inline_object206)
Initialize a new Vault.

The Vault must not have been previously initialized. The recovery options, as well as the stored shares option, are only available when using Vault HSM.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object206** | Option<[**InlineObject206**](InlineObject206.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_internal_counters_config

> post_sys_internal_counters_config(inline_object207)
Enable or disable collection of client count, set retention period, or set default reporting period.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object207** | Option<[**InlineObject207**](InlineObject207.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_leases_lookup

> post_sys_leases_lookup(inline_object208)
Retrieve lease metadata.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object208** | Option<[**InlineObject208**](InlineObject208.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_leases_renew

> post_sys_leases_renew(inline_object209)
Renews a lease, requesting to extend the lease.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object209** | Option<[**InlineObject209**](InlineObject209.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_leases_renew_url_lease_id

> post_sys_leases_renew_url_lease_id(url_lease_id, inline_object210)
Renews a lease, requesting to extend the lease.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**url_lease_id** | **String** | The lease identifier to renew. This is included with a lease. | [required] |
**inline_object210** | Option<[**InlineObject210**](InlineObject210.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_leases_revoke

> post_sys_leases_revoke(inline_object211)
Revokes a lease immediately.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object211** | Option<[**InlineObject211**](InlineObject211.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_leases_revoke_force_prefix

> post_sys_leases_revoke_force_prefix(prefix)
Revokes all secrets or tokens generated under a given prefix immediately

Unlike `/sys/leases/revoke-prefix`, this path ignores backend errors encountered during revocation. This is potentially very dangerous and should only be used in specific emergency situations where errors in the backend or the connected backend service prevent normal revocation.  By ignoring these errors, Vault abdicates responsibility for ensuring that the issued credentials or secrets are properly revoked and/or cleaned up. Access to this endpoint should be tightly controlled.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**prefix** | **String** | The path to revoke keys under. Example: \"prod/aws/ops\" | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_leases_revoke_prefix_prefix

> post_sys_leases_revoke_prefix_prefix(prefix, inline_object212)
Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**prefix** | **String** | The path to revoke keys under. Example: \"prod/aws/ops\" | [required] |
**inline_object212** | Option<[**InlineObject212**](InlineObject212.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_leases_revoke_url_lease_id

> post_sys_leases_revoke_url_lease_id(url_lease_id, inline_object213)
Revokes a lease immediately.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**url_lease_id** | **String** | The lease identifier to renew. This is included with a lease. | [required] |
**inline_object213** | Option<[**InlineObject213**](InlineObject213.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_leases_tidy

> post_sys_leases_tidy()
This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_mounts_path

> post_sys_mounts_path(path, inline_object214)
Enable a new secrets engine at the given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | The path to mount to. Example: \"aws/east\" | [required] |
**inline_object214** | Option<[**InlineObject214**](InlineObject214.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_mounts_path_tune

> post_sys_mounts_path_tune(path, inline_object215)
Tune backend configuration parameters for this mount.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | The path to mount to. Example: \"aws/east\" | [required] |
**inline_object215** | Option<[**InlineObject215**](InlineObject215.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_plugins_catalog_name

> post_sys_plugins_catalog_name(name, inline_object216)
Register a new plugin, or updates an existing one with the supplied name.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the plugin | [required] |
**inline_object216** | Option<[**InlineObject216**](InlineObject216.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_plugins_catalog_type_name

> post_sys_plugins_catalog_type_name(name, _type, inline_object217)
Register a new plugin, or updates an existing one with the supplied name.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the plugin | [required] |
**_type** | **String** | The type of the plugin, may be auth, secret, or database | [required] |
**inline_object217** | Option<[**InlineObject217**](InlineObject217.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_plugins_reload_backend

> post_sys_plugins_reload_backend(inline_object218)
Reload mounted plugin backends.

Either the plugin name (`plugin`) or the desired plugin backend mounts (`mounts`) must be provided, but not both. In the case that the plugin name is provided, all mounted paths that use that plugin backend will be reloaded.  If (`scope`) is provided and is (`global`), the plugin(s) are reloaded globally.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object218** | Option<[**InlineObject218**](InlineObject218.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_policies_acl_name

> post_sys_policies_acl_name(name, inline_object219)
Add a new or update an existing ACL policy.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the policy. Example: \"ops\" | [required] |
**inline_object219** | Option<[**InlineObject219**](InlineObject219.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_policies_password_name

> post_sys_policies_password_name(name, inline_object220)
Add a new or update an existing password policy.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the password policy. | [required] |
**inline_object220** | Option<[**InlineObject220**](InlineObject220.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_policy_name

> post_sys_policy_name(name, inline_object221)
Add a new or update an existing policy.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the policy. Example: \"ops\" | [required] |
**inline_object221** | Option<[**InlineObject221**](InlineObject221.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_quotas_config

> post_sys_quotas_config(inline_object222)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object222** | Option<[**InlineObject222**](InlineObject222.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_quotas_rate_limit_name

> post_sys_quotas_rate_limit_name(name, inline_object223)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the quota rule. | [required] |
**inline_object223** | Option<[**InlineObject223**](InlineObject223.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_raw

> post_sys_raw(inline_object224)
Update the value of the key at the given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object224** | Option<[**InlineObject224**](InlineObject224.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_raw_path

> post_sys_raw_path(path, inline_object225)
Update the value of the key at the given path.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** |  | [required] |
**inline_object225** | Option<[**InlineObject225**](InlineObject225.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_rekey_init

> post_sys_rekey_init(inline_object226)
Initializes a new rekey attempt.

Only a single rekey attempt can take place at a time, and changing the parameters of a rekey requires canceling and starting a new rekey, which will also provide a new nonce.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object226** | Option<[**InlineObject226**](InlineObject226.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_rekey_update

> post_sys_rekey_update(inline_object227)
Enter a single master key share to progress the rekey of the Vault.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object227** | Option<[**InlineObject227**](InlineObject227.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_rekey_verify

> post_sys_rekey_verify(inline_object228)
Enter a single new key share to progress the rekey verification operation.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object228** | Option<[**InlineObject228**](InlineObject228.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_remount

> post_sys_remount(inline_object229)
Move the mount point of an already-mounted backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object229** | Option<[**InlineObject229**](InlineObject229.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_renew

> post_sys_renew(inline_object230)
Renews a lease, requesting to extend the lease.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object230** | Option<[**InlineObject230**](InlineObject230.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_renew_url_lease_id

> post_sys_renew_url_lease_id(url_lease_id, inline_object231)
Renews a lease, requesting to extend the lease.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**url_lease_id** | **String** | The lease identifier to renew. This is included with a lease. | [required] |
**inline_object231** | Option<[**InlineObject231**](InlineObject231.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_revoke

> post_sys_revoke(inline_object232)
Revokes a lease immediately.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object232** | Option<[**InlineObject232**](InlineObject232.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_revoke_force_prefix

> post_sys_revoke_force_prefix(prefix)
Revokes all secrets or tokens generated under a given prefix immediately

Unlike `/sys/leases/revoke-prefix`, this path ignores backend errors encountered during revocation. This is potentially very dangerous and should only be used in specific emergency situations where errors in the backend or the connected backend service prevent normal revocation.  By ignoring these errors, Vault abdicates responsibility for ensuring that the issued credentials or secrets are properly revoked and/or cleaned up. Access to this endpoint should be tightly controlled.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**prefix** | **String** | The path to revoke keys under. Example: \"prod/aws/ops\" | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_revoke_prefix_prefix

> post_sys_revoke_prefix_prefix(prefix, inline_object233)
Revokes all secrets (via a lease ID prefix) or tokens (via the tokens' path property) generated under a given prefix immediately.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**prefix** | **String** | The path to revoke keys under. Example: \"prod/aws/ops\" | [required] |
**inline_object233** | Option<[**InlineObject233**](InlineObject233.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_revoke_url_lease_id

> post_sys_revoke_url_lease_id(url_lease_id, inline_object234)
Revokes a lease immediately.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**url_lease_id** | **String** | The lease identifier to renew. This is included with a lease. | [required] |
**inline_object234** | Option<[**InlineObject234**](InlineObject234.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_rotate

> post_sys_rotate()
Rotates the backend encryption key used to persist data.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_seal

> post_sys_seal()
Seal the Vault.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_step_down

> post_sys_step_down()
Cause the node to give up active status.

This endpoint forces the node to give up active status. If the node does not have active status, this endpoint does nothing. Note that the node will sleep for ten seconds before attempting to grab the active lock again, but if no standby nodes grab the active lock in the interim, the same node may become the active node again.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_tools_hash

> post_sys_tools_hash(inline_object235)
Generate a hash sum for input data

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object235** | Option<[**InlineObject235**](InlineObject235.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_tools_hash_urlalgorithm

> post_sys_tools_hash_urlalgorithm(urlalgorithm, inline_object236)
Generate a hash sum for input data

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**urlalgorithm** | **String** | Algorithm to use (POST URL parameter) | [required] |
**inline_object236** | Option<[**InlineObject236**](InlineObject236.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_tools_random

> post_sys_tools_random(inline_object237)
Generate random bytes

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object237** | Option<[**InlineObject237**](InlineObject237.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_tools_random_urlbytes

> post_sys_tools_random_urlbytes(urlbytes, inline_object238)
Generate random bytes

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**urlbytes** | **String** | The number of bytes to generate (POST URL parameter) | [required] |
**inline_object238** | Option<[**InlineObject238**](InlineObject238.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_unseal

> post_sys_unseal(inline_object239)
Unseal the Vault.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object239** | Option<[**InlineObject239**](InlineObject239.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_wrapping_lookup

> post_sys_wrapping_lookup(inline_object240)
Look up wrapping properties for the given token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object240** | Option<[**InlineObject240**](InlineObject240.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_wrapping_rewrap

> post_sys_wrapping_rewrap(inline_object241)
Rotates a response-wrapped token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object241** | Option<[**InlineObject241**](InlineObject241.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_wrapping_unwrap

> post_sys_wrapping_unwrap(inline_object242)
Unwraps a response-wrapped token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object242** | Option<[**InlineObject242**](InlineObject242.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_sys_wrapping_wrap

> post_sys_wrapping_wrap()
Response-wraps an arbitrary JSON object.

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

