# \SecretsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ad_config**](SecretsApi.md#delete_ad_config) | **delete** /ad/config | Configure the AD server to connect to, along with password options.
[**delete_ad_library_name**](SecretsApi.md#delete_ad_library_name) | **delete** /ad/library/{name} | Delete a library set.
[**delete_ad_roles_name**](SecretsApi.md#delete_ad_roles_name) | **delete** /ad/roles/{name} | Manage roles to build links between Vault and Active Directory service accounts.
[**delete_alicloud_config**](SecretsApi.md#delete_alicloud_config) | **delete** /alicloud/config | Configure the access key and secret to use for RAM and STS calls.
[**delete_alicloud_role_name**](SecretsApi.md#delete_alicloud_role_name) | **delete** /alicloud/role/{name} | Read, write and reference policies and roles that API keys or STS credentials can be made for.
[**delete_aws_roles_name**](SecretsApi.md#delete_aws_roles_name) | **delete** /aws/roles/{name} | Read, write and reference IAM policies that access keys can be made for.
[**delete_azure_config**](SecretsApi.md#delete_azure_config) | **delete** /azure/config | Configure the Azure Secret backend.
[**delete_azure_roles_name**](SecretsApi.md#delete_azure_roles_name) | **delete** /azure/roles/{name} | Manage the Vault roles used to generate Azure credentials.
[**delete_consul_roles_name**](SecretsApi.md#delete_consul_roles_name) | **delete** /consul/roles/{name} | 
[**delete_cubbyhole_path**](SecretsApi.md#delete_cubbyhole_path) | **delete** /cubbyhole/{path} | Deletes the secret at the specified location.
[**delete_database_config_name**](SecretsApi.md#delete_database_config_name) | **delete** /database/config/{name} | Configure connection details to a database plugin.
[**delete_database_roles_name**](SecretsApi.md#delete_database_roles_name) | **delete** /database/roles/{name} | Manage the roles that can be created with this backend.
[**delete_database_static_roles_name**](SecretsApi.md#delete_database_static_roles_name) | **delete** /database/static-roles/{name} | Manage the static roles that can be created with this backend.
[**delete_gcp_roleset_name**](SecretsApi.md#delete_gcp_roleset_name) | **delete** /gcp/roleset/{name} | 
[**delete_gcpkms_config**](SecretsApi.md#delete_gcpkms_config) | **delete** /gcpkms/config | Configure the GCP KMS secrets engine
[**delete_gcpkms_keys_deregister_key**](SecretsApi.md#delete_gcpkms_keys_deregister_key) | **delete** /gcpkms/keys/deregister/{key} | Deregister an existing key in Vault
[**delete_gcpkms_keys_key**](SecretsApi.md#delete_gcpkms_keys_key) | **delete** /gcpkms/keys/{key} | Interact with crypto keys in Vault and Google Cloud KMS
[**delete_gcpkms_keys_trim_key**](SecretsApi.md#delete_gcpkms_keys_trim_key) | **delete** /gcpkms/keys/trim/{key} | Delete old crypto key versions from Google Cloud KMS
[**delete_nomad_config_access**](SecretsApi.md#delete_nomad_config_access) | **delete** /nomad/config/access | 
[**delete_nomad_config_lease**](SecretsApi.md#delete_nomad_config_lease) | **delete** /nomad/config/lease | Configure the lease parameters for generated tokens
[**delete_nomad_role_name**](SecretsApi.md#delete_nomad_role_name) | **delete** /nomad/role/{name} | 
[**delete_pki_roles_name**](SecretsApi.md#delete_pki_roles_name) | **delete** /pki/roles/{name} | Manage the roles that can be created with this backend.
[**delete_pki_root**](SecretsApi.md#delete_pki_root) | **delete** /pki/root | Deletes the root CA key to allow a new one to be generated.
[**delete_rabbitmq_roles_name**](SecretsApi.md#delete_rabbitmq_roles_name) | **delete** /rabbitmq/roles/{name} | Manage the roles that can be created with this backend.
[**delete_secret_data_path**](SecretsApi.md#delete_secret_data_path) | **delete** /secret/data/{path} | Write, Read, and Delete data in the Key-Value Store.
[**delete_secret_metadata_path**](SecretsApi.md#delete_secret_metadata_path) | **delete** /secret/metadata/{path} | Configures settings for the KV store
[**delete_secretv1_path**](SecretsApi.md#delete_secretv1_path) | **delete** /secretv1/{path} | Pass-through secret storage to the storage backend, allowing you to read/write arbitrary data into secret storage.
[**delete_ssh_config_ca**](SecretsApi.md#delete_ssh_config_ca) | **delete** /ssh/config/ca | Set the SSH private key used for signing certificates.
[**delete_ssh_config_zeroaddress**](SecretsApi.md#delete_ssh_config_zeroaddress) | **delete** /ssh/config/zeroaddress | Assign zero address as default CIDR block for select roles.
[**delete_ssh_keys_key_name**](SecretsApi.md#delete_ssh_keys_key_name) | **delete** /ssh/keys/{key_name} | Register a shared private key with Vault.
[**delete_ssh_roles_role**](SecretsApi.md#delete_ssh_roles_role) | **delete** /ssh/roles/{role} | Manage the 'roles' that can be created with this backend.
[**delete_totp_keys_name**](SecretsApi.md#delete_totp_keys_name) | **delete** /totp/keys/{name} | Manage the keys that can be created with this backend.
[**delete_transit_keys_name**](SecretsApi.md#delete_transit_keys_name) | **delete** /transit/keys/{name} | Managed named encryption keys
[**get_ad_config**](SecretsApi.md#get_ad_config) | **get** /ad/config | Configure the AD server to connect to, along with password options.
[**get_ad_creds_name**](SecretsApi.md#get_ad_creds_name) | **get** /ad/creds/{name} | Retrieve a role's creds by role name.
[**get_ad_library**](SecretsApi.md#get_ad_library) | **get** /ad/library | 
[**get_ad_library_name**](SecretsApi.md#get_ad_library_name) | **get** /ad/library/{name} | Read a library set.
[**get_ad_library_name_status**](SecretsApi.md#get_ad_library_name_status) | **get** /ad/library/{name}/status | Check the status of the service accounts in a library set.
[**get_ad_roles**](SecretsApi.md#get_ad_roles) | **get** /ad/roles | List the name of each role currently stored.
[**get_ad_roles_name**](SecretsApi.md#get_ad_roles_name) | **get** /ad/roles/{name} | Manage roles to build links between Vault and Active Directory service accounts.
[**get_ad_rotate_root**](SecretsApi.md#get_ad_rotate_root) | **get** /ad/rotate-root | 
[**get_alicloud_config**](SecretsApi.md#get_alicloud_config) | **get** /alicloud/config | Configure the access key and secret to use for RAM and STS calls.
[**get_alicloud_creds_name**](SecretsApi.md#get_alicloud_creds_name) | **get** /alicloud/creds/{name} | Generate an API key or STS credential using the given role's configuration.'
[**get_alicloud_role**](SecretsApi.md#get_alicloud_role) | **get** /alicloud/role | List the existing roles in this backend.
[**get_alicloud_role_name**](SecretsApi.md#get_alicloud_role_name) | **get** /alicloud/role/{name} | Read, write and reference policies and roles that API keys or STS credentials can be made for.
[**get_aws_config_lease**](SecretsApi.md#get_aws_config_lease) | **get** /aws/config/lease | Configure the default lease information for generated credentials.
[**get_aws_config_root**](SecretsApi.md#get_aws_config_root) | **get** /aws/config/root | Configure the root credentials that are used to manage IAM.
[**get_aws_creds**](SecretsApi.md#get_aws_creds) | **get** /aws/creds | Generate AWS credentials from a specific Vault role.
[**get_aws_roles**](SecretsApi.md#get_aws_roles) | **get** /aws/roles | List the existing roles in this backend
[**get_aws_roles_name**](SecretsApi.md#get_aws_roles_name) | **get** /aws/roles/{name} | Read, write and reference IAM policies that access keys can be made for.
[**get_aws_sts_name**](SecretsApi.md#get_aws_sts_name) | **get** /aws/sts/{name} | Generate AWS credentials from a specific Vault role.
[**get_azure_config**](SecretsApi.md#get_azure_config) | **get** /azure/config | Configure the Azure Secret backend.
[**get_azure_creds_role**](SecretsApi.md#get_azure_creds_role) | **get** /azure/creds/{role} | Request Service Principal credentials for a given Vault role.
[**get_azure_roles**](SecretsApi.md#get_azure_roles) | **get** /azure/roles | List existing roles.
[**get_azure_roles_name**](SecretsApi.md#get_azure_roles_name) | **get** /azure/roles/{name} | Manage the Vault roles used to generate Azure credentials.
[**get_consul_config_access**](SecretsApi.md#get_consul_config_access) | **get** /consul/config/access | 
[**get_consul_creds_role**](SecretsApi.md#get_consul_creds_role) | **get** /consul/creds/{role} | 
[**get_consul_roles**](SecretsApi.md#get_consul_roles) | **get** /consul/roles | 
[**get_consul_roles_name**](SecretsApi.md#get_consul_roles_name) | **get** /consul/roles/{name} | 
[**get_cubbyhole_path**](SecretsApi.md#get_cubbyhole_path) | **get** /cubbyhole/{path} | Retrieve the secret at the specified location.
[**get_database_config**](SecretsApi.md#get_database_config) | **get** /database/config | Configure connection details to a database plugin.
[**get_database_config_name**](SecretsApi.md#get_database_config_name) | **get** /database/config/{name} | Configure connection details to a database plugin.
[**get_database_creds_name**](SecretsApi.md#get_database_creds_name) | **get** /database/creds/{name} | Request database credentials for a certain role.
[**get_database_roles**](SecretsApi.md#get_database_roles) | **get** /database/roles | Manage the roles that can be created with this backend.
[**get_database_roles_name**](SecretsApi.md#get_database_roles_name) | **get** /database/roles/{name} | Manage the roles that can be created with this backend.
[**get_database_static_creds_name**](SecretsApi.md#get_database_static_creds_name) | **get** /database/static-creds/{name} | Request database credentials for a certain static role. These credentials are rotated periodically.
[**get_database_static_roles**](SecretsApi.md#get_database_static_roles) | **get** /database/static-roles | Manage the static roles that can be created with this backend.
[**get_database_static_roles_name**](SecretsApi.md#get_database_static_roles_name) | **get** /database/static-roles/{name} | Manage the static roles that can be created with this backend.
[**get_gcp_config**](SecretsApi.md#get_gcp_config) | **get** /gcp/config | 
[**get_gcp_key_roleset**](SecretsApi.md#get_gcp_key_roleset) | **get** /gcp/key/{roleset} | 
[**get_gcp_roleset_name**](SecretsApi.md#get_gcp_roleset_name) | **get** /gcp/roleset/{name} | 
[**get_gcp_rolesets**](SecretsApi.md#get_gcp_rolesets) | **get** /gcp/rolesets | 
[**get_gcp_token_roleset**](SecretsApi.md#get_gcp_token_roleset) | **get** /gcp/token/{roleset} | 
[**get_gcpkms_config**](SecretsApi.md#get_gcpkms_config) | **get** /gcpkms/config | Configure the GCP KMS secrets engine
[**get_gcpkms_keys**](SecretsApi.md#get_gcpkms_keys) | **get** /gcpkms/keys | List named keys
[**get_gcpkms_keys_config_key**](SecretsApi.md#get_gcpkms_keys_config_key) | **get** /gcpkms/keys/config/{key} | Configure the key in Vault
[**get_gcpkms_keys_key**](SecretsApi.md#get_gcpkms_keys_key) | **get** /gcpkms/keys/{key} | Interact with crypto keys in Vault and Google Cloud KMS
[**get_gcpkms_pubkey_key**](SecretsApi.md#get_gcpkms_pubkey_key) | **get** /gcpkms/pubkey/{key} | Retrieve the public key associated with the named key
[**get_nomad_config_access**](SecretsApi.md#get_nomad_config_access) | **get** /nomad/config/access | 
[**get_nomad_config_lease**](SecretsApi.md#get_nomad_config_lease) | **get** /nomad/config/lease | Configure the lease parameters for generated tokens
[**get_nomad_creds_name**](SecretsApi.md#get_nomad_creds_name) | **get** /nomad/creds/{name} | 
[**get_nomad_role**](SecretsApi.md#get_nomad_role) | **get** /nomad/role | 
[**get_nomad_role_name**](SecretsApi.md#get_nomad_role_name) | **get** /nomad/role/{name} | 
[**get_pki_ca**](SecretsApi.md#get_pki_ca) | **get** /pki/ca | Fetch a CA, CRL, CA Chain, or non-revoked certificate.
[**get_pki_ca_chain**](SecretsApi.md#get_pki_ca_chain) | **get** /pki/ca_chain | Fetch a CA, CRL, CA Chain, or non-revoked certificate.
[**get_pki_ca_pem**](SecretsApi.md#get_pki_ca_pem) | **get** /pki/ca/pem | Fetch a CA, CRL, CA Chain, or non-revoked certificate.
[**get_pki_cert_ca_chain**](SecretsApi.md#get_pki_cert_ca_chain) | **get** /pki/cert/ca_chain | Fetch a CA, CRL, CA Chain, or non-revoked certificate.
[**get_pki_cert_crl**](SecretsApi.md#get_pki_cert_crl) | **get** /pki/cert/crl | Fetch a CA, CRL, CA Chain, or non-revoked certificate.
[**get_pki_cert_serial**](SecretsApi.md#get_pki_cert_serial) | **get** /pki/cert/{serial} | Fetch a CA, CRL, CA Chain, or non-revoked certificate.
[**get_pki_certs**](SecretsApi.md#get_pki_certs) | **get** /pki/certs | Fetch a CA, CRL, CA Chain, or non-revoked certificate.
[**get_pki_config_crl**](SecretsApi.md#get_pki_config_crl) | **get** /pki/config/crl | Configure the CRL expiration.
[**get_pki_config_urls**](SecretsApi.md#get_pki_config_urls) | **get** /pki/config/urls | Set the URLs for the issuing CA, CRL distribution points, and OCSP servers.
[**get_pki_crl**](SecretsApi.md#get_pki_crl) | **get** /pki/crl | Fetch a CA, CRL, CA Chain, or non-revoked certificate.
[**get_pki_crl_pem**](SecretsApi.md#get_pki_crl_pem) | **get** /pki/crl/pem | Fetch a CA, CRL, CA Chain, or non-revoked certificate.
[**get_pki_crl_rotate**](SecretsApi.md#get_pki_crl_rotate) | **get** /pki/crl/rotate | Force a rebuild of the CRL.
[**get_pki_roles**](SecretsApi.md#get_pki_roles) | **get** /pki/roles | List the existing roles in this backend
[**get_pki_roles_name**](SecretsApi.md#get_pki_roles_name) | **get** /pki/roles/{name} | Manage the roles that can be created with this backend.
[**get_rabbitmq_config_lease**](SecretsApi.md#get_rabbitmq_config_lease) | **get** /rabbitmq/config/lease | Configure the lease parameters for generated credentials
[**get_rabbitmq_creds_name**](SecretsApi.md#get_rabbitmq_creds_name) | **get** /rabbitmq/creds/{name} | Request RabbitMQ credentials for a certain role.
[**get_rabbitmq_roles**](SecretsApi.md#get_rabbitmq_roles) | **get** /rabbitmq/roles | Manage the roles that can be created with this backend.
[**get_rabbitmq_roles_name**](SecretsApi.md#get_rabbitmq_roles_name) | **get** /rabbitmq/roles/{name} | Manage the roles that can be created with this backend.
[**get_secret_config**](SecretsApi.md#get_secret_config) | **get** /secret/config | Read the backend level settings.
[**get_secret_data_path**](SecretsApi.md#get_secret_data_path) | **get** /secret/data/{path} | Write, Read, and Delete data in the Key-Value Store.
[**get_secret_metadata_path**](SecretsApi.md#get_secret_metadata_path) | **get** /secret/metadata/{path} | Configures settings for the KV store
[**get_secretv1_path**](SecretsApi.md#get_secretv1_path) | **get** /secretv1/{path} | Pass-through secret storage to the storage backend, allowing you to read/write arbitrary data into secret storage.
[**get_ssh_config_ca**](SecretsApi.md#get_ssh_config_ca) | **get** /ssh/config/ca | Set the SSH private key used for signing certificates.
[**get_ssh_config_zeroaddress**](SecretsApi.md#get_ssh_config_zeroaddress) | **get** /ssh/config/zeroaddress | Assign zero address as default CIDR block for select roles.
[**get_ssh_public_key**](SecretsApi.md#get_ssh_public_key) | **get** /ssh/public_key | Retrieve the public key.
[**get_ssh_roles**](SecretsApi.md#get_ssh_roles) | **get** /ssh/roles | Manage the 'roles' that can be created with this backend.
[**get_ssh_roles_role**](SecretsApi.md#get_ssh_roles_role) | **get** /ssh/roles/{role} | Manage the 'roles' that can be created with this backend.
[**get_totp_code_name**](SecretsApi.md#get_totp_code_name) | **get** /totp/code/{name} | Request time-based one-time use password or validate a password for a certain key .
[**get_totp_keys**](SecretsApi.md#get_totp_keys) | **get** /totp/keys | Manage the keys that can be created with this backend.
[**get_totp_keys_name**](SecretsApi.md#get_totp_keys_name) | **get** /totp/keys/{name} | Manage the keys that can be created with this backend.
[**get_transit_backup_name**](SecretsApi.md#get_transit_backup_name) | **get** /transit/backup/{name} | Backup the named key
[**get_transit_cache_config**](SecretsApi.md#get_transit_cache_config) | **get** /transit/cache-config | Returns the size of the active cache
[**get_transit_export_type_name**](SecretsApi.md#get_transit_export_type_name) | **get** /transit/export/{type}/{name} | Export named encryption or signing key
[**get_transit_export_type_name_version**](SecretsApi.md#get_transit_export_type_name_version) | **get** /transit/export/{type}/{name}/{version} | Export named encryption or signing key
[**get_transit_keys**](SecretsApi.md#get_transit_keys) | **get** /transit/keys | Managed named encryption keys
[**get_transit_keys_name**](SecretsApi.md#get_transit_keys_name) | **get** /transit/keys/{name} | Managed named encryption keys
[**post_ad_config**](SecretsApi.md#post_ad_config) | **post** /ad/config | Configure the AD server to connect to, along with password options.
[**post_ad_library_manage_name_check_in**](SecretsApi.md#post_ad_library_manage_name_check_in) | **post** /ad/library/manage/{name}/check-in | Check service accounts in to the library.
[**post_ad_library_name**](SecretsApi.md#post_ad_library_name) | **post** /ad/library/{name} | Update a library set.
[**post_ad_library_name_check_in**](SecretsApi.md#post_ad_library_name_check_in) | **post** /ad/library/{name}/check-in | Check service accounts in to the library.
[**post_ad_library_name_check_out**](SecretsApi.md#post_ad_library_name_check_out) | **post** /ad/library/{name}/check-out | Check a service account out from the library.
[**post_ad_roles_name**](SecretsApi.md#post_ad_roles_name) | **post** /ad/roles/{name} | Manage roles to build links between Vault and Active Directory service accounts.
[**post_ad_rotate_root**](SecretsApi.md#post_ad_rotate_root) | **post** /ad/rotate-root | 
[**post_alicloud_config**](SecretsApi.md#post_alicloud_config) | **post** /alicloud/config | Configure the access key and secret to use for RAM and STS calls.
[**post_alicloud_role_name**](SecretsApi.md#post_alicloud_role_name) | **post** /alicloud/role/{name} | Read, write and reference policies and roles that API keys or STS credentials can be made for.
[**post_aws_config_lease**](SecretsApi.md#post_aws_config_lease) | **post** /aws/config/lease | Configure the default lease information for generated credentials.
[**post_aws_config_root**](SecretsApi.md#post_aws_config_root) | **post** /aws/config/root | Configure the root credentials that are used to manage IAM.
[**post_aws_config_rotate_root**](SecretsApi.md#post_aws_config_rotate_root) | **post** /aws/config/rotate-root | 
[**post_aws_creds**](SecretsApi.md#post_aws_creds) | **post** /aws/creds | Generate AWS credentials from a specific Vault role.
[**post_aws_roles_name**](SecretsApi.md#post_aws_roles_name) | **post** /aws/roles/{name} | Read, write and reference IAM policies that access keys can be made for.
[**post_aws_sts_name**](SecretsApi.md#post_aws_sts_name) | **post** /aws/sts/{name} | Generate AWS credentials from a specific Vault role.
[**post_azure_config**](SecretsApi.md#post_azure_config) | **post** /azure/config | Configure the Azure Secret backend.
[**post_azure_roles_name**](SecretsApi.md#post_azure_roles_name) | **post** /azure/roles/{name} | Manage the Vault roles used to generate Azure credentials.
[**post_consul_config_access**](SecretsApi.md#post_consul_config_access) | **post** /consul/config/access | 
[**post_consul_roles_name**](SecretsApi.md#post_consul_roles_name) | **post** /consul/roles/{name} | 
[**post_cubbyhole_path**](SecretsApi.md#post_cubbyhole_path) | **post** /cubbyhole/{path} | Store a secret at the specified location.
[**post_database_config_name**](SecretsApi.md#post_database_config_name) | **post** /database/config/{name} | Configure connection details to a database plugin.
[**post_database_reset_name**](SecretsApi.md#post_database_reset_name) | **post** /database/reset/{name} | Resets a database plugin.
[**post_database_roles_name**](SecretsApi.md#post_database_roles_name) | **post** /database/roles/{name} | Manage the roles that can be created with this backend.
[**post_database_rotate_role_name**](SecretsApi.md#post_database_rotate_role_name) | **post** /database/rotate-role/{name} | 
[**post_database_rotate_root_name**](SecretsApi.md#post_database_rotate_root_name) | **post** /database/rotate-root/{name} | 
[**post_database_static_roles_name**](SecretsApi.md#post_database_static_roles_name) | **post** /database/static-roles/{name} | Manage the static roles that can be created with this backend.
[**post_gcp_config**](SecretsApi.md#post_gcp_config) | **post** /gcp/config | 
[**post_gcp_config_rotate_root**](SecretsApi.md#post_gcp_config_rotate_root) | **post** /gcp/config/rotate-root | 
[**post_gcp_key_roleset**](SecretsApi.md#post_gcp_key_roleset) | **post** /gcp/key/{roleset} | 
[**post_gcp_roleset_name**](SecretsApi.md#post_gcp_roleset_name) | **post** /gcp/roleset/{name} | 
[**post_gcp_roleset_name_rotate**](SecretsApi.md#post_gcp_roleset_name_rotate) | **post** /gcp/roleset/{name}/rotate | 
[**post_gcp_roleset_name_rotate_key**](SecretsApi.md#post_gcp_roleset_name_rotate_key) | **post** /gcp/roleset/{name}/rotate-key | 
[**post_gcp_token_roleset**](SecretsApi.md#post_gcp_token_roleset) | **post** /gcp/token/{roleset} | 
[**post_gcpkms_config**](SecretsApi.md#post_gcpkms_config) | **post** /gcpkms/config | Configure the GCP KMS secrets engine
[**post_gcpkms_decrypt_key**](SecretsApi.md#post_gcpkms_decrypt_key) | **post** /gcpkms/decrypt/{key} | Decrypt a ciphertext value using a named key
[**post_gcpkms_encrypt_key**](SecretsApi.md#post_gcpkms_encrypt_key) | **post** /gcpkms/encrypt/{key} | Encrypt a plaintext value using a named key
[**post_gcpkms_keys_config_key**](SecretsApi.md#post_gcpkms_keys_config_key) | **post** /gcpkms/keys/config/{key} | Configure the key in Vault
[**post_gcpkms_keys_deregister_key**](SecretsApi.md#post_gcpkms_keys_deregister_key) | **post** /gcpkms/keys/deregister/{key} | Deregister an existing key in Vault
[**post_gcpkms_keys_key**](SecretsApi.md#post_gcpkms_keys_key) | **post** /gcpkms/keys/{key} | Interact with crypto keys in Vault and Google Cloud KMS
[**post_gcpkms_keys_register_key**](SecretsApi.md#post_gcpkms_keys_register_key) | **post** /gcpkms/keys/register/{key} | Register an existing crypto key in Google Cloud KMS
[**post_gcpkms_keys_rotate_key**](SecretsApi.md#post_gcpkms_keys_rotate_key) | **post** /gcpkms/keys/rotate/{key} | Rotate a crypto key to a new primary version
[**post_gcpkms_keys_trim_key**](SecretsApi.md#post_gcpkms_keys_trim_key) | **post** /gcpkms/keys/trim/{key} | Delete old crypto key versions from Google Cloud KMS
[**post_gcpkms_reencrypt_key**](SecretsApi.md#post_gcpkms_reencrypt_key) | **post** /gcpkms/reencrypt/{key} | Re-encrypt existing ciphertext data to a new version
[**post_gcpkms_sign_key**](SecretsApi.md#post_gcpkms_sign_key) | **post** /gcpkms/sign/{key} | Signs a message or digest using a named key
[**post_gcpkms_verify_key**](SecretsApi.md#post_gcpkms_verify_key) | **post** /gcpkms/verify/{key} | Verify a signature using a named key
[**post_nomad_config_access**](SecretsApi.md#post_nomad_config_access) | **post** /nomad/config/access | 
[**post_nomad_config_lease**](SecretsApi.md#post_nomad_config_lease) | **post** /nomad/config/lease | Configure the lease parameters for generated tokens
[**post_nomad_role_name**](SecretsApi.md#post_nomad_role_name) | **post** /nomad/role/{name} | 
[**post_pki_config_ca**](SecretsApi.md#post_pki_config_ca) | **post** /pki/config/ca | Set the CA certificate and private key used for generated credentials.
[**post_pki_config_crl**](SecretsApi.md#post_pki_config_crl) | **post** /pki/config/crl | Configure the CRL expiration.
[**post_pki_config_urls**](SecretsApi.md#post_pki_config_urls) | **post** /pki/config/urls | Set the URLs for the issuing CA, CRL distribution points, and OCSP servers.
[**post_pki_intermediate_generate_exported**](SecretsApi.md#post_pki_intermediate_generate_exported) | **post** /pki/intermediate/generate/{exported} | Generate a new CSR and private key used for signing.
[**post_pki_intermediate_set_signed**](SecretsApi.md#post_pki_intermediate_set_signed) | **post** /pki/intermediate/set-signed | Provide the signed intermediate CA cert.
[**post_pki_issue_role**](SecretsApi.md#post_pki_issue_role) | **post** /pki/issue/{role} | Request a certificate using a certain role with the provided details.
[**post_pki_revoke**](SecretsApi.md#post_pki_revoke) | **post** /pki/revoke | Revoke a certificate by serial number.
[**post_pki_roles_name**](SecretsApi.md#post_pki_roles_name) | **post** /pki/roles/{name} | Manage the roles that can be created with this backend.
[**post_pki_root_generate_exported**](SecretsApi.md#post_pki_root_generate_exported) | **post** /pki/root/generate/{exported} | Generate a new CA certificate and private key used for signing.
[**post_pki_root_sign_intermediate**](SecretsApi.md#post_pki_root_sign_intermediate) | **post** /pki/root/sign-intermediate | Issue an intermediate CA certificate based on the provided CSR.
[**post_pki_root_sign_self_issued**](SecretsApi.md#post_pki_root_sign_self_issued) | **post** /pki/root/sign-self-issued | Signs another CA's self-issued certificate.
[**post_pki_sign_role**](SecretsApi.md#post_pki_sign_role) | **post** /pki/sign/{role} | Request certificates using a certain role with the provided details.
[**post_pki_sign_verbatim**](SecretsApi.md#post_pki_sign_verbatim) | **post** /pki/sign-verbatim | Request certificates using a certain role with the provided details.
[**post_pki_sign_verbatim_role**](SecretsApi.md#post_pki_sign_verbatim_role) | **post** /pki/sign-verbatim/{role} | Request certificates using a certain role with the provided details.
[**post_pki_tidy**](SecretsApi.md#post_pki_tidy) | **post** /pki/tidy | Tidy up the backend by removing expired certificates, revocation information, or both.
[**post_rabbitmq_config_connection**](SecretsApi.md#post_rabbitmq_config_connection) | **post** /rabbitmq/config/connection | Configure the connection URI, username, and password to talk to RabbitMQ management HTTP API.
[**post_rabbitmq_config_lease**](SecretsApi.md#post_rabbitmq_config_lease) | **post** /rabbitmq/config/lease | Configure the lease parameters for generated credentials
[**post_rabbitmq_roles_name**](SecretsApi.md#post_rabbitmq_roles_name) | **post** /rabbitmq/roles/{name} | Manage the roles that can be created with this backend.
[**post_secret_config**](SecretsApi.md#post_secret_config) | **post** /secret/config | Configure backend level settings that are applied to every key in the key-value store.
[**post_secret_data_path**](SecretsApi.md#post_secret_data_path) | **post** /secret/data/{path} | Write, Read, and Delete data in the Key-Value Store.
[**post_secret_delete_path**](SecretsApi.md#post_secret_delete_path) | **post** /secret/delete/{path} | Marks one or more versions as deleted in the KV store.
[**post_secret_destroy_path**](SecretsApi.md#post_secret_destroy_path) | **post** /secret/destroy/{path} | Permanently removes one or more versions in the KV store
[**post_secret_metadata_path**](SecretsApi.md#post_secret_metadata_path) | **post** /secret/metadata/{path} | Configures settings for the KV store
[**post_secret_undelete_path**](SecretsApi.md#post_secret_undelete_path) | **post** /secret/undelete/{path} | Undeletes one or more versions from the KV store.
[**post_secretv1_path**](SecretsApi.md#post_secretv1_path) | **post** /secretv1/{path} | Pass-through secret storage to the storage backend, allowing you to read/write arbitrary data into secret storage.
[**post_ssh_config_ca**](SecretsApi.md#post_ssh_config_ca) | **post** /ssh/config/ca | Set the SSH private key used for signing certificates.
[**post_ssh_config_zeroaddress**](SecretsApi.md#post_ssh_config_zeroaddress) | **post** /ssh/config/zeroaddress | Assign zero address as default CIDR block for select roles.
[**post_ssh_creds_role**](SecretsApi.md#post_ssh_creds_role) | **post** /ssh/creds/{role} | Creates a credential for establishing SSH connection with the remote host.
[**post_ssh_keys_key_name**](SecretsApi.md#post_ssh_keys_key_name) | **post** /ssh/keys/{key_name} | Register a shared private key with Vault.
[**post_ssh_lookup**](SecretsApi.md#post_ssh_lookup) | **post** /ssh/lookup | List all the roles associated with the given IP address.
[**post_ssh_roles_role**](SecretsApi.md#post_ssh_roles_role) | **post** /ssh/roles/{role} | Manage the 'roles' that can be created with this backend.
[**post_ssh_sign_role**](SecretsApi.md#post_ssh_sign_role) | **post** /ssh/sign/{role} | Request signing an SSH key using a certain role with the provided details.
[**post_ssh_verify**](SecretsApi.md#post_ssh_verify) | **post** /ssh/verify | Validate the OTP provided by Vault SSH Agent.
[**post_totp_code_name**](SecretsApi.md#post_totp_code_name) | **post** /totp/code/{name} | Request time-based one-time use password or validate a password for a certain key .
[**post_totp_keys_name**](SecretsApi.md#post_totp_keys_name) | **post** /totp/keys/{name} | Manage the keys that can be created with this backend.
[**post_transit_cache_config**](SecretsApi.md#post_transit_cache_config) | **post** /transit/cache-config | Configures a new cache of the specified size
[**post_transit_datakey_plaintext_name**](SecretsApi.md#post_transit_datakey_plaintext_name) | **post** /transit/datakey/{plaintext}/{name} | Generate a data key
[**post_transit_decrypt_name**](SecretsApi.md#post_transit_decrypt_name) | **post** /transit/decrypt/{name} | Decrypt a ciphertext value using a named key
[**post_transit_encrypt_name**](SecretsApi.md#post_transit_encrypt_name) | **post** /transit/encrypt/{name} | Encrypt a plaintext value or a batch of plaintext blocks using a named key
[**post_transit_hash**](SecretsApi.md#post_transit_hash) | **post** /transit/hash | Generate a hash sum for input data
[**post_transit_hash_urlalgorithm**](SecretsApi.md#post_transit_hash_urlalgorithm) | **post** /transit/hash/{urlalgorithm} | Generate a hash sum for input data
[**post_transit_hmac_name**](SecretsApi.md#post_transit_hmac_name) | **post** /transit/hmac/{name} | Generate an HMAC for input data using the named key
[**post_transit_hmac_name_urlalgorithm**](SecretsApi.md#post_transit_hmac_name_urlalgorithm) | **post** /transit/hmac/{name}/{urlalgorithm} | Generate an HMAC for input data using the named key
[**post_transit_keys_name**](SecretsApi.md#post_transit_keys_name) | **post** /transit/keys/{name} | Managed named encryption keys
[**post_transit_keys_name_config**](SecretsApi.md#post_transit_keys_name_config) | **post** /transit/keys/{name}/config | Configure a named encryption key
[**post_transit_keys_name_rotate**](SecretsApi.md#post_transit_keys_name_rotate) | **post** /transit/keys/{name}/rotate | Rotate named encryption key
[**post_transit_keys_name_trim**](SecretsApi.md#post_transit_keys_name_trim) | **post** /transit/keys/{name}/trim | Trim key versions of a named key
[**post_transit_random**](SecretsApi.md#post_transit_random) | **post** /transit/random | Generate random bytes
[**post_transit_random_urlbytes**](SecretsApi.md#post_transit_random_urlbytes) | **post** /transit/random/{urlbytes} | Generate random bytes
[**post_transit_restore**](SecretsApi.md#post_transit_restore) | **post** /transit/restore | Restore the named key
[**post_transit_restore_name**](SecretsApi.md#post_transit_restore_name) | **post** /transit/restore/{name} | Restore the named key
[**post_transit_rewrap_name**](SecretsApi.md#post_transit_rewrap_name) | **post** /transit/rewrap/{name} | Rewrap ciphertext
[**post_transit_sign_name**](SecretsApi.md#post_transit_sign_name) | **post** /transit/sign/{name} | Generate a signature for input data using the named key
[**post_transit_sign_name_urlalgorithm**](SecretsApi.md#post_transit_sign_name_urlalgorithm) | **post** /transit/sign/{name}/{urlalgorithm} | Generate a signature for input data using the named key
[**post_transit_verify_name**](SecretsApi.md#post_transit_verify_name) | **post** /transit/verify/{name} | Verify a signature or HMAC for input data created using the named key
[**post_transit_verify_name_urlalgorithm**](SecretsApi.md#post_transit_verify_name_urlalgorithm) | **post** /transit/verify/{name}/{urlalgorithm} | Verify a signature or HMAC for input data created using the named key



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


## delete_ad_library_name

> delete_ad_library_name(name)
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


## delete_ad_roles_name

> delete_ad_roles_name(name)
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


## delete_alicloud_role_name

> delete_alicloud_role_name(name)
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


## delete_aws_roles_name

> delete_aws_roles_name(name)
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


## delete_azure_roles_name

> delete_azure_roles_name(name)
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


## delete_consul_roles_name

> delete_consul_roles_name(name)


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


## delete_cubbyhole_path

> delete_cubbyhole_path(path)
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


## delete_database_config_name

> delete_database_config_name(name)
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


## delete_database_roles_name

> delete_database_roles_name(name)
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


## delete_database_static_roles_name

> delete_database_static_roles_name(name)
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


## delete_gcp_roleset_name

> delete_gcp_roleset_name(name)


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


## delete_gcpkms_keys_deregister_key

> delete_gcpkms_keys_deregister_key(key)
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


## delete_gcpkms_keys_key

> delete_gcpkms_keys_key(key)
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


## delete_gcpkms_keys_trim_key

> delete_gcpkms_keys_trim_key(key)
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


## delete_nomad_role_name

> delete_nomad_role_name(name)


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


## delete_pki_roles_name

> delete_pki_roles_name(name)
Manage the roles that can be created with this backend.

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


## delete_pki_root

> delete_pki_root()
Deletes the root CA key to allow a new one to be generated.

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


## delete_rabbitmq_roles_name

> delete_rabbitmq_roles_name(name)
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


## delete_secret_data_path

> delete_secret_data_path(path)
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


## delete_secret_metadata_path

> delete_secret_metadata_path(path)
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


## delete_secretv1_path

> delete_secretv1_path(path)
Pass-through secret storage to the storage backend, allowing you to read/write arbitrary data into secret storage.

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


## delete_ssh_keys_key_name

> delete_ssh_keys_key_name(key_name)
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


## delete_ssh_roles_role

> delete_ssh_roles_role(role)
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


## delete_totp_keys_name

> delete_totp_keys_name(name)
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


## delete_transit_keys_name

> delete_transit_keys_name(name)
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

> get_ad_config()
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


## get_ad_creds_name

> get_ad_creds_name(name)
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


## get_ad_library

> get_ad_library(list)


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


## get_ad_library_name

> get_ad_library_name(name)
Read a library set.

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


## get_ad_library_name_status

> get_ad_library_name_status(name)
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


## get_ad_roles_name

> get_ad_roles_name(name)
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

> get_alicloud_config()
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


## get_alicloud_creds_name

> get_alicloud_creds_name(name)
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

> get_alicloud_role(list)
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


## get_alicloud_role_name

> get_alicloud_role_name(name)
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


## get_aws_config_lease

> get_aws_config_lease()
Configure the default lease information for generated credentials.

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


## get_aws_config_root

> get_aws_config_root()
Configure the root credentials that are used to manage IAM.

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


## get_aws_creds

> get_aws_creds()
Generate AWS credentials from a specific Vault role.

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


## get_aws_roles_name

> get_aws_roles_name(name)
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


## get_aws_sts_name

> get_aws_sts_name(name)
Generate AWS credentials from a specific Vault role.

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


## get_azure_config

> get_azure_config()
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


## get_azure_creds_role

> get_azure_creds_role(role)
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


## get_azure_roles_name

> get_azure_roles_name(name)
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


## get_consul_config_access

> get_consul_config_access()


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


## get_consul_creds_role

> get_consul_creds_role(role)


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


## get_consul_roles_name

> get_consul_roles_name(name)


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


## get_cubbyhole_path

> get_cubbyhole_path(path, list)
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

> get_database_config(list)
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


## get_database_config_name

> get_database_config_name(name)
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


## get_database_creds_name

> get_database_creds_name(name)
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


## get_database_roles_name

> get_database_roles_name(name)
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


## get_database_static_creds_name

> get_database_static_creds_name(name)
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


## get_database_static_roles_name

> get_database_static_roles_name(name)
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


## get_gcp_config

> get_gcp_config()


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


## get_gcp_key_roleset

> get_gcp_key_roleset(roleset)


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


## get_gcp_roleset_name

> get_gcp_roleset_name(name)


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


## get_gcp_token_roleset

> get_gcp_token_roleset(roleset)


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

> get_gcpkms_config()
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


## get_gcpkms_keys_config_key

> get_gcpkms_keys_config_key(key)
Configure the key in Vault

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


## get_gcpkms_keys_key

> get_gcpkms_keys_key(key)
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


## get_gcpkms_pubkey_key

> get_gcpkms_pubkey_key(key)
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


## get_nomad_config_access

> get_nomad_config_access()


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


## get_nomad_config_lease

> get_nomad_config_lease()
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


## get_nomad_creds_name

> get_nomad_creds_name(name)


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

> get_nomad_role(list)


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


## get_nomad_role_name

> get_nomad_role_name(name)


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


## get_pki_ca

> get_pki_ca()
Fetch a CA, CRL, CA Chain, or non-revoked certificate.

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


## get_pki_ca_chain

> get_pki_ca_chain()
Fetch a CA, CRL, CA Chain, or non-revoked certificate.

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


## get_pki_ca_pem

> get_pki_ca_pem()
Fetch a CA, CRL, CA Chain, or non-revoked certificate.

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


## get_pki_cert_ca_chain

> get_pki_cert_ca_chain()
Fetch a CA, CRL, CA Chain, or non-revoked certificate.

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


## get_pki_cert_crl

> get_pki_cert_crl()
Fetch a CA, CRL, CA Chain, or non-revoked certificate.

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


## get_pki_cert_serial

> get_pki_cert_serial(serial)
Fetch a CA, CRL, CA Chain, or non-revoked certificate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**serial** | **String** | Certificate serial number, in colon- or hyphen-separated octal | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_pki_certs

> get_pki_certs(list)
Fetch a CA, CRL, CA Chain, or non-revoked certificate.

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


## get_pki_config_crl

> get_pki_config_crl()
Configure the CRL expiration.

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


## get_pki_config_urls

> get_pki_config_urls()
Set the URLs for the issuing CA, CRL distribution points, and OCSP servers.

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


## get_pki_crl

> get_pki_crl()
Fetch a CA, CRL, CA Chain, or non-revoked certificate.

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


## get_pki_crl_pem

> get_pki_crl_pem()
Fetch a CA, CRL, CA Chain, or non-revoked certificate.

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


## get_pki_crl_rotate

> get_pki_crl_rotate()
Force a rebuild of the CRL.

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


## get_pki_roles

> get_pki_roles(list)
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


## get_pki_roles_name

> get_pki_roles_name(name)
Manage the roles that can be created with this backend.

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


## get_rabbitmq_config_lease

> get_rabbitmq_config_lease()
Configure the lease parameters for generated credentials

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


## get_rabbitmq_creds_name

> get_rabbitmq_creds_name(name)
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


## get_rabbitmq_roles_name

> get_rabbitmq_roles_name(name)
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


## get_secret_config

> get_secret_config()
Read the backend level settings.

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


## get_secret_data_path

> get_secret_data_path(path)
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


## get_secret_metadata_path

> get_secret_metadata_path(path, list)
Configures settings for the KV store

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_secretv1_path

> get_secretv1_path(path, list)
Pass-through secret storage to the storage backend, allowing you to read/write arbitrary data into secret storage.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_ssh_config_ca

> get_ssh_config_ca()
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


## get_ssh_config_zeroaddress

> get_ssh_config_zeroaddress()
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


## get_ssh_roles_role

> get_ssh_roles_role(role)
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


## get_totp_code_name

> get_totp_code_name(name)
Request time-based one-time use password or validate a password for a certain key .

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


## get_totp_keys_name

> get_totp_keys_name(name)
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


## get_transit_backup_name

> get_transit_backup_name(name)
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

> get_transit_cache_config()
Returns the size of the active cache

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


## get_transit_export_type_name

> get_transit_export_type_name(name, _type)
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


## get_transit_export_type_name_version

> get_transit_export_type_name_version(name, _type, version)
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


## get_transit_keys_name

> get_transit_keys_name(name)
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


## post_ad_config

> post_ad_config(inline_object)
Configure the AD server to connect to, along with password options.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object** | Option<[**InlineObject**](InlineObject.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_library_manage_name_check_in

> post_ad_library_manage_name_check_in(name, inline_object1)
Check service accounts in to the library.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set. | [required] |
**inline_object1** | Option<[**InlineObject1**](InlineObject1.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_library_name

> post_ad_library_name(name, inline_object2)
Update a library set.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set. | [required] |
**inline_object2** | Option<[**InlineObject2**](InlineObject2.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_library_name_check_in

> post_ad_library_name_check_in(name, inline_object3)
Check service accounts in to the library.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set. | [required] |
**inline_object3** | Option<[**InlineObject3**](InlineObject3.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_library_name_check_out

> post_ad_library_name_check_out(name, inline_object4)
Check a service account out from the library.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the set | [required] |
**inline_object4** | Option<[**InlineObject4**](InlineObject4.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ad_roles_name

> post_ad_roles_name(name, inline_object5)
Manage roles to build links between Vault and Active Directory service accounts.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**inline_object5** | Option<[**InlineObject5**](InlineObject5.md)> |  |  |

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

> post_alicloud_config(inline_object6)
Configure the access key and secret to use for RAM and STS calls.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object6** | Option<[**InlineObject6**](InlineObject6.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_alicloud_role_name

> post_alicloud_role_name(name, inline_object7)
Read, write and reference policies and roles that API keys or STS credentials can be made for.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the role. | [required] |
**inline_object7** | Option<[**InlineObject7**](InlineObject7.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_aws_config_lease

> post_aws_config_lease(inline_object111)
Configure the default lease information for generated credentials.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object111** | Option<[**InlineObject111**](InlineObject111.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_aws_config_root

> post_aws_config_root(inline_object112)
Configure the root credentials that are used to manage IAM.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object112** | Option<[**InlineObject112**](InlineObject112.md)> |  |  |

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

> post_aws_creds(inline_object113)
Generate AWS credentials from a specific Vault role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object113** | Option<[**InlineObject113**](InlineObject113.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_aws_roles_name

> post_aws_roles_name(name, inline_object114)
Read, write and reference IAM policies that access keys can be made for.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the policy | [required] |
**inline_object114** | Option<[**InlineObject114**](InlineObject114.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_aws_sts_name

> post_aws_sts_name(name, inline_object115)
Generate AWS credentials from a specific Vault role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**inline_object115** | Option<[**InlineObject115**](InlineObject115.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_azure_config

> post_azure_config(inline_object116)
Configure the Azure Secret backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object116** | Option<[**InlineObject116**](InlineObject116.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_azure_roles_name

> post_azure_roles_name(name, inline_object117)
Manage the Vault roles used to generate Azure credentials.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object117** | Option<[**InlineObject117**](InlineObject117.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_consul_config_access

> post_consul_config_access(inline_object118)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object118** | Option<[**InlineObject118**](InlineObject118.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_consul_roles_name

> post_consul_roles_name(name, inline_object119)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**inline_object119** | Option<[**InlineObject119**](InlineObject119.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_cubbyhole_path

> post_cubbyhole_path(path)
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


## post_database_config_name

> post_database_config_name(name, inline_object120)
Configure connection details to a database plugin.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of this database connection | [required] |
**inline_object120** | Option<[**InlineObject120**](InlineObject120.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_database_reset_name

> post_database_reset_name(name)
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


## post_database_roles_name

> post_database_roles_name(name, inline_object121)
Manage the roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object121** | Option<[**InlineObject121**](InlineObject121.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_database_rotate_role_name

> post_database_rotate_role_name(name)


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


## post_database_rotate_root_name

> post_database_rotate_root_name(name)


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


## post_database_static_roles_name

> post_database_static_roles_name(name, inline_object122)
Manage the static roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object122** | Option<[**InlineObject122**](InlineObject122.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcp_config

> post_gcp_config(inline_object123)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object123** | Option<[**InlineObject123**](InlineObject123.md)> |  |  |

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


## post_gcp_key_roleset

> post_gcp_key_roleset(roleset, inline_object124)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**roleset** | **String** | Required. Name of the role set. | [required] |
**inline_object124** | Option<[**InlineObject124**](InlineObject124.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcp_roleset_name

> post_gcp_roleset_name(name, inline_object125)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Required. Name of the role. | [required] |
**inline_object125** | Option<[**InlineObject125**](InlineObject125.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcp_roleset_name_rotate

> post_gcp_roleset_name_rotate(name)


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


## post_gcp_roleset_name_rotate_key

> post_gcp_roleset_name_rotate_key(name)


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


## post_gcp_token_roleset

> post_gcp_token_roleset(roleset)


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

> post_gcpkms_config(inline_object126)
Configure the GCP KMS secrets engine

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object126** | Option<[**InlineObject126**](InlineObject126.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_decrypt_key

> post_gcpkms_decrypt_key(key, inline_object127)
Decrypt a ciphertext value using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault to use for decryption. This key must already exist in Vault and must map back to a Google Cloud KMS key. | [required] |
**inline_object127** | Option<[**InlineObject127**](InlineObject127.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_encrypt_key

> post_gcpkms_encrypt_key(key, inline_object128)
Encrypt a plaintext value using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault to use for encryption. This key must already exist in Vault and must map back to a Google Cloud KMS key. | [required] |
**inline_object128** | Option<[**InlineObject128**](InlineObject128.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_keys_config_key

> post_gcpkms_keys_config_key(key, inline_object129)
Configure the key in Vault

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault. | [required] |
**inline_object129** | Option<[**InlineObject129**](InlineObject129.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_keys_deregister_key

> post_gcpkms_keys_deregister_key(key)
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


## post_gcpkms_keys_key

> post_gcpkms_keys_key(key, inline_object131)
Interact with crypto keys in Vault and Google Cloud KMS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault. | [required] |
**inline_object131** | Option<[**InlineObject131**](InlineObject131.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_keys_register_key

> post_gcpkms_keys_register_key(key, inline_object130)
Register an existing crypto key in Google Cloud KMS

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key to register in Vault. This will be the named used to refer to the underlying crypto key when encrypting or decrypting data. | [required] |
**inline_object130** | Option<[**InlineObject130**](InlineObject130.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_keys_rotate_key

> post_gcpkms_keys_rotate_key(key)
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


## post_gcpkms_keys_trim_key

> post_gcpkms_keys_trim_key(key)
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


## post_gcpkms_reencrypt_key

> post_gcpkms_reencrypt_key(key, inline_object132)
Re-encrypt existing ciphertext data to a new version

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key to use for encryption. This key must already exist in Vault and Google Cloud KMS. | [required] |
**inline_object132** | Option<[**InlineObject132**](InlineObject132.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_sign_key

> post_gcpkms_sign_key(key, inline_object133)
Signs a message or digest using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault to use for signing. This key must already exist in Vault and must map back to a Google Cloud KMS key. | [required] |
**inline_object133** | Option<[**InlineObject133**](InlineObject133.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_gcpkms_verify_key

> post_gcpkms_verify_key(key, inline_object134)
Verify a signature using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Name of the key in Vault to use for verification. This key must already exist in Vault and must map back to a Google Cloud KMS key. | [required] |
**inline_object134** | Option<[**InlineObject134**](InlineObject134.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_nomad_config_access

> post_nomad_config_access(inline_object158)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object158** | Option<[**InlineObject158**](InlineObject158.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_nomad_config_lease

> post_nomad_config_lease(inline_object159)
Configure the lease parameters for generated tokens

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object159** | Option<[**InlineObject159**](InlineObject159.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_nomad_role_name

> post_nomad_role_name(name, inline_object160)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**inline_object160** | Option<[**InlineObject160**](InlineObject160.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_config_ca

> post_pki_config_ca(inline_object161)
Set the CA certificate and private key used for generated credentials.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object161** | Option<[**InlineObject161**](InlineObject161.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_config_crl

> post_pki_config_crl(inline_object162)
Configure the CRL expiration.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object162** | Option<[**InlineObject162**](InlineObject162.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_config_urls

> post_pki_config_urls(inline_object163)
Set the URLs for the issuing CA, CRL distribution points, and OCSP servers.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object163** | Option<[**InlineObject163**](InlineObject163.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_intermediate_generate_exported

> post_pki_intermediate_generate_exported(exported, inline_object164)
Generate a new CSR and private key used for signing.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**exported** | **String** | Must be \"internal\" or \"exported\". If set to \"exported\", the generated private key will be returned. This is your *only* chance to retrieve the private key! | [required] |
**inline_object164** | Option<[**InlineObject164**](InlineObject164.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_intermediate_set_signed

> post_pki_intermediate_set_signed(inline_object165)
Provide the signed intermediate CA cert.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object165** | Option<[**InlineObject165**](InlineObject165.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_issue_role

> post_pki_issue_role(role, inline_object166)
Request a certificate using a certain role with the provided details.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | The desired role with configuration for this request | [required] |
**inline_object166** | Option<[**InlineObject166**](InlineObject166.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_revoke

> post_pki_revoke(inline_object167)
Revoke a certificate by serial number.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object167** | Option<[**InlineObject167**](InlineObject167.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_roles_name

> post_pki_roles_name(name, inline_object168)
Manage the roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role | [required] |
**inline_object168** | Option<[**InlineObject168**](InlineObject168.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_root_generate_exported

> post_pki_root_generate_exported(exported, inline_object169)
Generate a new CA certificate and private key used for signing.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**exported** | **String** | Must be \"internal\" or \"exported\". If set to \"exported\", the generated private key will be returned. This is your *only* chance to retrieve the private key! | [required] |
**inline_object169** | Option<[**InlineObject169**](InlineObject169.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_root_sign_intermediate

> post_pki_root_sign_intermediate(inline_object170)
Issue an intermediate CA certificate based on the provided CSR.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object170** | Option<[**InlineObject170**](InlineObject170.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_root_sign_self_issued

> post_pki_root_sign_self_issued(inline_object171)
Signs another CA's self-issued certificate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object171** | Option<[**InlineObject171**](InlineObject171.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_sign_role

> post_pki_sign_role(role, inline_object174)
Request certificates using a certain role with the provided details.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | The desired role with configuration for this request | [required] |
**inline_object174** | Option<[**InlineObject174**](InlineObject174.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_sign_verbatim

> post_pki_sign_verbatim(inline_object172)
Request certificates using a certain role with the provided details.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object172** | Option<[**InlineObject172**](InlineObject172.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_sign_verbatim_role

> post_pki_sign_verbatim_role(role, inline_object173)
Request certificates using a certain role with the provided details.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | The desired role with configuration for this request | [required] |
**inline_object173** | Option<[**InlineObject173**](InlineObject173.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_pki_tidy

> post_pki_tidy(inline_object175)
Tidy up the backend by removing expired certificates, revocation information, or both.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object175** | Option<[**InlineObject175**](InlineObject175.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_rabbitmq_config_connection

> post_rabbitmq_config_connection(inline_object176)
Configure the connection URI, username, and password to talk to RabbitMQ management HTTP API.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object176** | Option<[**InlineObject176**](InlineObject176.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_rabbitmq_config_lease

> post_rabbitmq_config_lease(inline_object177)
Configure the lease parameters for generated credentials

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object177** | Option<[**InlineObject177**](InlineObject177.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_rabbitmq_roles_name

> post_rabbitmq_roles_name(name, inline_object178)
Manage the roles that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object178** | Option<[**InlineObject178**](InlineObject178.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_config

> post_secret_config(inline_object179)
Configure backend level settings that are applied to every key in the key-value store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object179** | Option<[**InlineObject179**](InlineObject179.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_data_path

> post_secret_data_path(path, inline_object180)
Write, Read, and Delete data in the Key-Value Store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**inline_object180** | Option<[**InlineObject180**](InlineObject180.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_delete_path

> post_secret_delete_path(path, inline_object181)
Marks one or more versions as deleted in the KV store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**inline_object181** | Option<[**InlineObject181**](InlineObject181.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_destroy_path

> post_secret_destroy_path(path, inline_object182)
Permanently removes one or more versions in the KV store

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**inline_object182** | Option<[**InlineObject182**](InlineObject182.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_metadata_path

> post_secret_metadata_path(path, inline_object183)
Configures settings for the KV store

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**inline_object183** | Option<[**InlineObject183**](InlineObject183.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secret_undelete_path

> post_secret_undelete_path(path, inline_object184)
Undeletes one or more versions from the KV store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**path** | **String** | Location of the secret. | [required] |
**inline_object184** | Option<[**InlineObject184**](InlineObject184.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_secretv1_path

> post_secretv1_path(path)
Pass-through secret storage to the storage backend, allowing you to read/write arbitrary data into secret storage.

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


## post_ssh_config_ca

> post_ssh_config_ca(inline_object185)
Set the SSH private key used for signing certificates.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object185** | Option<[**InlineObject185**](InlineObject185.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_config_zeroaddress

> post_ssh_config_zeroaddress(inline_object186)
Assign zero address as default CIDR block for select roles.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object186** | Option<[**InlineObject186**](InlineObject186.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_creds_role

> post_ssh_creds_role(role, inline_object187)
Creates a credential for establishing SSH connection with the remote host.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | [Required] Name of the role | [required] |
**inline_object187** | Option<[**InlineObject187**](InlineObject187.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_keys_key_name

> post_ssh_keys_key_name(key_name, inline_object188)
Register a shared private key with Vault.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key_name** | **String** | [Required] Name of the key | [required] |
**inline_object188** | Option<[**InlineObject188**](InlineObject188.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_lookup

> post_ssh_lookup(inline_object189)
List all the roles associated with the given IP address.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object189** | Option<[**InlineObject189**](InlineObject189.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_roles_role

> post_ssh_roles_role(role, inline_object190)
Manage the 'roles' that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | [Required for all types] Name of the role being created. | [required] |
**inline_object190** | Option<[**InlineObject190**](InlineObject190.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_sign_role

> post_ssh_sign_role(role, inline_object191)
Request signing an SSH key using a certain role with the provided details.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | The desired role with configuration for this request. | [required] |
**inline_object191** | Option<[**InlineObject191**](InlineObject191.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_ssh_verify

> post_ssh_verify(inline_object192)
Validate the OTP provided by Vault SSH Agent.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object192** | Option<[**InlineObject192**](InlineObject192.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_totp_code_name

> post_totp_code_name(name, inline_object243)
Request time-based one-time use password or validate a password for a certain key .

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key. | [required] |
**inline_object243** | Option<[**InlineObject243**](InlineObject243.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_totp_keys_name

> post_totp_keys_name(name, inline_object244)
Manage the keys that can be created with this backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key. | [required] |
**inline_object244** | Option<[**InlineObject244**](InlineObject244.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_cache_config

> post_transit_cache_config(inline_object245)
Configures a new cache of the specified size

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object245** | Option<[**InlineObject245**](InlineObject245.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_datakey_plaintext_name

> post_transit_datakey_plaintext_name(name, plaintext, inline_object246)
Generate a data key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The backend key used for encrypting the data key | [required] |
**plaintext** | **String** | \"plaintext\" will return the key in both plaintext and ciphertext; \"wrapped\" will return the ciphertext only. | [required] |
**inline_object246** | Option<[**InlineObject246**](InlineObject246.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_decrypt_name

> post_transit_decrypt_name(name, inline_object247)
Decrypt a ciphertext value using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the policy | [required] |
**inline_object247** | Option<[**InlineObject247**](InlineObject247.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_encrypt_name

> post_transit_encrypt_name(name, inline_object248)
Encrypt a plaintext value or a batch of plaintext blocks using a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the policy | [required] |
**inline_object248** | Option<[**InlineObject248**](InlineObject248.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_hash

> post_transit_hash(inline_object249)
Generate a hash sum for input data

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object249** | Option<[**InlineObject249**](InlineObject249.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_hash_urlalgorithm

> post_transit_hash_urlalgorithm(urlalgorithm, inline_object250)
Generate a hash sum for input data

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**urlalgorithm** | **String** | Algorithm to use (POST URL parameter) | [required] |
**inline_object250** | Option<[**InlineObject250**](InlineObject250.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_hmac_name

> post_transit_hmac_name(name, inline_object251)
Generate an HMAC for input data using the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The key to use for the HMAC function | [required] |
**inline_object251** | Option<[**InlineObject251**](InlineObject251.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_hmac_name_urlalgorithm

> post_transit_hmac_name_urlalgorithm(name, urlalgorithm, inline_object252)
Generate an HMAC for input data using the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The key to use for the HMAC function | [required] |
**urlalgorithm** | **String** | Algorithm to use (POST URL parameter) | [required] |
**inline_object252** | Option<[**InlineObject252**](InlineObject252.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_keys_name

> post_transit_keys_name(name, inline_object253)
Managed named encryption keys

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |
**inline_object253** | Option<[**InlineObject253**](InlineObject253.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_keys_name_config

> post_transit_keys_name_config(name, inline_object254)
Configure a named encryption key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |
**inline_object254** | Option<[**InlineObject254**](InlineObject254.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_keys_name_rotate

> post_transit_keys_name_rotate(name)
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


## post_transit_keys_name_trim

> post_transit_keys_name_trim(name, inline_object255)
Trim key versions of a named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |
**inline_object255** | Option<[**InlineObject255**](InlineObject255.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_random

> post_transit_random(inline_object256)
Generate random bytes

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object256** | Option<[**InlineObject256**](InlineObject256.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_random_urlbytes

> post_transit_random_urlbytes(urlbytes, inline_object257)
Generate random bytes

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**urlbytes** | **String** | The number of bytes to generate (POST URL parameter) | [required] |
**inline_object257** | Option<[**InlineObject257**](InlineObject257.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_restore

> post_transit_restore(inline_object258)
Restore the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object258** | Option<[**InlineObject258**](InlineObject258.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_restore_name

> post_transit_restore_name(name, inline_object259)
Restore the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | If set, this will be the name of the restored key. | [required] |
**inline_object259** | Option<[**InlineObject259**](InlineObject259.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_rewrap_name

> post_transit_rewrap_name(name, inline_object260)
Rewrap ciphertext

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the key | [required] |
**inline_object260** | Option<[**InlineObject260**](InlineObject260.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_sign_name

> post_transit_sign_name(name, inline_object261)
Generate a signature for input data using the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The key to use | [required] |
**inline_object261** | Option<[**InlineObject261**](InlineObject261.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_sign_name_urlalgorithm

> post_transit_sign_name_urlalgorithm(name, urlalgorithm, inline_object262)
Generate a signature for input data using the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The key to use | [required] |
**urlalgorithm** | **String** | Hash algorithm to use (POST URL parameter) | [required] |
**inline_object262** | Option<[**InlineObject262**](InlineObject262.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_verify_name

> post_transit_verify_name(name, inline_object263)
Verify a signature or HMAC for input data created using the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The key to use | [required] |
**inline_object263** | Option<[**InlineObject263**](InlineObject263.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_transit_verify_name_urlalgorithm

> post_transit_verify_name_urlalgorithm(name, urlalgorithm, inline_object264)
Verify a signature or HMAC for input data created using the named key

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The key to use | [required] |
**urlalgorithm** | **String** | Hash algorithm to use (POST URL parameter) | [required] |
**inline_object264** | Option<[**InlineObject264**](InlineObject264.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

