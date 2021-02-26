# \SecretsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ad_config**](SecretsApi.md#delete_ad_config) | **delete** /ad/config | Configure the AD server to connect to, along with password options.
[**delete_ad_library**](SecretsApi.md#delete_ad_library) | **delete** /ad/library/{name} | Delete a library set.
[**delete_ad_role**](SecretsApi.md#delete_ad_role) | **delete** /ad/roles/{name} | Manage roles to build links between Vault and Active Directory service accounts.
[**delete_alicloud_config**](SecretsApi.md#delete_alicloud_config) | **delete** /alicloud/config | Configure the access key and secret to use for RAM and STS calls.
[**delete_alicloud_role**](SecretsApi.md#delete_alicloud_role) | **delete** /alicloud/role/{name} | Read, write and reference policies and roles that API keys or STS credentials can be made for.
[**delete_aws_role**](SecretsApi.md#delete_aws_role) | **delete** /aws/roles/{name} | Read, write and reference IAM policies that access keys can be made for.
[**delete_azure_config**](SecretsApi.md#delete_azure_config) | **delete** /azure/config | Configure the Azure Secret backend.
[**delete_azure_role**](SecretsApi.md#delete_azure_role) | **delete** /azure/roles/{name} | Manage the Vault roles used to generate Azure credentials.
[**delete_consul_role**](SecretsApi.md#delete_consul_role) | **delete** /consul/roles/{name} | 
[**delete_cubbyhole_secret**](SecretsApi.md#delete_cubbyhole_secret) | **delete** /cubbyhole/{path} | Deletes the secret at the specified location.
[**delete_database_config**](SecretsApi.md#delete_database_config) | **delete** /database/config/{name} | Configure connection details to a database plugin.
[**delete_database_role**](SecretsApi.md#delete_database_role) | **delete** /database/roles/{name} | Manage the roles that can be created with this backend.
[**delete_database_static_role**](SecretsApi.md#delete_database_static_role) | **delete** /database/static-roles/{name} | Manage the static roles that can be created with this backend.
[**delete_gcp_roleset**](SecretsApi.md#delete_gcp_roleset) | **delete** /gcp/roleset/{name} | 
[**delete_gcpkms_config**](SecretsApi.md#delete_gcpkms_config) | **delete** /gcpkms/config | Configure the GCP KMS secrets engine
[**delete_gcpkms_key**](SecretsApi.md#delete_gcpkms_key) | **delete** /gcpkms/keys/{key} | Interact with crypto keys in Vault and Google Cloud KMS
[**delete_gcpkms_keys_deregister**](SecretsApi.md#delete_gcpkms_keys_deregister) | **delete** /gcpkms/keys/deregister/{key} | Deregister an existing key in Vault
[**delete_gcpkms_keys_trim**](SecretsApi.md#delete_gcpkms_keys_trim) | **delete** /gcpkms/keys/trim/{key} | Delete old crypto key versions from Google Cloud KMS
[**delete_mongodbatlas_role**](SecretsApi.md#delete_mongodbatlas_role) | **delete** /mongodbatlas/roles/{name} | Manage the roles used to generate MongoDB Atlas Programmatic API Keys.
[**delete_nomad_config_access**](SecretsApi.md#delete_nomad_config_access) | **delete** /nomad/config/access | 
[**delete_nomad_config_lease**](SecretsApi.md#delete_nomad_config_lease) | **delete** /nomad/config/lease | Configure the lease parameters for generated tokens
[**delete_nomad_role**](SecretsApi.md#delete_nomad_role) | **delete** /nomad/role/{name} | 
[**delete_openldap_config**](SecretsApi.md#delete_openldap_config) | **delete** /openldap/config | 
[**delete_openldap_role**](SecretsApi.md#delete_openldap_role) | **delete** /openldap/role/{name} | 
[**delete_openldap_static_role**](SecretsApi.md#delete_openldap_static_role) | **delete** /openldap/static-role/{name} | 
[**delete_rabbitmq_role**](SecretsApi.md#delete_rabbitmq_role) | **delete** /rabbitmq/roles/{name} | Manage the roles that can be created with this backend.
[**delete_secret_data**](SecretsApi.md#delete_secret_data) | **delete** /secret/data/{path} | Write, Read, and Delete data in the Key-Value Store.
[**delete_secret_metadata**](SecretsApi.md#delete_secret_metadata) | **delete** /secret/metadata/{path} | Configures settings for the KV store
[**delete_ssh_config_ca**](SecretsApi.md#delete_ssh_config_ca) | **delete** /ssh/config/ca | Set the SSH private key used for signing certificates.
[**delete_ssh_config_zeroaddress**](SecretsApi.md#delete_ssh_config_zeroaddress) | **delete** /ssh/config/zeroaddress | Assign zero address as default CIDR block for select roles.
[**delete_ssh_keys**](SecretsApi.md#delete_ssh_keys) | **delete** /ssh/keys/{key_name} | Register a shared private key with Vault.
[**delete_ssh_role**](SecretsApi.md#delete_ssh_role) | **delete** /ssh/roles/{role} | Manage the 'roles' that can be created with this backend.
[**delete_terraform_config**](SecretsApi.md#delete_terraform_config) | **delete** /terraform/config | 
[**delete_terraform_role**](SecretsApi.md#delete_terraform_role) | **delete** /terraform/role/{name} | 
[**delete_totp_key**](SecretsApi.md#delete_totp_key) | **delete** /totp/keys/{name} | Manage the keys that can be created with this backend.
[**delete_transit_key**](SecretsApi.md#delete_transit_key) | **delete** /transit/keys/{name} | Managed named encryption keys
[**get_ad_config**](SecretsApi.md#get_ad_config) | **get** /ad/config | Configure the AD server to connect to, along with password options.
[**get_ad_creds**](SecretsApi.md#get_ad_creds) | **get** /ad/creds/{name} | Retrieve a role's creds by role name.
[**get_ad_libraries**](SecretsApi.md#get_ad_libraries) | **get** /ad/library | 
[**get_ad_library**](SecretsApi.md#get_ad_library) | **get** /ad/library/{name} | Read a library set.
[**get_ad_library_status**](SecretsApi.md#get_ad_library_status) | **get** /ad/library/{name}/status | Check the status of the service accounts in a library set.
[**get_ad_role**](SecretsApi.md#get_ad_role) | **get** /ad/roles/{name} | Manage roles to build links between Vault and Active Directory service accounts.
[**get_ad_roles**](SecretsApi.md#get_ad_roles) | **get** /ad/roles | List the name of each role currently stored.
[**get_ad_rotate_root**](SecretsApi.md#get_ad_rotate_root) | **get** /ad/rotate-root | 
[**get_alicloud_config**](SecretsApi.md#get_alicloud_config) | **get** /alicloud/config | Configure the access key and secret to use for RAM and STS calls.
[**get_alicloud_creds**](SecretsApi.md#get_alicloud_creds) | **get** /alicloud/creds/{name} | Generate an API key or STS credential using the given role's configuration.'
[**get_alicloud_role**](SecretsApi.md#get_alicloud_role) | **get** /alicloud/role/{name} | Read, write and reference policies and roles that API keys or STS credentials can be made for.
[**get_alicloud_roles**](SecretsApi.md#get_alicloud_roles) | **get** /alicloud/role | List the existing roles in this backend.
[**get_aws_config_lease**](SecretsApi.md#get_aws_config_lease) | **get** /aws/config/lease | Configure the default lease information for generated credentials.
[**get_aws_config_root**](SecretsApi.md#get_aws_config_root) | **get** /aws/config/root | Configure the root credentials that are used to manage IAM.
[**get_aws_creds**](SecretsApi.md#get_aws_creds) | **get** /aws/creds | Generate AWS credentials from a specific Vault role.
[**get_aws_role**](SecretsApi.md#get_aws_role) | **get** /aws/roles/{name} | Read, write and reference IAM policies that access keys can be made for.
[**get_aws_roles**](SecretsApi.md#get_aws_roles) | **get** /aws/roles | List the existing roles in this backend
[**get_aws_sts**](SecretsApi.md#get_aws_sts) | **get** /aws/sts/{name} | Generate AWS credentials from a specific Vault role.
[**get_azure_config**](SecretsApi.md#get_azure_config) | **get** /azure/config | Configure the Azure Secret backend.
[**get_azure_creds**](SecretsApi.md#get_azure_creds) | **get** /azure/creds/{role} | Request Service Principal credentials for a given Vault role.
[**get_azure_role**](SecretsApi.md#get_azure_role) | **get** /azure/roles/{name} | Manage the Vault roles used to generate Azure credentials.
[**get_azure_roles**](SecretsApi.md#get_azure_roles) | **get** /azure/roles | List existing roles.
[**get_consul_config_access**](SecretsApi.md#get_consul_config_access) | **get** /consul/config/access | 
[**get_consul_creds**](SecretsApi.md#get_consul_creds) | **get** /consul/creds/{role} | 
[**get_consul_role**](SecretsApi.md#get_consul_role) | **get** /consul/roles/{name} | 
[**get_consul_roles**](SecretsApi.md#get_consul_roles) | **get** /consul/roles | 
[**get_cubbyhole_secret**](SecretsApi.md#get_cubbyhole_secret) | **get** /cubbyhole/{path} | Retrieve the secret at the specified location.
[**get_database_config**](SecretsApi.md#get_database_config) | **get** /database/config/{name} | Configure connection details to a database plugin.
[**get_database_configs**](SecretsApi.md#get_database_configs) | **get** /database/config | Configure connection details to a database plugin.
[**get_database_creds**](SecretsApi.md#get_database_creds) | **get** /database/creds/{name} | Request database credentials for a certain role.
[**get_database_role**](SecretsApi.md#get_database_role) | **get** /database/roles/{name} | Manage the roles that can be created with this backend.
[**get_database_roles**](SecretsApi.md#get_database_roles) | **get** /database/roles | Manage the roles that can be created with this backend.
[**get_database_static_creds**](SecretsApi.md#get_database_static_creds) | **get** /database/static-creds/{name} | Request database credentials for a certain static role. These credentials are rotated periodically.
[**get_database_static_role**](SecretsApi.md#get_database_static_role) | **get** /database/static-roles/{name} | Manage the static roles that can be created with this backend.
[**get_database_static_roles**](SecretsApi.md#get_database_static_roles) | **get** /database/static-roles | Manage the static roles that can be created with this backend.
[**get_gcp_config**](SecretsApi.md#get_gcp_config) | **get** /gcp/config | 
[**get_gcp_key**](SecretsApi.md#get_gcp_key) | **get** /gcp/key/{roleset} | 
[**get_gcp_roleset**](SecretsApi.md#get_gcp_roleset) | **get** /gcp/roleset/{name} | 
[**get_gcp_rolesets**](SecretsApi.md#get_gcp_rolesets) | **get** /gcp/rolesets | 
[**get_gcp_token**](SecretsApi.md#get_gcp_token) | **get** /gcp/token/{roleset} | 
[**get_gcpkms_config**](SecretsApi.md#get_gcpkms_config) | **get** /gcpkms/config | Configure the GCP KMS secrets engine
[**get_gcpkms_key**](SecretsApi.md#get_gcpkms_key) | **get** /gcpkms/keys/{key} | Interact with crypto keys in Vault and Google Cloud KMS
[**get_gcpkms_keys**](SecretsApi.md#get_gcpkms_keys) | **get** /gcpkms/keys | List named keys
[**get_gcpkms_keys_config**](SecretsApi.md#get_gcpkms_keys_config) | **get** /gcpkms/keys/config/{key} | Configure the key in Vault
[**get_gcpkms_pubkey**](SecretsApi.md#get_gcpkms_pubkey) | **get** /gcpkms/pubkey/{key} | Retrieve the public key associated with the named key
[**get_mongodbatlas_config**](SecretsApi.md#get_mongodbatlas_config) | **get** /mongodbatlas/config | Configure the  credentials that are used to manage Database Users.
[**get_mongodbatlas_creds**](SecretsApi.md#get_mongodbatlas_creds) | **get** /mongodbatlas/creds/{name} | Generate MongoDB Atlas Programmatic API from a specific Vault role.
[**get_mongodbatlas_role**](SecretsApi.md#get_mongodbatlas_role) | **get** /mongodbatlas/roles/{name} | Manage the roles used to generate MongoDB Atlas Programmatic API Keys.
[**get_mongodbatlas_roles**](SecretsApi.md#get_mongodbatlas_roles) | **get** /mongodbatlas/roles | List the existing roles in this backend
[**get_nomad_config_access**](SecretsApi.md#get_nomad_config_access) | **get** /nomad/config/access | 
[**get_nomad_config_lease**](SecretsApi.md#get_nomad_config_lease) | **get** /nomad/config/lease | Configure the lease parameters for generated tokens
[**get_nomad_creds**](SecretsApi.md#get_nomad_creds) | **get** /nomad/creds/{name} | 
[**get_nomad_role**](SecretsApi.md#get_nomad_role) | **get** /nomad/role/{name} | 
[**get_nomad_roles**](SecretsApi.md#get_nomad_roles) | **get** /nomad/role | 
[**get_openldap_config**](SecretsApi.md#get_openldap_config) | **get** /openldap/config | 
[**get_openldap_cred**](SecretsApi.md#get_openldap_cred) | **get** /openldap/cred/{name} | 
[**get_openldap_role**](SecretsApi.md#get_openldap_role) | **get** /openldap/role/{name} | 
[**get_openldap_roles**](SecretsApi.md#get_openldap_roles) | **get** /openldap/role | 
[**get_openldap_static_cred**](SecretsApi.md#get_openldap_static_cred) | **get** /openldap/static-cred/{name} | 
[**get_openldap_static_role**](SecretsApi.md#get_openldap_static_role) | **get** /openldap/static-role/{name} | 
[**get_openldap_static_roles**](SecretsApi.md#get_openldap_static_roles) | **get** /openldap/static-role/ | 
[**get_rabbitmq_config_lease**](SecretsApi.md#get_rabbitmq_config_lease) | **get** /rabbitmq/config/lease | Configure the lease parameters for generated credentials
[**get_rabbitmq_creds**](SecretsApi.md#get_rabbitmq_creds) | **get** /rabbitmq/creds/{name} | Request RabbitMQ credentials for a certain role.
[**get_rabbitmq_role**](SecretsApi.md#get_rabbitmq_role) | **get** /rabbitmq/roles/{name} | Manage the roles that can be created with this backend.
[**get_rabbitmq_roles**](SecretsApi.md#get_rabbitmq_roles) | **get** /rabbitmq/roles | Manage the roles that can be created with this backend.
[**get_secret_config**](SecretsApi.md#get_secret_config) | **get** /secret/config | Read the backend level settings.
[**get_secret_data**](SecretsApi.md#get_secret_data) | **get** /secret/data/{path} | Write, Read, and Delete data in the Key-Value Store.
[**get_secret_metadata**](SecretsApi.md#get_secret_metadata) | **get** /secret/metadata/{path} | Configures settings for the KV store
[**get_ssh_config_ca**](SecretsApi.md#get_ssh_config_ca) | **get** /ssh/config/ca | Set the SSH private key used for signing certificates.
[**get_ssh_config_zeroaddress**](SecretsApi.md#get_ssh_config_zeroaddress) | **get** /ssh/config/zeroaddress | Assign zero address as default CIDR block for select roles.
[**get_ssh_public_key**](SecretsApi.md#get_ssh_public_key) | **get** /ssh/public_key | Retrieve the public key.
[**get_ssh_role**](SecretsApi.md#get_ssh_role) | **get** /ssh/roles/{role} | Manage the 'roles' that can be created with this backend.
[**get_ssh_roles**](SecretsApi.md#get_ssh_roles) | **get** /ssh/roles | Manage the 'roles' that can be created with this backend.
[**get_terraform_config**](SecretsApi.md#get_terraform_config) | **get** /terraform/config | 
[**get_terraform_creds**](SecretsApi.md#get_terraform_creds) | **get** /terraform/creds/{name} | Generate a Terraform Cloud or Enterprise API token from a specific Vault role.
[**get_terraform_role**](SecretsApi.md#get_terraform_role) | **get** /terraform/role/{name} | 
[**get_terraform_roles**](SecretsApi.md#get_terraform_roles) | **get** /terraform/role | 
[**get_totp_code**](SecretsApi.md#get_totp_code) | **get** /totp/code/{name} | Request time-based one-time use password or validate a password for a certain key .
[**get_totp_key**](SecretsApi.md#get_totp_key) | **get** /totp/keys/{name} | Manage the keys that can be created with this backend.
[**get_totp_keys**](SecretsApi.md#get_totp_keys) | **get** /totp/keys | Manage the keys that can be created with this backend.
[**get_transit_backup**](SecretsApi.md#get_transit_backup) | **get** /transit/backup/{name} | Backup the named key
[**get_transit_cache_config**](SecretsApi.md#get_transit_cache_config) | **get** /transit/cache-config | Returns the size of the active cache
[**get_transit_export**](SecretsApi.md#get_transit_export) | **get** /transit/export/{type}/{name} | Export named encryption or signing key
[**get_transit_export_version**](SecretsApi.md#get_transit_export_version) | **get** /transit/export/{type}/{name}/{version} | Export named encryption or signing key
[**get_transit_key**](SecretsApi.md#get_transit_key) | **get** /transit/keys/{name} | Managed named encryption keys
[**get_transit_keys**](SecretsApi.md#get_transit_keys) | **get** /transit/keys | Managed named encryption keys
[**post_ad_config**](SecretsApi.md#post_ad_config) | **post** /ad/config | Configure the AD server to connect to, along with password options.
[**post_ad_library**](SecretsApi.md#post_ad_library) | **post** /ad/library/{name} | Update a library set.
[**post_ad_library_check_in**](SecretsApi.md#post_ad_library_check_in) | **post** /ad/library/{name}/check-in | Check service accounts in to the library.
[**post_ad_library_check_out**](SecretsApi.md#post_ad_library_check_out) | **post** /ad/library/{name}/check-out | Check a service account out from the library.
[**post_ad_library_manage_check_in**](SecretsApi.md#post_ad_library_manage_check_in) | **post** /ad/library/manage/{name}/check-in | Check service accounts in to the library.
[**post_ad_role**](SecretsApi.md#post_ad_role) | **post** /ad/roles/{name} | Manage roles to build links between Vault and Active Directory service accounts.
[**post_ad_rotate_root**](SecretsApi.md#post_ad_rotate_root) | **post** /ad/rotate-root | 
[**post_alicloud_config**](SecretsApi.md#post_alicloud_config) | **post** /alicloud/config | Configure the access key and secret to use for RAM and STS calls.
[**post_alicloud_role**](SecretsApi.md#post_alicloud_role) | **post** /alicloud/role/{name} | Read, write and reference policies and roles that API keys or STS credentials can be made for.
[**post_aws_config_lease**](SecretsApi.md#post_aws_config_lease) | **post** /aws/config/lease | Configure the default lease information for generated credentials.
[**post_aws_config_root**](SecretsApi.md#post_aws_config_root) | **post** /aws/config/root | Configure the root credentials that are used to manage IAM.
[**post_aws_config_rotate_root**](SecretsApi.md#post_aws_config_rotate_root) | **post** /aws/config/rotate-root | 
[**post_aws_creds**](SecretsApi.md#post_aws_creds) | **post** /aws/creds | Generate AWS credentials from a specific Vault role.
[**post_aws_role**](SecretsApi.md#post_aws_role) | **post** /aws/roles/{name} | Read, write and reference IAM policies that access keys can be made for.
[**post_aws_sts**](SecretsApi.md#post_aws_sts) | **post** /aws/sts/{name} | Generate AWS credentials from a specific Vault role.
[**post_azure_config**](SecretsApi.md#post_azure_config) | **post** /azure/config | Configure the Azure Secret backend.
[**post_azure_role**](SecretsApi.md#post_azure_role) | **post** /azure/roles/{name} | Manage the Vault roles used to generate Azure credentials.
[**post_consul_config_access**](SecretsApi.md#post_consul_config_access) | **post** /consul/config/access | 
[**post_consul_role**](SecretsApi.md#post_consul_role) | **post** /consul/roles/{name} | 
[**post_cubbyhole_secret**](SecretsApi.md#post_cubbyhole_secret) | **post** /cubbyhole/{path} | Store a secret at the specified location.
[**post_database_config**](SecretsApi.md#post_database_config) | **post** /database/config/{name} | Configure connection details to a database plugin.
[**post_database_reset**](SecretsApi.md#post_database_reset) | **post** /database/reset/{name} | Resets a database plugin.
[**post_database_role**](SecretsApi.md#post_database_role) | **post** /database/roles/{name} | Manage the roles that can be created with this backend.
[**post_database_rotate_role**](SecretsApi.md#post_database_rotate_role) | **post** /database/rotate-role/{name} | 
[**post_database_rotate_root**](SecretsApi.md#post_database_rotate_root) | **post** /database/rotate-root/{name} | 
[**post_database_static_role**](SecretsApi.md#post_database_static_role) | **post** /database/static-roles/{name} | Manage the static roles that can be created with this backend.
[**post_gcp_config**](SecretsApi.md#post_gcp_config) | **post** /gcp/config | 
[**post_gcp_config_rotate_root**](SecretsApi.md#post_gcp_config_rotate_root) | **post** /gcp/config/rotate-root | 
[**post_gcp_key**](SecretsApi.md#post_gcp_key) | **post** /gcp/key/{roleset} | 
[**post_gcp_roleset**](SecretsApi.md#post_gcp_roleset) | **post** /gcp/roleset/{name} | 
[**post_gcp_roleset_rotate**](SecretsApi.md#post_gcp_roleset_rotate) | **post** /gcp/roleset/{name}/rotate | 
[**post_gcp_roleset_rotate_key**](SecretsApi.md#post_gcp_roleset_rotate_key) | **post** /gcp/roleset/{name}/rotate-key | 
[**post_gcp_token**](SecretsApi.md#post_gcp_token) | **post** /gcp/token/{roleset} | 
[**post_gcpkms_config**](SecretsApi.md#post_gcpkms_config) | **post** /gcpkms/config | Configure the GCP KMS secrets engine
[**post_gcpkms_decrypt**](SecretsApi.md#post_gcpkms_decrypt) | **post** /gcpkms/decrypt/{key} | Decrypt a ciphertext value using a named key
[**post_gcpkms_encrypt**](SecretsApi.md#post_gcpkms_encrypt) | **post** /gcpkms/encrypt/{key} | Encrypt a plaintext value using a named key
[**post_gcpkms_key**](SecretsApi.md#post_gcpkms_key) | **post** /gcpkms/keys/{key} | Interact with crypto keys in Vault and Google Cloud KMS
[**post_gcpkms_keys_config**](SecretsApi.md#post_gcpkms_keys_config) | **post** /gcpkms/keys/config/{key} | Configure the key in Vault
[**post_gcpkms_keys_deregister**](SecretsApi.md#post_gcpkms_keys_deregister) | **post** /gcpkms/keys/deregister/{key} | Deregister an existing key in Vault
[**post_gcpkms_keys_register**](SecretsApi.md#post_gcpkms_keys_register) | **post** /gcpkms/keys/register/{key} | Register an existing crypto key in Google Cloud KMS
[**post_gcpkms_keys_rotate**](SecretsApi.md#post_gcpkms_keys_rotate) | **post** /gcpkms/keys/rotate/{key} | Rotate a crypto key to a new primary version
[**post_gcpkms_keys_trim**](SecretsApi.md#post_gcpkms_keys_trim) | **post** /gcpkms/keys/trim/{key} | Delete old crypto key versions from Google Cloud KMS
[**post_gcpkms_reencrypt**](SecretsApi.md#post_gcpkms_reencrypt) | **post** /gcpkms/reencrypt/{key} | Re-encrypt existing ciphertext data to a new version
[**post_gcpkms_sign**](SecretsApi.md#post_gcpkms_sign) | **post** /gcpkms/sign/{key} | Signs a message or digest using a named key
[**post_gcpkms_verify**](SecretsApi.md#post_gcpkms_verify) | **post** /gcpkms/verify/{key} | Verify a signature using a named key
[**post_mongodbatlas_config**](SecretsApi.md#post_mongodbatlas_config) | **post** /mongodbatlas/config | Configure the  credentials that are used to manage Database Users.
[**post_mongodbatlas_creds**](SecretsApi.md#post_mongodbatlas_creds) | **post** /mongodbatlas/creds/{name} | Generate MongoDB Atlas Programmatic API from a specific Vault role.
[**post_mongodbatlas_role**](SecretsApi.md#post_mongodbatlas_role) | **post** /mongodbatlas/roles/{name} | Manage the roles used to generate MongoDB Atlas Programmatic API Keys.
[**post_nomad_config_access**](SecretsApi.md#post_nomad_config_access) | **post** /nomad/config/access | 
[**post_nomad_config_lease**](SecretsApi.md#post_nomad_config_lease) | **post** /nomad/config/lease | Configure the lease parameters for generated tokens
[**post_nomad_role**](SecretsApi.md#post_nomad_role) | **post** /nomad/role/{name} | 
[**post_openldap_config**](SecretsApi.md#post_openldap_config) | **post** /openldap/config | 
[**post_openldap_role**](SecretsApi.md#post_openldap_role) | **post** /openldap/role/{name} | 
[**post_openldap_rotate_role**](SecretsApi.md#post_openldap_rotate_role) | **post** /openldap/rotate-role/{name} | 
[**post_openldap_rotate_root**](SecretsApi.md#post_openldap_rotate_root) | **post** /openldap/rotate-root | 
[**post_openldap_static_role**](SecretsApi.md#post_openldap_static_role) | **post** /openldap/static-role/{name} | 
[**post_rabbitmq_config_connection**](SecretsApi.md#post_rabbitmq_config_connection) | **post** /rabbitmq/config/connection | Configure the connection URI, username, and password to talk to RabbitMQ management HTTP API.
[**post_rabbitmq_config_lease**](SecretsApi.md#post_rabbitmq_config_lease) | **post** /rabbitmq/config/lease | Configure the lease parameters for generated credentials
[**post_rabbitmq_role**](SecretsApi.md#post_rabbitmq_role) | **post** /rabbitmq/roles/{name} | Manage the roles that can be created with this backend.
[**post_secret_config**](SecretsApi.md#post_secret_config) | **post** /secret/config | Configure backend level settings that are applied to every key in the key-value store.
[**post_secret_data**](SecretsApi.md#post_secret_data) | **post** /secret/data/{path} | Write, Read, and Delete data in the Key-Value Store.
[**post_secret_delete**](SecretsApi.md#post_secret_delete) | **post** /secret/delete/{path} | Marks one or more versions as deleted in the KV store.
[**post_secret_destroy**](SecretsApi.md#post_secret_destroy) | **post** /secret/destroy/{path} | Permanently removes one or more versions in the KV store
[**post_secret_metadata**](SecretsApi.md#post_secret_metadata) | **post** /secret/metadata/{path} | Configures settings for the KV store
[**post_secret_undelete**](SecretsApi.md#post_secret_undelete) | **post** /secret/undelete/{path} | Undeletes one or more versions from the KV store.
[**post_ssh_config_ca**](SecretsApi.md#post_ssh_config_ca) | **post** /ssh/config/ca | Set the SSH private key used for signing certificates.
[**post_ssh_config_zeroaddress**](SecretsApi.md#post_ssh_config_zeroaddress) | **post** /ssh/config/zeroaddress | Assign zero address as default CIDR block for select roles.
[**post_ssh_creds**](SecretsApi.md#post_ssh_creds) | **post** /ssh/creds/{role} | Creates a credential for establishing SSH connection with the remote host.
[**post_ssh_keys**](SecretsApi.md#post_ssh_keys) | **post** /ssh/keys/{key_name} | Register a shared private key with Vault.
[**post_ssh_lookup**](SecretsApi.md#post_ssh_lookup) | **post** /ssh/lookup | List all the roles associated with the given IP address.
[**post_ssh_role**](SecretsApi.md#post_ssh_role) | **post** /ssh/roles/{role} | Manage the 'roles' that can be created with this backend.
[**post_ssh_sign**](SecretsApi.md#post_ssh_sign) | **post** /ssh/sign/{role} | Request signing an SSH key using a certain role with the provided details.
[**post_ssh_verify**](SecretsApi.md#post_ssh_verify) | **post** /ssh/verify | Validate the OTP provided by Vault SSH Agent.
[**post_terraform_config**](SecretsApi.md#post_terraform_config) | **post** /terraform/config | 
[**post_terraform_creds**](SecretsApi.md#post_terraform_creds) | **post** /terraform/creds/{name} | Generate a Terraform Cloud or Enterprise API token from a specific Vault role.
[**post_terraform_role**](SecretsApi.md#post_terraform_role) | **post** /terraform/role/{name} | 
[**post_terraform_rotate_role**](SecretsApi.md#post_terraform_rotate_role) | **post** /terraform/rotate-role/{name} | 
[**post_totp_code**](SecretsApi.md#post_totp_code) | **post** /totp/code/{name} | Request time-based one-time use password or validate a password for a certain key .
[**post_totp_key**](SecretsApi.md#post_totp_key) | **post** /totp/keys/{name} | Manage the keys that can be created with this backend.
[**post_transit_cache_config**](SecretsApi.md#post_transit_cache_config) | **post** /transit/cache-config | Configures a new cache of the specified size
[**post_transit_datakey**](SecretsApi.md#post_transit_datakey) | **post** /transit/datakey/{plaintext}/{name} | Generate a data key
[**post_transit_decrypt**](SecretsApi.md#post_transit_decrypt) | **post** /transit/decrypt/{name} | Decrypt a ciphertext value using a named key
[**post_transit_encrypt**](SecretsApi.md#post_transit_encrypt) | **post** /transit/encrypt/{name} | Encrypt a plaintext value or a batch of plaintext blocks using a named key
[**post_transit_hash**](SecretsApi.md#post_transit_hash) | **post** /transit/hash | Generate a hash sum for input data
[**post_transit_hmac**](SecretsApi.md#post_transit_hmac) | **post** /transit/hmac/{name} | Generate an HMAC for input data using the named key
[**post_transit_key**](SecretsApi.md#post_transit_key) | **post** /transit/keys/{name} | Managed named encryption keys
[**post_transit_key_config**](SecretsApi.md#post_transit_key_config) | **post** /transit/keys/{name}/config | Configure a named encryption key
[**post_transit_key_rotate**](SecretsApi.md#post_transit_key_rotate) | **post** /transit/keys/{name}/rotate | Rotate named encryption key
[**post_transit_key_trim**](SecretsApi.md#post_transit_key_trim) | **post** /transit/keys/{name}/trim | Trim key versions of a named key
[**post_transit_random**](SecretsApi.md#post_transit_random) | **post** /transit/random | Generate random bytes
[**post_transit_restore**](SecretsApi.md#post_transit_restore) | **post** /transit/restore | Restore the named key
[**post_transit_rewrap**](SecretsApi.md#post_transit_rewrap) | **post** /transit/rewrap/{name} | Rewrap ciphertext
[**post_transit_sign**](SecretsApi.md#post_transit_sign) | **post** /transit/sign/{name} | Generate a signature for input data using the named key
[**post_transit_verify**](SecretsApi.md#post_transit_verify) | **post** /transit/verify/{name} | Verify a signature or HMAC for input data created using the named key



## delete_ad_config

> delete_ad_config()
Configure the AD server to connect to, along with password options.

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


## delete_ad_library

> delete_ad_library(name)
Delete a library set.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_ad_role

> delete_ad_role(name)
Manage roles to build links between Vault and Active Directory service accounts.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_alicloud_config

> delete_alicloud_config()
Configure the access key and secret to use for RAM and STS calls.

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


## delete_alicloud_role

> delete_alicloud_role(name)
Read, write and reference policies and roles that API keys or STS credentials can be made for.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_aws_role

> delete_aws_role(name)
Read, write and reference IAM policies that access keys can be made for.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the policy | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_azure_config

> delete_azure_config()
Configure the Azure Secret backend.

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


## delete_azure_role

> delete_azure_role(name)
Manage the Vault roles used to generate Azure credentials.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_consul_role

> delete_consul_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_cubbyhole_secret

> delete_cubbyhole_secret(path)
Deletes the secret at the specified location.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Specifies the path of the secret. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_database_config

> delete_database_config(name)
Configure connection details to a database plugin.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of this database connection | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_database_role

> delete_database_role(name)
Manage the roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_database_static_role

> delete_database_static_role(name)
Manage the static roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_gcp_roleset

> delete_gcp_roleset(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Required. Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_gcpkms_config

> delete_gcpkms_config()
Configure the GCP KMS secrets engine

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


## delete_gcpkms_key

> delete_gcpkms_key(key)
Interact with crypto keys in Vault and Google Cloud KMS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_gcpkms_keys_deregister

> delete_gcpkms_keys_deregister(key)
Deregister an existing key in Vault

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key to deregister in Vault. If the key exists in Google Cloud KMS, it will be left untouched. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_gcpkms_keys_trim

> delete_gcpkms_keys_trim(key)
Delete old crypto key versions from Google Cloud KMS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_mongodbatlas_role

> delete_mongodbatlas_role(name)
Manage the roles used to generate MongoDB Atlas Programmatic API Keys.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the Roles | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_nomad_config_access

> delete_nomad_config_access()


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


## delete_nomad_config_lease

> delete_nomad_config_lease()
Configure the lease parameters for generated tokens

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


## delete_nomad_role

> delete_nomad_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_openldap_config

> delete_openldap_config()


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


## delete_openldap_role

> delete_openldap_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role (lowercase) | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_openldap_static_role

> delete_openldap_static_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_rabbitmq_role

> delete_rabbitmq_role(name)
Manage the roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_secret_data

> delete_secret_data(path)
Write, Read, and Delete data in the Key-Value Store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_secret_metadata

> delete_secret_metadata(path)
Configures settings for the KV store

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_ssh_config_ca

> delete_ssh_config_ca()
Set the SSH private key used for signing certificates.

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


## delete_ssh_config_zeroaddress

> delete_ssh_config_zeroaddress()
Assign zero address as default CIDR block for select roles.

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


## delete_ssh_keys

> delete_ssh_keys(key_name)
Register a shared private key with Vault.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key_name** | **String** | [Required] Name of the key | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_ssh_role

> delete_ssh_role(role)
Manage the 'roles' that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | [Required for all types] Name of the role being created. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_terraform_config

> delete_terraform_config()


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


## delete_terraform_role

> delete_terraform_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_totp_key

> delete_totp_key(name)
Manage the keys that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_transit_key

> delete_transit_key(name)
Managed named encryption keys

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ad_config

> crate::models::AdConfig get_ad_config()
Configure the AD server to connect to, along with password options.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::AdConfig**](AdConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ad_creds

> get_ad_creds(name)
Retrieve a role's creds by role name.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ad_libraries

> get_ad_libraries(list)


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


## get_ad_library

> crate::models::AdLibrary get_ad_library(name)
Read a library set.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set. | [required] |

### Return type

[**crate::models::AdLibrary**](AdLibrary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ad_library_status

> get_ad_library_status(name)
Check the status of the service accounts in a library set.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ad_role

> crate::models::AdRole get_ad_role(name)
Manage roles to build links between Vault and Active Directory service accounts.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

[**crate::models::AdRole**](AdRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ad_roles

> get_ad_roles(list)
List the name of each role currently stored.

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


## get_ad_rotate_root

> get_ad_rotate_root()


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


## get_alicloud_config

> crate::models::AlicloudConfig get_alicloud_config()
Configure the access key and secret to use for RAM and STS calls.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::AlicloudConfig**](AlicloudConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_alicloud_creds

> get_alicloud_creds(name)
Generate an API key or STS credential using the given role's configuration.'

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_alicloud_role

> crate::models::AlicloudRole get_alicloud_role(name)
Read, write and reference policies and roles that API keys or STS credentials can be made for.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the role. | [required] |

### Return type

[**crate::models::AlicloudRole**](AlicloudRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_alicloud_roles

> get_alicloud_roles(list)
List the existing roles in this backend.

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


## get_aws_config_lease

> crate::models::AwsConfigLease get_aws_config_lease()
Configure the default lease information for generated credentials.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::AwsConfigLease**](AwsConfigLease.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_aws_config_root

> crate::models::AwsConfigRoot get_aws_config_root()
Configure the root credentials that are used to manage IAM.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::AwsConfigRoot**](AwsConfigRoot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_aws_creds

> crate::models::AwsCreds get_aws_creds()
Generate AWS credentials from a specific Vault role.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::AwsCreds**](AwsCreds.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_aws_role

> crate::models::AwsRole get_aws_role(name)
Read, write and reference IAM policies that access keys can be made for.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the policy | [required] |

### Return type

[**crate::models::AwsRole**](AwsRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_aws_roles

> get_aws_roles(list)
List the existing roles in this backend

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


## get_aws_sts

> crate::models::AwsSts get_aws_sts(name)
Generate AWS credentials from a specific Vault role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

[**crate::models::AwsSts**](AwsSts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_azure_config

> crate::models::AzureConfig get_azure_config()
Configure the Azure Secret backend.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::AzureConfig**](AzureConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_azure_creds

> get_azure_creds(role)
Request Service Principal credentials for a given Vault role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | Name of the Vault role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_azure_role

> crate::models::AzureRole get_azure_role(name)
Manage the Vault roles used to generate Azure credentials.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

[**crate::models::AzureRole**](AzureRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_azure_roles

> get_azure_roles(list)
List existing roles.

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


## get_consul_config_access

> crate::models::ConsulConfigAccess get_consul_config_access()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::ConsulConfigAccess**](ConsulConfigAccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_consul_creds

> get_consul_creds(role)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_consul_role

> crate::models::ConsulRole get_consul_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

[**crate::models::ConsulRole**](ConsulRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_consul_roles

> get_consul_roles(list)


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


## get_cubbyhole_secret

> get_cubbyhole_secret(path, list)
Retrieve the secret at the specified location.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Specifies the path of the secret. | [required] |
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_database_config

> crate::models::DatabaseConfig get_database_config(name)
Configure connection details to a database plugin.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of this database connection | [required] |

### Return type

[**crate::models::DatabaseConfig**](DatabaseConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_database_configs

> get_database_configs(list)
Configure connection details to a database plugin.

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


## get_database_creds

> get_database_creds(name)
Request database credentials for a certain role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_database_role

> crate::models::DatabaseRole get_database_role(name)
Manage the roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

[**crate::models::DatabaseRole**](DatabaseRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_database_roles

> get_database_roles(list)
Manage the roles that can be created with this backend.

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


## get_database_static_creds

> get_database_static_creds(name)
Request database credentials for a certain static role. These credentials are rotated periodically.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the static role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_database_static_role

> crate::models::DatabaseStaticRole get_database_static_role(name)
Manage the static roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

[**crate::models::DatabaseStaticRole**](DatabaseStaticRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_database_static_roles

> get_database_static_roles(list)
Manage the static roles that can be created with this backend.

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


## get_gcp_config

> crate::models::GcpConfig get_gcp_config()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::GcpConfig**](GcpConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_gcp_key

> crate::models::GcpKey get_gcp_key(roleset)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**roleset** | **String** | Required. Name of the role set. | [required] |

### Return type

[**crate::models::GcpKey**](GcpKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_gcp_roleset

> crate::models::GcpRoleset get_gcp_roleset(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Required. Name of the role. | [required] |

### Return type

[**crate::models::GcpRoleset**](GcpRoleset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_gcp_rolesets

> get_gcp_rolesets(list)


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


## get_gcp_token

> get_gcp_token(roleset)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**roleset** | **String** | Required. Name of the role set. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_gcpkms_config

> crate::models::GcpkmsConfig get_gcpkms_config()
Configure the GCP KMS secrets engine

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::GcpkmsConfig**](GcpkmsConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_gcpkms_key

> crate::models::GcpkmsKey get_gcpkms_key(key)
Interact with crypto keys in Vault and Google Cloud KMS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault. | [required] |

### Return type

[**crate::models::GcpkmsKey**](GcpkmsKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_gcpkms_keys

> get_gcpkms_keys(list)
List named keys

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


## get_gcpkms_keys_config

> crate::models::GcpkmsKeysConfig get_gcpkms_keys_config(key)
Configure the key in Vault

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault. | [required] |

### Return type

[**crate::models::GcpkmsKeysConfig**](GcpkmsKeysConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_gcpkms_pubkey

> get_gcpkms_pubkey(key)
Retrieve the public key associated with the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key for which to get the public key. This key must already exist in Vault and Google Cloud KMS. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_mongodbatlas_config

> crate::models::MongodbatlasConfig get_mongodbatlas_config()
Configure the  credentials that are used to manage Database Users.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::MongodbatlasConfig**](MongodbatlasConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_mongodbatlas_creds

> get_mongodbatlas_creds(name)
Generate MongoDB Atlas Programmatic API from a specific Vault role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_mongodbatlas_role

> crate::models::MongodbatlasRole get_mongodbatlas_role(name)
Manage the roles used to generate MongoDB Atlas Programmatic API Keys.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the Roles | [required] |

### Return type

[**crate::models::MongodbatlasRole**](MongodbatlasRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_mongodbatlas_roles

> get_mongodbatlas_roles(list)
List the existing roles in this backend

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


## get_nomad_config_access

> crate::models::NomadConfigAccess get_nomad_config_access()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::NomadConfigAccess**](NomadConfigAccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_nomad_config_lease

> crate::models::NomadConfigLease get_nomad_config_lease()
Configure the lease parameters for generated tokens

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::NomadConfigLease**](NomadConfigLease.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_nomad_creds

> get_nomad_creds(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_nomad_role

> crate::models::NomadRole get_nomad_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

[**crate::models::NomadRole**](NomadRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_nomad_roles

> get_nomad_roles(list)


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


## get_openldap_config

> crate::models::OpenldapConfig get_openldap_config()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::OpenldapConfig**](OpenldapConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_openldap_cred

> get_openldap_cred(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the dynamic role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_openldap_role

> crate::models::OpenldapRole get_openldap_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role (lowercase) | [required] |

### Return type

[**crate::models::OpenldapRole**](OpenldapRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_openldap_roles

> get_openldap_roles(list)


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


## get_openldap_static_cred

> get_openldap_static_cred(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the static role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_openldap_static_role

> crate::models::OpenldapStaticRole get_openldap_static_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

[**crate::models::OpenldapStaticRole**](OpenldapStaticRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_openldap_static_roles

> get_openldap_static_roles(list)


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


## get_rabbitmq_config_lease

> crate::models::RabbitmqConfigLease get_rabbitmq_config_lease()
Configure the lease parameters for generated credentials

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::RabbitmqConfigLease**](RabbitmqConfigLease.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_rabbitmq_creds

> get_rabbitmq_creds(name)
Request RabbitMQ credentials for a certain role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_rabbitmq_role

> crate::models::RabbitmqRole get_rabbitmq_role(name)
Manage the roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

[**crate::models::RabbitmqRole**](RabbitmqRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_rabbitmq_roles

> get_rabbitmq_roles(list)
Manage the roles that can be created with this backend.

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


## get_secret_config

> crate::models::SecretConfig get_secret_config()
Read the backend level settings.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::SecretConfig**](SecretConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_secret_data

> crate::models::SecretData get_secret_data(path)
Write, Read, and Delete data in the Key-Value Store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |

### Return type

[**crate::models::SecretData**](SecretData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_secret_metadata

> crate::models::SecretMetadata get_secret_metadata(path, list)
Configures settings for the KV store

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

[**crate::models::SecretMetadata**](SecretMetadata.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ssh_config_ca

> crate::models::SshConfigCa get_ssh_config_ca()
Set the SSH private key used for signing certificates.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::SshConfigCa**](SshConfigCa.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ssh_config_zeroaddress

> crate::models::SshConfigZeroaddress get_ssh_config_zeroaddress()
Assign zero address as default CIDR block for select roles.

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::SshConfigZeroaddress**](SshConfigZeroaddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ssh_public_key

> get_ssh_public_key()
Retrieve the public key.

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


## get_ssh_role

> crate::models::SshRole get_ssh_role(role)
Manage the 'roles' that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | [Required for all types] Name of the role being created. | [required] |

### Return type

[**crate::models::SshRole**](SshRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ssh_roles

> get_ssh_roles(list)
Manage the 'roles' that can be created with this backend.

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


## get_terraform_config

> crate::models::TerraformConfig get_terraform_config()


### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::TerraformConfig**](TerraformConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_terraform_creds

> get_terraform_creds(name)
Generate a Terraform Cloud or Enterprise API token from a specific Vault role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_terraform_role

> crate::models::TerraformRole get_terraform_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

[**crate::models::TerraformRole**](TerraformRole.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_terraform_roles

> get_terraform_roles(list)


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


## get_totp_code

> crate::models::TotpCode get_totp_code(name)
Request time-based one-time use password or validate a password for a certain key .

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key. | [required] |

### Return type

[**crate::models::TotpCode**](TotpCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_totp_key

> crate::models::TotpKey get_totp_key(name)
Manage the keys that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key. | [required] |

### Return type

[**crate::models::TotpKey**](TotpKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_totp_keys

> get_totp_keys(list)
Manage the keys that can be created with this backend.

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


## get_transit_backup

> get_transit_backup(name)
Backup the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_transit_cache_config

> crate::models::TransitCacheConfig get_transit_cache_config()
Returns the size of the active cache

### Parameters

This endpoint does not need any parameter.

### Return type

[**crate::models::TransitCacheConfig**](TransitCacheConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_transit_export

> get_transit_export(name, _type)
Export named encryption or signing key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |
**_type** | **String** | Type of key to export (encryption-key, signing-key, hmac-key) | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_transit_export_version

> get_transit_export_version(name, _type, version)
Export named encryption or signing key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |
**_type** | **String** | Type of key to export (encryption-key, signing-key, hmac-key) | [required] |
**version** | **String** | Version of the key | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_transit_key

> crate::models::TransitKey get_transit_key(name)
Managed named encryption keys

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |

### Return type

[**crate::models::TransitKey**](TransitKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_transit_keys

> get_transit_keys(list)
Managed named encryption keys

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


## post_ad_config

> post_ad_config(ad_config_input)
Configure the AD server to connect to, along with password options.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**ad_config_input** | Option<[**AdConfigInput**](AdConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_library

> post_ad_library(name, ad_library_input)
Update a library set.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set. | [required] |
**ad_library_input** | Option<[**AdLibraryInput**](AdLibraryInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_library_check_in

> post_ad_library_check_in(name, ad_library_check_in_input)
Check service accounts in to the library.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set. | [required] |
**ad_library_check_in_input** | Option<[**AdLibraryCheckInInput**](AdLibraryCheckInInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_library_check_out

> post_ad_library_check_out(name, ad_library_check_out_input)
Check a service account out from the library.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set | [required] |
**ad_library_check_out_input** | Option<[**AdLibraryCheckOutInput**](AdLibraryCheckOutInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_library_manage_check_in

> post_ad_library_manage_check_in(name, ad_library_manage_check_in_input)
Check service accounts in to the library.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set. | [required] |
**ad_library_manage_check_in_input** | Option<[**AdLibraryManageCheckInInput**](AdLibraryManageCheckInInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_role

> post_ad_role(name, ad_role_input)
Manage roles to build links between Vault and Active Directory service accounts.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**ad_role_input** | Option<[**AdRoleInput**](AdRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_rotate_root

> post_ad_rotate_root()


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


## post_alicloud_config

> post_alicloud_config(alicloud_config_input)
Configure the access key and secret to use for RAM and STS calls.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**alicloud_config_input** | Option<[**AlicloudConfigInput**](AlicloudConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_alicloud_role

> post_alicloud_role(name, alicloud_role_input)
Read, write and reference policies and roles that API keys or STS credentials can be made for.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the role. | [required] |
**alicloud_role_input** | Option<[**AlicloudRoleInput**](AlicloudRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_aws_config_lease

> post_aws_config_lease(aws_config_lease_input)
Configure the default lease information for generated credentials.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**aws_config_lease_input** | Option<[**AwsConfigLeaseInput**](AwsConfigLeaseInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_aws_config_root

> post_aws_config_root(aws_config_root_input)
Configure the root credentials that are used to manage IAM.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**aws_config_root_input** | Option<[**AwsConfigRootInput**](AwsConfigRootInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_aws_config_rotate_root

> post_aws_config_rotate_root()


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


## post_aws_creds

> post_aws_creds(aws_creds_input)
Generate AWS credentials from a specific Vault role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**aws_creds_input** | Option<[**AwsCredsInput**](AwsCredsInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_aws_role

> post_aws_role(name, aws_role_input)
Read, write and reference IAM policies that access keys can be made for.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the policy | [required] |
**aws_role_input** | Option<[**AwsRoleInput**](AwsRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_aws_sts

> post_aws_sts(name, aws_sts_input)
Generate AWS credentials from a specific Vault role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**aws_sts_input** | Option<[**AwsStsInput**](AwsStsInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_azure_config

> post_azure_config(azure_config_input)
Configure the Azure Secret backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**azure_config_input** | Option<[**AzureConfigInput**](AzureConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_azure_role

> post_azure_role(name, azure_role_input)
Manage the Vault roles used to generate Azure credentials.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**azure_role_input** | Option<[**AzureRoleInput**](AzureRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_consul_config_access

> post_consul_config_access(consul_config_access_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**consul_config_access_input** | Option<[**ConsulConfigAccessInput**](ConsulConfigAccessInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_consul_role

> post_consul_role(name, consul_role_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**consul_role_input** | Option<[**ConsulRoleInput**](ConsulRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_cubbyhole_secret

> post_cubbyhole_secret(path)
Store a secret at the specified location.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Specifies the path of the secret. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_database_config

> post_database_config(name, database_config_input)
Configure connection details to a database plugin.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of this database connection | [required] |
**database_config_input** | Option<[**DatabaseConfigInput**](DatabaseConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_database_reset

> post_database_reset(name)
Resets a database plugin.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of this database connection | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_database_role

> post_database_role(name, database_role_input)
Manage the roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**database_role_input** | Option<[**DatabaseRoleInput**](DatabaseRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_database_rotate_role

> post_database_rotate_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the static role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_database_rotate_root

> post_database_rotate_root(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of this database connection | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_database_static_role

> post_database_static_role(name, database_static_role_input)
Manage the static roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**database_static_role_input** | Option<[**DatabaseStaticRoleInput**](DatabaseStaticRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcp_config

> post_gcp_config(gcp_config_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**gcp_config_input** | Option<[**GcpConfigInput**](GcpConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcp_config_rotate_root

> post_gcp_config_rotate_root()


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


## post_gcp_key

> post_gcp_key(roleset, gcp_key_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**roleset** | **String** | Required. Name of the role set. | [required] |
**gcp_key_input** | Option<[**GcpKeyInput**](GcpKeyInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcp_roleset

> post_gcp_roleset(name, gcp_roleset_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Required. Name of the role. | [required] |
**gcp_roleset_input** | Option<[**GcpRolesetInput**](GcpRolesetInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcp_roleset_rotate

> post_gcp_roleset_rotate(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcp_roleset_rotate_key

> post_gcp_roleset_rotate_key(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcp_token

> post_gcp_token(roleset)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**roleset** | **String** | Required. Name of the role set. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_config

> post_gcpkms_config(gcpkms_config_input)
Configure the GCP KMS secrets engine

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**gcpkms_config_input** | Option<[**GcpkmsConfigInput**](GcpkmsConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_decrypt

> post_gcpkms_decrypt(key, gcpkms_decrypt_input)
Decrypt a ciphertext value using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault to use for decryption. This key must already exist in Vault and must map back to a Google Cloud KMS key. | [required] |
**gcpkms_decrypt_input** | Option<[**GcpkmsDecryptInput**](GcpkmsDecryptInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_encrypt

> post_gcpkms_encrypt(key, gcpkms_encrypt_input)
Encrypt a plaintext value using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault to use for encryption. This key must already exist in Vault and must map back to a Google Cloud KMS key. | [required] |
**gcpkms_encrypt_input** | Option<[**GcpkmsEncryptInput**](GcpkmsEncryptInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_key

> post_gcpkms_key(key, gcpkms_key_input)
Interact with crypto keys in Vault and Google Cloud KMS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault. | [required] |
**gcpkms_key_input** | Option<[**GcpkmsKeyInput**](GcpkmsKeyInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_keys_config

> post_gcpkms_keys_config(key, gcpkms_keys_config_input)
Configure the key in Vault

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault. | [required] |
**gcpkms_keys_config_input** | Option<[**GcpkmsKeysConfigInput**](GcpkmsKeysConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_keys_deregister

> post_gcpkms_keys_deregister(key)
Deregister an existing key in Vault

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key to deregister in Vault. If the key exists in Google Cloud KMS, it will be left untouched. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_keys_register

> post_gcpkms_keys_register(key, gcpkms_keys_register_input)
Register an existing crypto key in Google Cloud KMS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key to register in Vault. This will be the named used to refer to the underlying crypto key when encrypting or decrypting data. | [required] |
**gcpkms_keys_register_input** | Option<[**GcpkmsKeysRegisterInput**](GcpkmsKeysRegisterInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_keys_rotate

> post_gcpkms_keys_rotate(key)
Rotate a crypto key to a new primary version

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key to rotate. This key must already be registered with Vault and point to a valid Google Cloud KMS crypto key. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_keys_trim

> post_gcpkms_keys_trim(key)
Delete old crypto key versions from Google Cloud KMS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_reencrypt

> post_gcpkms_reencrypt(key, gcpkms_reencrypt_input)
Re-encrypt existing ciphertext data to a new version

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key to use for encryption. This key must already exist in Vault and Google Cloud KMS. | [required] |
**gcpkms_reencrypt_input** | Option<[**GcpkmsReencryptInput**](GcpkmsReencryptInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_sign

> post_gcpkms_sign(key, gcpkms_sign_input)
Signs a message or digest using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault to use for signing. This key must already exist in Vault and must map back to a Google Cloud KMS key. | [required] |
**gcpkms_sign_input** | Option<[**GcpkmsSignInput**](GcpkmsSignInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_verify

> post_gcpkms_verify(key, gcpkms_verify_input)
Verify a signature using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault to use for verification. This key must already exist in Vault and must map back to a Google Cloud KMS key. | [required] |
**gcpkms_verify_input** | Option<[**GcpkmsVerifyInput**](GcpkmsVerifyInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_mongodbatlas_config

> post_mongodbatlas_config(mongodbatlas_config_input)
Configure the  credentials that are used to manage Database Users.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**mongodbatlas_config_input** | Option<[**MongodbatlasConfigInput**](MongodbatlasConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_mongodbatlas_creds

> post_mongodbatlas_creds(name)
Generate MongoDB Atlas Programmatic API from a specific Vault role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_mongodbatlas_role

> post_mongodbatlas_role(name, mongodbatlas_role_input)
Manage the roles used to generate MongoDB Atlas Programmatic API Keys.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the Roles | [required] |
**mongodbatlas_role_input** | Option<[**MongodbatlasRoleInput**](MongodbatlasRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_nomad_config_access

> post_nomad_config_access(nomad_config_access_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**nomad_config_access_input** | Option<[**NomadConfigAccessInput**](NomadConfigAccessInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_nomad_config_lease

> post_nomad_config_lease(nomad_config_lease_input)
Configure the lease parameters for generated tokens

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**nomad_config_lease_input** | Option<[**NomadConfigLeaseInput**](NomadConfigLeaseInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_nomad_role

> post_nomad_role(name, nomad_role_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**nomad_role_input** | Option<[**NomadRoleInput**](NomadRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_openldap_config

> post_openldap_config(openldap_config_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**openldap_config_input** | Option<[**OpenldapConfigInput**](OpenldapConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_openldap_role

> post_openldap_role(name, openldap_role_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role (lowercase) | [required] |
**openldap_role_input** | Option<[**OpenldapRoleInput**](OpenldapRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_openldap_rotate_role

> post_openldap_rotate_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the static role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_openldap_rotate_root

> post_openldap_rotate_root()


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


## post_openldap_static_role

> post_openldap_static_role(name, openldap_static_role_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**openldap_static_role_input** | Option<[**OpenldapStaticRoleInput**](OpenldapStaticRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_rabbitmq_config_connection

> post_rabbitmq_config_connection(rabbitmq_config_connection_input)
Configure the connection URI, username, and password to talk to RabbitMQ management HTTP API.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**rabbitmq_config_connection_input** | Option<[**RabbitmqConfigConnectionInput**](RabbitmqConfigConnectionInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_rabbitmq_config_lease

> post_rabbitmq_config_lease(rabbitmq_config_lease_input)
Configure the lease parameters for generated credentials

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**rabbitmq_config_lease_input** | Option<[**RabbitmqConfigLeaseInput**](RabbitmqConfigLeaseInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_rabbitmq_role

> post_rabbitmq_role(name, rabbitmq_role_input)
Manage the roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**rabbitmq_role_input** | Option<[**RabbitmqRoleInput**](RabbitmqRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_config

> post_secret_config(secret_config_input)
Configure backend level settings that are applied to every key in the key-value store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**secret_config_input** | Option<[**SecretConfigInput**](SecretConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_data

> post_secret_data(path, secret_data_input)
Write, Read, and Delete data in the Key-Value Store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**secret_data_input** | Option<[**SecretDataInput**](SecretDataInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_delete

> post_secret_delete(path, secret_delete_input)
Marks one or more versions as deleted in the KV store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**secret_delete_input** | Option<[**SecretDeleteInput**](SecretDeleteInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_destroy

> post_secret_destroy(path, secret_destroy_input)
Permanently removes one or more versions in the KV store

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**secret_destroy_input** | Option<[**SecretDestroyInput**](SecretDestroyInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_metadata

> post_secret_metadata(path, secret_metadata_input)
Configures settings for the KV store

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**secret_metadata_input** | Option<[**SecretMetadataInput**](SecretMetadataInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_undelete

> post_secret_undelete(path, secret_undelete_input)
Undeletes one or more versions from the KV store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**secret_undelete_input** | Option<[**SecretUndeleteInput**](SecretUndeleteInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_config_ca

> post_ssh_config_ca(ssh_config_ca_input)
Set the SSH private key used for signing certificates.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**ssh_config_ca_input** | Option<[**SshConfigCaInput**](SshConfigCaInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_config_zeroaddress

> post_ssh_config_zeroaddress(ssh_config_zeroaddress_input)
Assign zero address as default CIDR block for select roles.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**ssh_config_zeroaddress_input** | Option<[**SshConfigZeroaddressInput**](SshConfigZeroaddressInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_creds

> post_ssh_creds(role, ssh_creds_input)
Creates a credential for establishing SSH connection with the remote host.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | [Required] Name of the role | [required] |
**ssh_creds_input** | Option<[**SshCredsInput**](SshCredsInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_keys

> post_ssh_keys(key_name, ssh_keys_input)
Register a shared private key with Vault.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key_name** | **String** | [Required] Name of the key | [required] |
**ssh_keys_input** | Option<[**SshKeysInput**](SshKeysInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_lookup

> post_ssh_lookup(ssh_lookup_input)
List all the roles associated with the given IP address.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**ssh_lookup_input** | Option<[**SshLookupInput**](SshLookupInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_role

> post_ssh_role(role, ssh_role_input)
Manage the 'roles' that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | [Required for all types] Name of the role being created. | [required] |
**ssh_role_input** | Option<[**SshRoleInput**](SshRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_sign

> post_ssh_sign(role, ssh_sign_input)
Request signing an SSH key using a certain role with the provided details.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | The desired role with configuration for this request. | [required] |
**ssh_sign_input** | Option<[**SshSignInput**](SshSignInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_verify

> post_ssh_verify(ssh_verify_input)
Validate the OTP provided by Vault SSH Agent.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**ssh_verify_input** | Option<[**SshVerifyInput**](SshVerifyInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_terraform_config

> post_terraform_config(terraform_config_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**terraform_config_input** | Option<[**TerraformConfigInput**](TerraformConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_terraform_creds

> post_terraform_creds(name)
Generate a Terraform Cloud or Enterprise API token from a specific Vault role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_terraform_role

> post_terraform_role(name, terraform_role_input)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**terraform_role_input** | Option<[**TerraformRoleInput**](TerraformRoleInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_terraform_rotate_role

> post_terraform_rotate_role(name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the team or organization role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_totp_code

> post_totp_code(name, totp_code_input)
Request time-based one-time use password or validate a password for a certain key .

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key. | [required] |
**totp_code_input** | Option<[**TotpCodeInput**](TotpCodeInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_totp_key

> post_totp_key(name, totp_key_input)
Manage the keys that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key. | [required] |
**totp_key_input** | Option<[**TotpKeyInput**](TotpKeyInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_cache_config

> post_transit_cache_config(transit_cache_config_input)
Configures a new cache of the specified size

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**transit_cache_config_input** | Option<[**TransitCacheConfigInput**](TransitCacheConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_datakey

> post_transit_datakey(name, plaintext, transit_datakey_input)
Generate a data key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The backend key used for encrypting the data key | [required] |
**plaintext** | **String** | \"plaintext\" will return the key in both plaintext and ciphertext; \"wrapped\" will return the ciphertext only. | [required] |
**transit_datakey_input** | Option<[**TransitDatakeyInput**](TransitDatakeyInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_decrypt

> post_transit_decrypt(name, transit_decrypt_input)
Decrypt a ciphertext value using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the policy | [required] |
**transit_decrypt_input** | Option<[**TransitDecryptInput**](TransitDecryptInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_encrypt

> post_transit_encrypt(name, transit_encrypt_input)
Encrypt a plaintext value or a batch of plaintext blocks using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the policy | [required] |
**transit_encrypt_input** | Option<[**TransitEncryptInput**](TransitEncryptInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_hash

> post_transit_hash(transit_hash_input)
Generate a hash sum for input data

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**transit_hash_input** | Option<[**TransitHashInput**](TransitHashInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_hmac

> post_transit_hmac(name, transit_hmac_input)
Generate an HMAC for input data using the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The key to use for the HMAC function | [required] |
**transit_hmac_input** | Option<[**TransitHmacInput**](TransitHmacInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_key

> post_transit_key(name, transit_key_input)
Managed named encryption keys

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |
**transit_key_input** | Option<[**TransitKeyInput**](TransitKeyInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_key_config

> post_transit_key_config(name, transit_key_config_input)
Configure a named encryption key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |
**transit_key_config_input** | Option<[**TransitKeyConfigInput**](TransitKeyConfigInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_key_rotate

> post_transit_key_rotate(name)
Rotate named encryption key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_key_trim

> post_transit_key_trim(name, transit_key_trim_input)
Trim key versions of a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |
**transit_key_trim_input** | Option<[**TransitKeyTrimInput**](TransitKeyTrimInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_random

> post_transit_random(transit_random_input)
Generate random bytes

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**transit_random_input** | Option<[**TransitRandomInput**](TransitRandomInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_restore

> post_transit_restore(transit_restore_input)
Restore the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**transit_restore_input** | Option<[**TransitRestoreInput**](TransitRestoreInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_rewrap

> post_transit_rewrap(name, transit_rewrap_input)
Rewrap ciphertext

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |
**transit_rewrap_input** | Option<[**TransitRewrapInput**](TransitRewrapInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_sign

> post_transit_sign(name, transit_sign_input)
Generate a signature for input data using the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The key to use | [required] |
**transit_sign_input** | Option<[**TransitSignInput**](TransitSignInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_verify

> post_transit_verify(name, transit_verify_input)
Verify a signature or HMAC for input data created using the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The key to use | [required] |
**transit_verify_input** | Option<[**TransitVerifyInput**](TransitVerifyInput.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

