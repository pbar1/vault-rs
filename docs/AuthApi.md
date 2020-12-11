# \AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_auth_alicloud_role_role**](AuthApi.md#delete_auth_alicloud_role_role) | **delete** /auth/alicloud/role/{role} | Create a role and associate policies to it.
[**delete_auth_approle_role_role_name**](AuthApi.md#delete_auth_approle_role_role_name) | **delete** /auth/approle/role/{role_name} | Register an role with the backend.
[**delete_auth_approle_role_role_name_bind_secret_id**](AuthApi.md#delete_auth_approle_role_role_name_bind_secret_id) | **delete** /auth/approle/role/{role_name}/bind-secret-id | Impose secret_id to be presented during login using this role.
[**delete_auth_approle_role_role_name_bound_cidr_list**](AuthApi.md#delete_auth_approle_role_role_name_bound_cidr_list) | **delete** /auth/approle/role/{role_name}/bound-cidr-list | Deprecated: Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation
[**delete_auth_approle_role_role_name_period**](AuthApi.md#delete_auth_approle_role_role_name_period) | **delete** /auth/approle/role/{role_name}/period | Updates the value of 'period' on the role
[**delete_auth_approle_role_role_name_policies**](AuthApi.md#delete_auth_approle_role_role_name_policies) | **delete** /auth/approle/role/{role_name}/policies | Policies of the role.
[**delete_auth_approle_role_role_name_secret_id_accessor_destroy**](AuthApi.md#delete_auth_approle_role_role_name_secret_id_accessor_destroy) | **delete** /auth/approle/role/{role_name}/secret-id-accessor/destroy | 
[**delete_auth_approle_role_role_name_secret_id_bound_cidrs**](AuthApi.md#delete_auth_approle_role_role_name_secret_id_bound_cidrs) | **delete** /auth/approle/role/{role_name}/secret-id-bound-cidrs | Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation
[**delete_auth_approle_role_role_name_secret_id_destroy**](AuthApi.md#delete_auth_approle_role_role_name_secret_id_destroy) | **delete** /auth/approle/role/{role_name}/secret-id/destroy | Invalidate an issued secret_id
[**delete_auth_approle_role_role_name_secret_id_num_uses**](AuthApi.md#delete_auth_approle_role_role_name_secret_id_num_uses) | **delete** /auth/approle/role/{role_name}/secret-id-num-uses | Use limit of the SecretID generated against the role.
[**delete_auth_approle_role_role_name_secret_id_ttl**](AuthApi.md#delete_auth_approle_role_role_name_secret_id_ttl) | **delete** /auth/approle/role/{role_name}/secret-id-ttl | Duration in seconds, representing the lifetime of the SecretIDs that are generated against the role using 'role/<role_name>/secret-id' or 'role/<role_name>/custom-secret-id' endpoints.
[**delete_auth_approle_role_role_name_token_bound_cidrs**](AuthApi.md#delete_auth_approle_role_role_name_token_bound_cidrs) | **delete** /auth/approle/role/{role_name}/token-bound-cidrs | Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can use the returned token.
[**delete_auth_approle_role_role_name_token_max_ttl**](AuthApi.md#delete_auth_approle_role_role_name_token_max_ttl) | **delete** /auth/approle/role/{role_name}/token-max-ttl | Duration in seconds, the maximum lifetime of the tokens issued by using the SecretIDs that were generated against this role, after which the tokens are not allowed to be renewed.
[**delete_auth_approle_role_role_name_token_num_uses**](AuthApi.md#delete_auth_approle_role_role_name_token_num_uses) | **delete** /auth/approle/role/{role_name}/token-num-uses | Number of times issued tokens can be used
[**delete_auth_approle_role_role_name_token_ttl**](AuthApi.md#delete_auth_approle_role_role_name_token_ttl) | **delete** /auth/approle/role/{role_name}/token-ttl | Duration in seconds, the lifetime of the token issued by using the SecretID that is generated against this role, before which the token needs to be renewed.
[**delete_auth_aws_config_certificate_cert_name**](AuthApi.md#delete_auth_aws_config_certificate_cert_name) | **delete** /auth/aws/config/certificate/{cert_name} | 
[**delete_auth_aws_config_client**](AuthApi.md#delete_auth_aws_config_client) | **delete** /auth/aws/config/client | 
[**delete_auth_aws_config_sts_account_id**](AuthApi.md#delete_auth_aws_config_sts_account_id) | **delete** /auth/aws/config/sts/{account_id} | 
[**delete_auth_aws_config_tidy_identity_whitelist**](AuthApi.md#delete_auth_aws_config_tidy_identity_whitelist) | **delete** /auth/aws/config/tidy/identity-whitelist | 
[**delete_auth_aws_config_tidy_roletag_blacklist**](AuthApi.md#delete_auth_aws_config_tidy_roletag_blacklist) | **delete** /auth/aws/config/tidy/roletag-blacklist | 
[**delete_auth_aws_identity_whitelist_instance_id**](AuthApi.md#delete_auth_aws_identity_whitelist_instance_id) | **delete** /auth/aws/identity-whitelist/{instance_id} | 
[**delete_auth_aws_role_role**](AuthApi.md#delete_auth_aws_role_role) | **delete** /auth/aws/role/{role} | 
[**delete_auth_aws_roletag_blacklist_role_tag**](AuthApi.md#delete_auth_aws_roletag_blacklist_role_tag) | **delete** /auth/aws/roletag-blacklist/{role_tag} | 
[**delete_auth_azure_config**](AuthApi.md#delete_auth_azure_config) | **delete** /auth/azure/config | Configures the Azure authentication backend.
[**delete_auth_azure_role_name**](AuthApi.md#delete_auth_azure_role_name) | **delete** /auth/azure/role/{name} | Register an role with the backend.
[**delete_auth_cert_certs_name**](AuthApi.md#delete_auth_cert_certs_name) | **delete** /auth/cert/certs/{name} | Manage trusted certificates used for authentication.
[**delete_auth_cert_crls_name**](AuthApi.md#delete_auth_cert_crls_name) | **delete** /auth/cert/crls/{name} | Manage Certificate Revocation Lists checked during authentication.
[**delete_auth_gcp_role_name**](AuthApi.md#delete_auth_gcp_role_name) | **delete** /auth/gcp/role/{name} | Create a GCP role with associated policies and required attributes.
[**delete_auth_github_map_teams_key**](AuthApi.md#delete_auth_github_map_teams_key) | **delete** /auth/github/map/teams/{key} | Read/write/delete a single teams mapping
[**delete_auth_github_map_users_key**](AuthApi.md#delete_auth_github_map_users_key) | **delete** /auth/github/map/users/{key} | Read/write/delete a single users mapping
[**delete_auth_jwt_role_name**](AuthApi.md#delete_auth_jwt_role_name) | **delete** /auth/jwt/role/{name} | Delete an existing role.
[**delete_auth_kubernetes_role_name**](AuthApi.md#delete_auth_kubernetes_role_name) | **delete** /auth/kubernetes/role/{name} | Register an role with the backend.
[**delete_auth_ldap_groups_name**](AuthApi.md#delete_auth_ldap_groups_name) | **delete** /auth/ldap/groups/{name} | Manage additional groups for users allowed to authenticate.
[**delete_auth_ldap_users_name**](AuthApi.md#delete_auth_ldap_users_name) | **delete** /auth/ldap/users/{name} | Manage users allowed to authenticate.
[**delete_auth_oidc_role_name**](AuthApi.md#delete_auth_oidc_role_name) | **delete** /auth/oidc/role/{name} | Delete an existing role.
[**delete_auth_okta_groups_name**](AuthApi.md#delete_auth_okta_groups_name) | **delete** /auth/okta/groups/{name} | Manage users allowed to authenticate.
[**delete_auth_okta_users_name**](AuthApi.md#delete_auth_okta_users_name) | **delete** /auth/okta/users/{name} | Manage additional groups for users allowed to authenticate.
[**delete_auth_radius_users_name**](AuthApi.md#delete_auth_radius_users_name) | **delete** /auth/radius/users/{name} | Manage users allowed to authenticate.
[**delete_auth_token_roles_role_name**](AuthApi.md#delete_auth_token_roles_role_name) | **delete** /auth/token/roles/{role_name} | 
[**delete_auth_userpass_users_username**](AuthApi.md#delete_auth_userpass_users_username) | **delete** /auth/userpass/users/{username} | Manage users allowed to authenticate.
[**get_auth_alicloud_role**](AuthApi.md#get_auth_alicloud_role) | **get** /auth/alicloud/role | Lists all the roles that are registered with Vault.
[**get_auth_alicloud_role_role**](AuthApi.md#get_auth_alicloud_role_role) | **get** /auth/alicloud/role/{role} | Create a role and associate policies to it.
[**get_auth_alicloud_roles**](AuthApi.md#get_auth_alicloud_roles) | **get** /auth/alicloud/roles | Lists all the roles that are registered with Vault.
[**get_auth_approle_role**](AuthApi.md#get_auth_approle_role) | **get** /auth/approle/role | Lists all the roles registered with the backend.
[**get_auth_approle_role_role_name**](AuthApi.md#get_auth_approle_role_role_name) | **get** /auth/approle/role/{role_name} | Register an role with the backend.
[**get_auth_approle_role_role_name_bind_secret_id**](AuthApi.md#get_auth_approle_role_role_name_bind_secret_id) | **get** /auth/approle/role/{role_name}/bind-secret-id | Impose secret_id to be presented during login using this role.
[**get_auth_approle_role_role_name_bound_cidr_list**](AuthApi.md#get_auth_approle_role_role_name_bound_cidr_list) | **get** /auth/approle/role/{role_name}/bound-cidr-list | Deprecated: Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation
[**get_auth_approle_role_role_name_local_secret_ids**](AuthApi.md#get_auth_approle_role_role_name_local_secret_ids) | **get** /auth/approle/role/{role_name}/local-secret-ids | Enables cluster local secret IDs
[**get_auth_approle_role_role_name_period**](AuthApi.md#get_auth_approle_role_role_name_period) | **get** /auth/approle/role/{role_name}/period | Updates the value of 'period' on the role
[**get_auth_approle_role_role_name_policies**](AuthApi.md#get_auth_approle_role_role_name_policies) | **get** /auth/approle/role/{role_name}/policies | Policies of the role.
[**get_auth_approle_role_role_name_role_id**](AuthApi.md#get_auth_approle_role_role_name_role_id) | **get** /auth/approle/role/{role_name}/role-id | Returns the 'role_id' of the role.
[**get_auth_approle_role_role_name_secret_id**](AuthApi.md#get_auth_approle_role_role_name_secret_id) | **get** /auth/approle/role/{role_name}/secret-id | Generate a SecretID against this role.
[**get_auth_approle_role_role_name_secret_id_bound_cidrs**](AuthApi.md#get_auth_approle_role_role_name_secret_id_bound_cidrs) | **get** /auth/approle/role/{role_name}/secret-id-bound-cidrs | Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation
[**get_auth_approle_role_role_name_secret_id_num_uses**](AuthApi.md#get_auth_approle_role_role_name_secret_id_num_uses) | **get** /auth/approle/role/{role_name}/secret-id-num-uses | Use limit of the SecretID generated against the role.
[**get_auth_approle_role_role_name_secret_id_ttl**](AuthApi.md#get_auth_approle_role_role_name_secret_id_ttl) | **get** /auth/approle/role/{role_name}/secret-id-ttl | Duration in seconds, representing the lifetime of the SecretIDs that are generated against the role using 'role/<role_name>/secret-id' or 'role/<role_name>/custom-secret-id' endpoints.
[**get_auth_approle_role_role_name_token_bound_cidrs**](AuthApi.md#get_auth_approle_role_role_name_token_bound_cidrs) | **get** /auth/approle/role/{role_name}/token-bound-cidrs | Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can use the returned token.
[**get_auth_approle_role_role_name_token_max_ttl**](AuthApi.md#get_auth_approle_role_role_name_token_max_ttl) | **get** /auth/approle/role/{role_name}/token-max-ttl | Duration in seconds, the maximum lifetime of the tokens issued by using the SecretIDs that were generated against this role, after which the tokens are not allowed to be renewed.
[**get_auth_approle_role_role_name_token_num_uses**](AuthApi.md#get_auth_approle_role_role_name_token_num_uses) | **get** /auth/approle/role/{role_name}/token-num-uses | Number of times issued tokens can be used
[**get_auth_approle_role_role_name_token_ttl**](AuthApi.md#get_auth_approle_role_role_name_token_ttl) | **get** /auth/approle/role/{role_name}/token-ttl | Duration in seconds, the lifetime of the token issued by using the SecretID that is generated against this role, before which the token needs to be renewed.
[**get_auth_aws_config_certificate_cert_name**](AuthApi.md#get_auth_aws_config_certificate_cert_name) | **get** /auth/aws/config/certificate/{cert_name} | 
[**get_auth_aws_config_certificates**](AuthApi.md#get_auth_aws_config_certificates) | **get** /auth/aws/config/certificates | 
[**get_auth_aws_config_client**](AuthApi.md#get_auth_aws_config_client) | **get** /auth/aws/config/client | 
[**get_auth_aws_config_identity**](AuthApi.md#get_auth_aws_config_identity) | **get** /auth/aws/config/identity | 
[**get_auth_aws_config_sts**](AuthApi.md#get_auth_aws_config_sts) | **get** /auth/aws/config/sts | 
[**get_auth_aws_config_sts_account_id**](AuthApi.md#get_auth_aws_config_sts_account_id) | **get** /auth/aws/config/sts/{account_id} | 
[**get_auth_aws_config_tidy_identity_whitelist**](AuthApi.md#get_auth_aws_config_tidy_identity_whitelist) | **get** /auth/aws/config/tidy/identity-whitelist | 
[**get_auth_aws_config_tidy_roletag_blacklist**](AuthApi.md#get_auth_aws_config_tidy_roletag_blacklist) | **get** /auth/aws/config/tidy/roletag-blacklist | 
[**get_auth_aws_identity_whitelist**](AuthApi.md#get_auth_aws_identity_whitelist) | **get** /auth/aws/identity-whitelist | 
[**get_auth_aws_identity_whitelist_instance_id**](AuthApi.md#get_auth_aws_identity_whitelist_instance_id) | **get** /auth/aws/identity-whitelist/{instance_id} | 
[**get_auth_aws_role**](AuthApi.md#get_auth_aws_role) | **get** /auth/aws/role | 
[**get_auth_aws_role_role**](AuthApi.md#get_auth_aws_role_role) | **get** /auth/aws/role/{role} | 
[**get_auth_aws_roles**](AuthApi.md#get_auth_aws_roles) | **get** /auth/aws/roles | 
[**get_auth_aws_roletag_blacklist**](AuthApi.md#get_auth_aws_roletag_blacklist) | **get** /auth/aws/roletag-blacklist | 
[**get_auth_aws_roletag_blacklist_role_tag**](AuthApi.md#get_auth_aws_roletag_blacklist_role_tag) | **get** /auth/aws/roletag-blacklist/{role_tag} | 
[**get_auth_azure_config**](AuthApi.md#get_auth_azure_config) | **get** /auth/azure/config | Configures the Azure authentication backend.
[**get_auth_azure_role**](AuthApi.md#get_auth_azure_role) | **get** /auth/azure/role | Lists all the roles registered with the backend.
[**get_auth_azure_role_name**](AuthApi.md#get_auth_azure_role_name) | **get** /auth/azure/role/{name} | Register an role with the backend.
[**get_auth_cert_certs**](AuthApi.md#get_auth_cert_certs) | **get** /auth/cert/certs | Manage trusted certificates used for authentication.
[**get_auth_cert_certs_name**](AuthApi.md#get_auth_cert_certs_name) | **get** /auth/cert/certs/{name} | Manage trusted certificates used for authentication.
[**get_auth_cert_crls_name**](AuthApi.md#get_auth_cert_crls_name) | **get** /auth/cert/crls/{name} | Manage Certificate Revocation Lists checked during authentication.
[**get_auth_gcp_config**](AuthApi.md#get_auth_gcp_config) | **get** /auth/gcp/config | Configure credentials used to query the GCP IAM API to verify authenticating service accounts
[**get_auth_gcp_role**](AuthApi.md#get_auth_gcp_role) | **get** /auth/gcp/role | Lists all the roles that are registered with Vault.
[**get_auth_gcp_role_name**](AuthApi.md#get_auth_gcp_role_name) | **get** /auth/gcp/role/{name} | Create a GCP role with associated policies and required attributes.
[**get_auth_gcp_roles**](AuthApi.md#get_auth_gcp_roles) | **get** /auth/gcp/roles | Lists all the roles that are registered with Vault.
[**get_auth_github_config**](AuthApi.md#get_auth_github_config) | **get** /auth/github/config | 
[**get_auth_github_duo_config**](AuthApi.md#get_auth_github_duo_config) | **get** /auth/github/duo/config | Configure Duo second factor behavior.
[**get_auth_github_map_teams**](AuthApi.md#get_auth_github_map_teams) | **get** /auth/github/map/teams | Read mappings for teams
[**get_auth_github_map_teams_key**](AuthApi.md#get_auth_github_map_teams_key) | **get** /auth/github/map/teams/{key} | Read/write/delete a single teams mapping
[**get_auth_github_map_users**](AuthApi.md#get_auth_github_map_users) | **get** /auth/github/map/users | Read mappings for users
[**get_auth_github_map_users_key**](AuthApi.md#get_auth_github_map_users_key) | **get** /auth/github/map/users/{key} | Read/write/delete a single users mapping
[**get_auth_github_mfa_config**](AuthApi.md#get_auth_github_mfa_config) | **get** /auth/github/mfa_config | Configure multi factor backend.
[**get_auth_jwt_config**](AuthApi.md#get_auth_jwt_config) | **get** /auth/jwt/config | Read the current JWT authentication backend configuration.
[**get_auth_jwt_oidc_callback**](AuthApi.md#get_auth_jwt_oidc_callback) | **get** /auth/jwt/oidc/callback | Callback endpoint to complete an OIDC login.
[**get_auth_jwt_role**](AuthApi.md#get_auth_jwt_role) | **get** /auth/jwt/role | Lists all the roles registered with the backend.
[**get_auth_jwt_role_name**](AuthApi.md#get_auth_jwt_role_name) | **get** /auth/jwt/role/{name} | Read an existing role.
[**get_auth_kubernetes_config**](AuthApi.md#get_auth_kubernetes_config) | **get** /auth/kubernetes/config | Configures the JWT Public Key and Kubernetes API information.
[**get_auth_kubernetes_role**](AuthApi.md#get_auth_kubernetes_role) | **get** /auth/kubernetes/role | Lists all the roles registered with the backend.
[**get_auth_kubernetes_role_name**](AuthApi.md#get_auth_kubernetes_role_name) | **get** /auth/kubernetes/role/{name} | Register an role with the backend.
[**get_auth_ldap_config**](AuthApi.md#get_auth_ldap_config) | **get** /auth/ldap/config | Configure the LDAP server to connect to, along with its options.
[**get_auth_ldap_duo_config**](AuthApi.md#get_auth_ldap_duo_config) | **get** /auth/ldap/duo/config | Configure Duo second factor behavior.
[**get_auth_ldap_groups**](AuthApi.md#get_auth_ldap_groups) | **get** /auth/ldap/groups | Manage additional groups for users allowed to authenticate.
[**get_auth_ldap_groups_name**](AuthApi.md#get_auth_ldap_groups_name) | **get** /auth/ldap/groups/{name} | Manage additional groups for users allowed to authenticate.
[**get_auth_ldap_mfa_config**](AuthApi.md#get_auth_ldap_mfa_config) | **get** /auth/ldap/mfa_config | Configure multi factor backend.
[**get_auth_ldap_users**](AuthApi.md#get_auth_ldap_users) | **get** /auth/ldap/users | Manage users allowed to authenticate.
[**get_auth_ldap_users_name**](AuthApi.md#get_auth_ldap_users_name) | **get** /auth/ldap/users/{name} | Manage users allowed to authenticate.
[**get_auth_oidc_config**](AuthApi.md#get_auth_oidc_config) | **get** /auth/oidc/config | Read the current JWT authentication backend configuration.
[**get_auth_oidc_oidc_callback**](AuthApi.md#get_auth_oidc_oidc_callback) | **get** /auth/oidc/oidc/callback | Callback endpoint to complete an OIDC login.
[**get_auth_oidc_role**](AuthApi.md#get_auth_oidc_role) | **get** /auth/oidc/role | Lists all the roles registered with the backend.
[**get_auth_oidc_role_name**](AuthApi.md#get_auth_oidc_role_name) | **get** /auth/oidc/role/{name} | Read an existing role.
[**get_auth_okta_config**](AuthApi.md#get_auth_okta_config) | **get** /auth/okta/config | This endpoint allows you to configure the Okta and its configuration options.  The Okta organization are the characters at the front of the URL for Okta. Example https://ORG.okta.com
[**get_auth_okta_duo_config**](AuthApi.md#get_auth_okta_duo_config) | **get** /auth/okta/duo/config | Configure Duo second factor behavior.
[**get_auth_okta_groups**](AuthApi.md#get_auth_okta_groups) | **get** /auth/okta/groups | Manage users allowed to authenticate.
[**get_auth_okta_groups_name**](AuthApi.md#get_auth_okta_groups_name) | **get** /auth/okta/groups/{name} | Manage users allowed to authenticate.
[**get_auth_okta_mfa_config**](AuthApi.md#get_auth_okta_mfa_config) | **get** /auth/okta/mfa_config | Configure multi factor backend.
[**get_auth_okta_users**](AuthApi.md#get_auth_okta_users) | **get** /auth/okta/users | Manage additional groups for users allowed to authenticate.
[**get_auth_okta_users_name**](AuthApi.md#get_auth_okta_users_name) | **get** /auth/okta/users/{name} | Manage additional groups for users allowed to authenticate.
[**get_auth_radius_config**](AuthApi.md#get_auth_radius_config) | **get** /auth/radius/config | Configure the RADIUS server to connect to, along with its options.
[**get_auth_radius_duo_config**](AuthApi.md#get_auth_radius_duo_config) | **get** /auth/radius/duo/config | Configure Duo second factor behavior.
[**get_auth_radius_mfa_config**](AuthApi.md#get_auth_radius_mfa_config) | **get** /auth/radius/mfa_config | Configure multi factor backend.
[**get_auth_radius_users**](AuthApi.md#get_auth_radius_users) | **get** /auth/radius/users | Manage users allowed to authenticate.
[**get_auth_radius_users_name**](AuthApi.md#get_auth_radius_users_name) | **get** /auth/radius/users/{name} | Manage users allowed to authenticate.
[**get_auth_token_accessors**](AuthApi.md#get_auth_token_accessors) | **get** /auth/token/accessors/ | List token accessors, which can then be be used to iterate and discover their properties or revoke them. Because this can be used to cause a denial of service, this endpoint requires 'sudo' capability in addition to 'list'.
[**get_auth_token_lookup**](AuthApi.md#get_auth_token_lookup) | **get** /auth/token/lookup | This endpoint will lookup a token and its properties.
[**get_auth_token_lookup_self**](AuthApi.md#get_auth_token_lookup_self) | **get** /auth/token/lookup-self | This endpoint will lookup a token and its properties.
[**get_auth_token_roles**](AuthApi.md#get_auth_token_roles) | **get** /auth/token/roles | This endpoint lists configured roles.
[**get_auth_token_roles_role_name**](AuthApi.md#get_auth_token_roles_role_name) | **get** /auth/token/roles/{role_name} | 
[**get_auth_userpass_duo_config**](AuthApi.md#get_auth_userpass_duo_config) | **get** /auth/userpass/duo/config | Configure Duo second factor behavior.
[**get_auth_userpass_mfa_config**](AuthApi.md#get_auth_userpass_mfa_config) | **get** /auth/userpass/mfa_config | Configure multi factor backend.
[**get_auth_userpass_users**](AuthApi.md#get_auth_userpass_users) | **get** /auth/userpass/users | Manage users allowed to authenticate.
[**get_auth_userpass_users_username**](AuthApi.md#get_auth_userpass_users_username) | **get** /auth/userpass/users/{username} | Manage users allowed to authenticate.
[**post_auth_alicloud_login**](AuthApi.md#post_auth_alicloud_login) | **post** /auth/alicloud/login | Authenticates an RAM entity with Vault.
[**post_auth_alicloud_role_role**](AuthApi.md#post_auth_alicloud_role_role) | **post** /auth/alicloud/role/{role} | Create a role and associate policies to it.
[**post_auth_approle_login**](AuthApi.md#post_auth_approle_login) | **post** /auth/approle/login | Issue a token based on the credentials supplied
[**post_auth_approle_role_role_name**](AuthApi.md#post_auth_approle_role_role_name) | **post** /auth/approle/role/{role_name} | Register an role with the backend.
[**post_auth_approle_role_role_name_bind_secret_id**](AuthApi.md#post_auth_approle_role_role_name_bind_secret_id) | **post** /auth/approle/role/{role_name}/bind-secret-id | Impose secret_id to be presented during login using this role.
[**post_auth_approle_role_role_name_bound_cidr_list**](AuthApi.md#post_auth_approle_role_role_name_bound_cidr_list) | **post** /auth/approle/role/{role_name}/bound-cidr-list | Deprecated: Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation
[**post_auth_approle_role_role_name_custom_secret_id**](AuthApi.md#post_auth_approle_role_role_name_custom_secret_id) | **post** /auth/approle/role/{role_name}/custom-secret-id | Assign a SecretID of choice against the role.
[**post_auth_approle_role_role_name_period**](AuthApi.md#post_auth_approle_role_role_name_period) | **post** /auth/approle/role/{role_name}/period | Updates the value of 'period' on the role
[**post_auth_approle_role_role_name_policies**](AuthApi.md#post_auth_approle_role_role_name_policies) | **post** /auth/approle/role/{role_name}/policies | Policies of the role.
[**post_auth_approle_role_role_name_role_id**](AuthApi.md#post_auth_approle_role_role_name_role_id) | **post** /auth/approle/role/{role_name}/role-id | Returns the 'role_id' of the role.
[**post_auth_approle_role_role_name_secret_id**](AuthApi.md#post_auth_approle_role_role_name_secret_id) | **post** /auth/approle/role/{role_name}/secret-id | Generate a SecretID against this role.
[**post_auth_approle_role_role_name_secret_id_accessor_destroy**](AuthApi.md#post_auth_approle_role_role_name_secret_id_accessor_destroy) | **post** /auth/approle/role/{role_name}/secret-id-accessor/destroy | 
[**post_auth_approle_role_role_name_secret_id_accessor_lookup**](AuthApi.md#post_auth_approle_role_role_name_secret_id_accessor_lookup) | **post** /auth/approle/role/{role_name}/secret-id-accessor/lookup | 
[**post_auth_approle_role_role_name_secret_id_bound_cidrs**](AuthApi.md#post_auth_approle_role_role_name_secret_id_bound_cidrs) | **post** /auth/approle/role/{role_name}/secret-id-bound-cidrs | Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation
[**post_auth_approle_role_role_name_secret_id_destroy**](AuthApi.md#post_auth_approle_role_role_name_secret_id_destroy) | **post** /auth/approle/role/{role_name}/secret-id/destroy | Invalidate an issued secret_id
[**post_auth_approle_role_role_name_secret_id_lookup**](AuthApi.md#post_auth_approle_role_role_name_secret_id_lookup) | **post** /auth/approle/role/{role_name}/secret-id/lookup | Read the properties of an issued secret_id
[**post_auth_approle_role_role_name_secret_id_num_uses**](AuthApi.md#post_auth_approle_role_role_name_secret_id_num_uses) | **post** /auth/approle/role/{role_name}/secret-id-num-uses | Use limit of the SecretID generated against the role.
[**post_auth_approle_role_role_name_secret_id_ttl**](AuthApi.md#post_auth_approle_role_role_name_secret_id_ttl) | **post** /auth/approle/role/{role_name}/secret-id-ttl | Duration in seconds, representing the lifetime of the SecretIDs that are generated against the role using 'role/<role_name>/secret-id' or 'role/<role_name>/custom-secret-id' endpoints.
[**post_auth_approle_role_role_name_token_bound_cidrs**](AuthApi.md#post_auth_approle_role_role_name_token_bound_cidrs) | **post** /auth/approle/role/{role_name}/token-bound-cidrs | Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can use the returned token.
[**post_auth_approle_role_role_name_token_max_ttl**](AuthApi.md#post_auth_approle_role_role_name_token_max_ttl) | **post** /auth/approle/role/{role_name}/token-max-ttl | Duration in seconds, the maximum lifetime of the tokens issued by using the SecretIDs that were generated against this role, after which the tokens are not allowed to be renewed.
[**post_auth_approle_role_role_name_token_num_uses**](AuthApi.md#post_auth_approle_role_role_name_token_num_uses) | **post** /auth/approle/role/{role_name}/token-num-uses | Number of times issued tokens can be used
[**post_auth_approle_role_role_name_token_ttl**](AuthApi.md#post_auth_approle_role_role_name_token_ttl) | **post** /auth/approle/role/{role_name}/token-ttl | Duration in seconds, the lifetime of the token issued by using the SecretID that is generated against this role, before which the token needs to be renewed.
[**post_auth_approle_tidy_secret_id**](AuthApi.md#post_auth_approle_tidy_secret_id) | **post** /auth/approle/tidy/secret-id | Trigger the clean-up of expired SecretID entries.
[**post_auth_aws_config_certificate_cert_name**](AuthApi.md#post_auth_aws_config_certificate_cert_name) | **post** /auth/aws/config/certificate/{cert_name} | 
[**post_auth_aws_config_client**](AuthApi.md#post_auth_aws_config_client) | **post** /auth/aws/config/client | 
[**post_auth_aws_config_identity**](AuthApi.md#post_auth_aws_config_identity) | **post** /auth/aws/config/identity | 
[**post_auth_aws_config_rotate_root**](AuthApi.md#post_auth_aws_config_rotate_root) | **post** /auth/aws/config/rotate-root | 
[**post_auth_aws_config_sts_account_id**](AuthApi.md#post_auth_aws_config_sts_account_id) | **post** /auth/aws/config/sts/{account_id} | 
[**post_auth_aws_config_tidy_identity_whitelist**](AuthApi.md#post_auth_aws_config_tidy_identity_whitelist) | **post** /auth/aws/config/tidy/identity-whitelist | 
[**post_auth_aws_config_tidy_roletag_blacklist**](AuthApi.md#post_auth_aws_config_tidy_roletag_blacklist) | **post** /auth/aws/config/tidy/roletag-blacklist | 
[**post_auth_aws_login**](AuthApi.md#post_auth_aws_login) | **post** /auth/aws/login | 
[**post_auth_aws_role_role**](AuthApi.md#post_auth_aws_role_role) | **post** /auth/aws/role/{role} | 
[**post_auth_aws_role_role_tag**](AuthApi.md#post_auth_aws_role_role_tag) | **post** /auth/aws/role/{role}/tag | 
[**post_auth_aws_roletag_blacklist_role_tag**](AuthApi.md#post_auth_aws_roletag_blacklist_role_tag) | **post** /auth/aws/roletag-blacklist/{role_tag} | 
[**post_auth_aws_tidy_identity_whitelist**](AuthApi.md#post_auth_aws_tidy_identity_whitelist) | **post** /auth/aws/tidy/identity-whitelist | 
[**post_auth_aws_tidy_roletag_blacklist**](AuthApi.md#post_auth_aws_tidy_roletag_blacklist) | **post** /auth/aws/tidy/roletag-blacklist | 
[**post_auth_azure_config**](AuthApi.md#post_auth_azure_config) | **post** /auth/azure/config | Configures the Azure authentication backend.
[**post_auth_azure_login**](AuthApi.md#post_auth_azure_login) | **post** /auth/azure/login | Authenticates Azure Managed Service Identities with Vault.
[**post_auth_azure_role_name**](AuthApi.md#post_auth_azure_role_name) | **post** /auth/azure/role/{name} | Register an role with the backend.
[**post_auth_cert_certs_name**](AuthApi.md#post_auth_cert_certs_name) | **post** /auth/cert/certs/{name} | Manage trusted certificates used for authentication.
[**post_auth_cert_config**](AuthApi.md#post_auth_cert_config) | **post** /auth/cert/config | 
[**post_auth_cert_crls_name**](AuthApi.md#post_auth_cert_crls_name) | **post** /auth/cert/crls/{name} | Manage Certificate Revocation Lists checked during authentication.
[**post_auth_cert_login**](AuthApi.md#post_auth_cert_login) | **post** /auth/cert/login | 
[**post_auth_gcp_config**](AuthApi.md#post_auth_gcp_config) | **post** /auth/gcp/config | Configure credentials used to query the GCP IAM API to verify authenticating service accounts
[**post_auth_gcp_login**](AuthApi.md#post_auth_gcp_login) | **post** /auth/gcp/login | 
[**post_auth_gcp_role_name**](AuthApi.md#post_auth_gcp_role_name) | **post** /auth/gcp/role/{name} | Create a GCP role with associated policies and required attributes.
[**post_auth_gcp_role_name_labels**](AuthApi.md#post_auth_gcp_role_name_labels) | **post** /auth/gcp/role/{name}/labels | Add or remove labels for an existing 'gce' role
[**post_auth_gcp_role_name_service_accounts**](AuthApi.md#post_auth_gcp_role_name_service_accounts) | **post** /auth/gcp/role/{name}/service-accounts | Add or remove service accounts for an existing `iam` role
[**post_auth_github_config**](AuthApi.md#post_auth_github_config) | **post** /auth/github/config | 
[**post_auth_github_duo_access**](AuthApi.md#post_auth_github_duo_access) | **post** /auth/github/duo/access | Configure the access keys and host for Duo API connections.
[**post_auth_github_duo_config**](AuthApi.md#post_auth_github_duo_config) | **post** /auth/github/duo/config | Configure Duo second factor behavior.
[**post_auth_github_login**](AuthApi.md#post_auth_github_login) | **post** /auth/github/login | 
[**post_auth_github_map_teams_key**](AuthApi.md#post_auth_github_map_teams_key) | **post** /auth/github/map/teams/{key} | Read/write/delete a single teams mapping
[**post_auth_github_map_users_key**](AuthApi.md#post_auth_github_map_users_key) | **post** /auth/github/map/users/{key} | Read/write/delete a single users mapping
[**post_auth_github_mfa_config**](AuthApi.md#post_auth_github_mfa_config) | **post** /auth/github/mfa_config | Configure multi factor backend.
[**post_auth_jwt_config**](AuthApi.md#post_auth_jwt_config) | **post** /auth/jwt/config | Configure the JWT authentication backend.
[**post_auth_jwt_login**](AuthApi.md#post_auth_jwt_login) | **post** /auth/jwt/login | Authenticates to Vault using a JWT (or OIDC) token.
[**post_auth_jwt_oidc_auth_url**](AuthApi.md#post_auth_jwt_oidc_auth_url) | **post** /auth/jwt/oidc/auth_url | Request an authorization URL to start an OIDC login flow.
[**post_auth_jwt_oidc_callback**](AuthApi.md#post_auth_jwt_oidc_callback) | **post** /auth/jwt/oidc/callback | Callback endpoint to handle form_posts.
[**post_auth_jwt_role_name**](AuthApi.md#post_auth_jwt_role_name) | **post** /auth/jwt/role/{name} | Register an role with the backend.
[**post_auth_kubernetes_config**](AuthApi.md#post_auth_kubernetes_config) | **post** /auth/kubernetes/config | Configures the JWT Public Key and Kubernetes API information.
[**post_auth_kubernetes_login**](AuthApi.md#post_auth_kubernetes_login) | **post** /auth/kubernetes/login | Authenticates Kubernetes service accounts with Vault.
[**post_auth_kubernetes_role_name**](AuthApi.md#post_auth_kubernetes_role_name) | **post** /auth/kubernetes/role/{name} | Register an role with the backend.
[**post_auth_ldap_config**](AuthApi.md#post_auth_ldap_config) | **post** /auth/ldap/config | Configure the LDAP server to connect to, along with its options.
[**post_auth_ldap_duo_access**](AuthApi.md#post_auth_ldap_duo_access) | **post** /auth/ldap/duo/access | Configure the access keys and host for Duo API connections.
[**post_auth_ldap_duo_config**](AuthApi.md#post_auth_ldap_duo_config) | **post** /auth/ldap/duo/config | Configure Duo second factor behavior.
[**post_auth_ldap_groups_name**](AuthApi.md#post_auth_ldap_groups_name) | **post** /auth/ldap/groups/{name} | Manage additional groups for users allowed to authenticate.
[**post_auth_ldap_login_username**](AuthApi.md#post_auth_ldap_login_username) | **post** /auth/ldap/login/{username} | Log in with a username and password.
[**post_auth_ldap_mfa_config**](AuthApi.md#post_auth_ldap_mfa_config) | **post** /auth/ldap/mfa_config | Configure multi factor backend.
[**post_auth_ldap_users_name**](AuthApi.md#post_auth_ldap_users_name) | **post** /auth/ldap/users/{name} | Manage users allowed to authenticate.
[**post_auth_oidc_config**](AuthApi.md#post_auth_oidc_config) | **post** /auth/oidc/config | Configure the JWT authentication backend.
[**post_auth_oidc_login**](AuthApi.md#post_auth_oidc_login) | **post** /auth/oidc/login | Authenticates to Vault using a JWT (or OIDC) token.
[**post_auth_oidc_oidc_auth_url**](AuthApi.md#post_auth_oidc_oidc_auth_url) | **post** /auth/oidc/oidc/auth_url | Request an authorization URL to start an OIDC login flow.
[**post_auth_oidc_oidc_callback**](AuthApi.md#post_auth_oidc_oidc_callback) | **post** /auth/oidc/oidc/callback | Callback endpoint to handle form_posts.
[**post_auth_oidc_role_name**](AuthApi.md#post_auth_oidc_role_name) | **post** /auth/oidc/role/{name} | Register an role with the backend.
[**post_auth_okta_config**](AuthApi.md#post_auth_okta_config) | **post** /auth/okta/config | This endpoint allows you to configure the Okta and its configuration options.  The Okta organization are the characters at the front of the URL for Okta. Example https://ORG.okta.com
[**post_auth_okta_duo_access**](AuthApi.md#post_auth_okta_duo_access) | **post** /auth/okta/duo/access | Configure the access keys and host for Duo API connections.
[**post_auth_okta_duo_config**](AuthApi.md#post_auth_okta_duo_config) | **post** /auth/okta/duo/config | Configure Duo second factor behavior.
[**post_auth_okta_groups_name**](AuthApi.md#post_auth_okta_groups_name) | **post** /auth/okta/groups/{name} | Manage users allowed to authenticate.
[**post_auth_okta_login_username**](AuthApi.md#post_auth_okta_login_username) | **post** /auth/okta/login/{username} | Log in with a username and password.
[**post_auth_okta_mfa_config**](AuthApi.md#post_auth_okta_mfa_config) | **post** /auth/okta/mfa_config | Configure multi factor backend.
[**post_auth_okta_users_name**](AuthApi.md#post_auth_okta_users_name) | **post** /auth/okta/users/{name} | Manage additional groups for users allowed to authenticate.
[**post_auth_radius_config**](AuthApi.md#post_auth_radius_config) | **post** /auth/radius/config | Configure the RADIUS server to connect to, along with its options.
[**post_auth_radius_duo_access**](AuthApi.md#post_auth_radius_duo_access) | **post** /auth/radius/duo/access | Configure the access keys and host for Duo API connections.
[**post_auth_radius_duo_config**](AuthApi.md#post_auth_radius_duo_config) | **post** /auth/radius/duo/config | Configure Duo second factor behavior.
[**post_auth_radius_login**](AuthApi.md#post_auth_radius_login) | **post** /auth/radius/login | Log in with a username and password.
[**post_auth_radius_login_urlusername**](AuthApi.md#post_auth_radius_login_urlusername) | **post** /auth/radius/login/{urlusername} | Log in with a username and password.
[**post_auth_radius_mfa_config**](AuthApi.md#post_auth_radius_mfa_config) | **post** /auth/radius/mfa_config | Configure multi factor backend.
[**post_auth_radius_users_name**](AuthApi.md#post_auth_radius_users_name) | **post** /auth/radius/users/{name} | Manage users allowed to authenticate.
[**post_auth_token_create**](AuthApi.md#post_auth_token_create) | **post** /auth/token/create | The token create path is used to create new tokens.
[**post_auth_token_create_orphan**](AuthApi.md#post_auth_token_create_orphan) | **post** /auth/token/create-orphan | The token create path is used to create new orphan tokens.
[**post_auth_token_create_role_name**](AuthApi.md#post_auth_token_create_role_name) | **post** /auth/token/create/{role_name} | This token create path is used to create new tokens adhering to the given role.
[**post_auth_token_lookup**](AuthApi.md#post_auth_token_lookup) | **post** /auth/token/lookup | This endpoint will lookup a token and its properties.
[**post_auth_token_lookup_accessor**](AuthApi.md#post_auth_token_lookup_accessor) | **post** /auth/token/lookup-accessor | This endpoint will lookup a token associated with the given accessor and its properties. Response will not contain the token ID.
[**post_auth_token_lookup_self**](AuthApi.md#post_auth_token_lookup_self) | **post** /auth/token/lookup-self | This endpoint will lookup a token and its properties.
[**post_auth_token_renew**](AuthApi.md#post_auth_token_renew) | **post** /auth/token/renew | This endpoint will renew the given token and prevent expiration.
[**post_auth_token_renew_accessor**](AuthApi.md#post_auth_token_renew_accessor) | **post** /auth/token/renew-accessor | This endpoint will renew a token associated with the given accessor and its properties. Response will not contain the token ID.
[**post_auth_token_renew_self**](AuthApi.md#post_auth_token_renew_self) | **post** /auth/token/renew-self | This endpoint will renew the token used to call it and prevent expiration.
[**post_auth_token_revoke**](AuthApi.md#post_auth_token_revoke) | **post** /auth/token/revoke | This endpoint will delete the given token and all of its child tokens.
[**post_auth_token_revoke_accessor**](AuthApi.md#post_auth_token_revoke_accessor) | **post** /auth/token/revoke-accessor | This endpoint will delete the token associated with the accessor and all of its child tokens.
[**post_auth_token_revoke_orphan**](AuthApi.md#post_auth_token_revoke_orphan) | **post** /auth/token/revoke-orphan | This endpoint will delete the token and orphan its child tokens.
[**post_auth_token_revoke_self**](AuthApi.md#post_auth_token_revoke_self) | **post** /auth/token/revoke-self | This endpoint will delete the token used to call it and all of its child tokens.
[**post_auth_token_roles_role_name**](AuthApi.md#post_auth_token_roles_role_name) | **post** /auth/token/roles/{role_name} | 
[**post_auth_token_tidy**](AuthApi.md#post_auth_token_tidy) | **post** /auth/token/tidy | This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.
[**post_auth_userpass_duo_access**](AuthApi.md#post_auth_userpass_duo_access) | **post** /auth/userpass/duo/access | Configure the access keys and host for Duo API connections.
[**post_auth_userpass_duo_config**](AuthApi.md#post_auth_userpass_duo_config) | **post** /auth/userpass/duo/config | Configure Duo second factor behavior.
[**post_auth_userpass_login_username**](AuthApi.md#post_auth_userpass_login_username) | **post** /auth/userpass/login/{username} | Log in with a username and password.
[**post_auth_userpass_mfa_config**](AuthApi.md#post_auth_userpass_mfa_config) | **post** /auth/userpass/mfa_config | Configure multi factor backend.
[**post_auth_userpass_users_username**](AuthApi.md#post_auth_userpass_users_username) | **post** /auth/userpass/users/{username} | Manage users allowed to authenticate.
[**post_auth_userpass_users_username_password**](AuthApi.md#post_auth_userpass_users_username_password) | **post** /auth/userpass/users/{username}/password | Reset user's password.
[**post_auth_userpass_users_username_policies**](AuthApi.md#post_auth_userpass_users_username_policies) | **post** /auth/userpass/users/{username}/policies | Update the policies associated with the username.



## delete_auth_alicloud_role_role

> delete_auth_alicloud_role_role(role)
Create a role and associate policies to it.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | The name of the role as it should appear in Vault. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name

> delete_auth_approle_role_role_name(role_name)
Register an role with the backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_bind_secret_id

> delete_auth_approle_role_role_name_bind_secret_id(role_name)
Impose secret_id to be presented during login using this role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_bound_cidr_list

> delete_auth_approle_role_role_name_bound_cidr_list(role_name)
Deprecated: Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_period

> delete_auth_approle_role_role_name_period(role_name)
Updates the value of 'period' on the role

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_policies

> delete_auth_approle_role_role_name_policies(role_name)
Policies of the role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_secret_id_accessor_destroy

> delete_auth_approle_role_role_name_secret_id_accessor_destroy(role_name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_secret_id_bound_cidrs

> delete_auth_approle_role_role_name_secret_id_bound_cidrs(role_name)
Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_secret_id_destroy

> delete_auth_approle_role_role_name_secret_id_destroy(role_name)
Invalidate an issued secret_id

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_secret_id_num_uses

> delete_auth_approle_role_role_name_secret_id_num_uses(role_name)
Use limit of the SecretID generated against the role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_secret_id_ttl

> delete_auth_approle_role_role_name_secret_id_ttl(role_name)
Duration in seconds, representing the lifetime of the SecretIDs that are generated against the role using 'role/<role_name>/secret-id' or 'role/<role_name>/custom-secret-id' endpoints.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_token_bound_cidrs

> delete_auth_approle_role_role_name_token_bound_cidrs(role_name)
Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can use the returned token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_token_max_ttl

> delete_auth_approle_role_role_name_token_max_ttl(role_name)
Duration in seconds, the maximum lifetime of the tokens issued by using the SecretIDs that were generated against this role, after which the tokens are not allowed to be renewed.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_token_num_uses

> delete_auth_approle_role_role_name_token_num_uses(role_name)
Number of times issued tokens can be used

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_approle_role_role_name_token_ttl

> delete_auth_approle_role_role_name_token_ttl(role_name)
Duration in seconds, the lifetime of the token issued by using the SecretID that is generated against this role, before which the token needs to be renewed.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_aws_config_certificate_cert_name

> delete_auth_aws_config_certificate_cert_name(cert_name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**cert_name** | **String** | Name of the certificate. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_aws_config_client

> delete_auth_aws_config_client()


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


## delete_auth_aws_config_sts_account_id

> delete_auth_aws_config_sts_account_id(account_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **String** | AWS account ID to be associated with STS role. If set, Vault will use assumed credentials to verify any login attempts from EC2 instances in this account. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_aws_config_tidy_identity_whitelist

> delete_auth_aws_config_tidy_identity_whitelist()


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


## delete_auth_aws_config_tidy_roletag_blacklist

> delete_auth_aws_config_tidy_roletag_blacklist()


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


## delete_auth_aws_identity_whitelist_instance_id

> delete_auth_aws_identity_whitelist_instance_id(instance_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**instance_id** | **String** | EC2 instance ID. A successful login operation from an EC2 instance gets cached in this whitelist, keyed off of instance ID. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_aws_role_role

> delete_auth_aws_role_role(role)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_aws_roletag_blacklist_role_tag

> delete_auth_aws_roletag_blacklist_role_tag(role_tag)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_tag** | **String** | Role tag to be blacklisted. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_azure_config

> delete_auth_azure_config()
Configures the Azure authentication backend.

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


## delete_auth_azure_role_name

> delete_auth_azure_role_name(name)
Register an role with the backend.

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


## delete_auth_cert_certs_name

> delete_auth_cert_certs_name(name)
Manage trusted certificates used for authentication.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the certificate | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_cert_crls_name

> delete_auth_cert_crls_name(name)
Manage Certificate Revocation Lists checked during authentication.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the certificate | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_gcp_role_name

> delete_auth_gcp_role_name(name)
Create a GCP role with associated policies and required attributes.

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


## delete_auth_github_map_teams_key

> delete_auth_github_map_teams_key(key)
Read/write/delete a single teams mapping

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Key for the teams mapping | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_github_map_users_key

> delete_auth_github_map_users_key(key)
Read/write/delete a single users mapping

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Key for the users mapping | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_jwt_role_name

> delete_auth_jwt_role_name(name)
Delete an existing role.

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


## delete_auth_kubernetes_role_name

> delete_auth_kubernetes_role_name(name)
Register an role with the backend.

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


## delete_auth_ldap_groups_name

> delete_auth_ldap_groups_name(name)
Manage additional groups for users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the LDAP group. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_ldap_users_name

> delete_auth_ldap_users_name(name)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the LDAP user. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_oidc_role_name

> delete_auth_oidc_role_name(name)
Delete an existing role.

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


## delete_auth_okta_groups_name

> delete_auth_okta_groups_name(name)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the Okta group. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_okta_users_name

> delete_auth_okta_users_name(name)
Manage additional groups for users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the user. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_radius_users_name

> delete_auth_radius_users_name(name)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the RADIUS user. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_token_roles_role_name

> delete_auth_token_roles_role_name(role_name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## delete_auth_userpass_users_username

> delete_auth_userpass_users_username(username)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**username** | **String** | Username for this user. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_alicloud_role

> get_auth_alicloud_role(list)
Lists all the roles that are registered with Vault.

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


## get_auth_alicloud_role_role

> get_auth_alicloud_role_role(role)
Create a role and associate policies to it.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | The name of the role as it should appear in Vault. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_alicloud_roles

> get_auth_alicloud_roles(list)
Lists all the roles that are registered with Vault.

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


## get_auth_approle_role

> get_auth_approle_role(list)
Lists all the roles registered with the backend.

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


## get_auth_approle_role_role_name

> get_auth_approle_role_role_name(role_name)
Register an role with the backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_bind_secret_id

> get_auth_approle_role_role_name_bind_secret_id(role_name)
Impose secret_id to be presented during login using this role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_bound_cidr_list

> get_auth_approle_role_role_name_bound_cidr_list(role_name)
Deprecated: Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_local_secret_ids

> get_auth_approle_role_role_name_local_secret_ids(role_name)
Enables cluster local secret IDs

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_period

> get_auth_approle_role_role_name_period(role_name)
Updates the value of 'period' on the role

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_policies

> get_auth_approle_role_role_name_policies(role_name)
Policies of the role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_role_id

> get_auth_approle_role_role_name_role_id(role_name)
Returns the 'role_id' of the role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_secret_id

> get_auth_approle_role_role_name_secret_id(role_name, list)
Generate a SecretID against this role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**list** | Option<**String**> | Return a list if `true` |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_secret_id_bound_cidrs

> get_auth_approle_role_role_name_secret_id_bound_cidrs(role_name)
Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_secret_id_num_uses

> get_auth_approle_role_role_name_secret_id_num_uses(role_name)
Use limit of the SecretID generated against the role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_secret_id_ttl

> get_auth_approle_role_role_name_secret_id_ttl(role_name)
Duration in seconds, representing the lifetime of the SecretIDs that are generated against the role using 'role/<role_name>/secret-id' or 'role/<role_name>/custom-secret-id' endpoints.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_token_bound_cidrs

> get_auth_approle_role_role_name_token_bound_cidrs(role_name)
Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can use the returned token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_token_max_ttl

> get_auth_approle_role_role_name_token_max_ttl(role_name)
Duration in seconds, the maximum lifetime of the tokens issued by using the SecretIDs that were generated against this role, after which the tokens are not allowed to be renewed.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_token_num_uses

> get_auth_approle_role_role_name_token_num_uses(role_name)
Number of times issued tokens can be used

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_approle_role_role_name_token_ttl

> get_auth_approle_role_role_name_token_ttl(role_name)
Duration in seconds, the lifetime of the token issued by using the SecretID that is generated against this role, before which the token needs to be renewed.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_aws_config_certificate_cert_name

> get_auth_aws_config_certificate_cert_name(cert_name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**cert_name** | **String** | Name of the certificate. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_aws_config_certificates

> get_auth_aws_config_certificates(list)


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


## get_auth_aws_config_client

> get_auth_aws_config_client()


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


## get_auth_aws_config_identity

> get_auth_aws_config_identity()


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


## get_auth_aws_config_sts

> get_auth_aws_config_sts(list)


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


## get_auth_aws_config_sts_account_id

> get_auth_aws_config_sts_account_id(account_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **String** | AWS account ID to be associated with STS role. If set, Vault will use assumed credentials to verify any login attempts from EC2 instances in this account. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_aws_config_tidy_identity_whitelist

> get_auth_aws_config_tidy_identity_whitelist()


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


## get_auth_aws_config_tidy_roletag_blacklist

> get_auth_aws_config_tidy_roletag_blacklist()


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


## get_auth_aws_identity_whitelist

> get_auth_aws_identity_whitelist(list)


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


## get_auth_aws_identity_whitelist_instance_id

> get_auth_aws_identity_whitelist_instance_id(instance_id)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**instance_id** | **String** | EC2 instance ID. A successful login operation from an EC2 instance gets cached in this whitelist, keyed off of instance ID. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_aws_role

> get_auth_aws_role(list)


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


## get_auth_aws_role_role

> get_auth_aws_role_role(role)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | Name of the role. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_aws_roles

> get_auth_aws_roles(list)


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


## get_auth_aws_roletag_blacklist

> get_auth_aws_roletag_blacklist(list)


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


## get_auth_aws_roletag_blacklist_role_tag

> get_auth_aws_roletag_blacklist_role_tag(role_tag)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_tag** | **String** | Role tag to be blacklisted. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_azure_config

> get_auth_azure_config()
Configures the Azure authentication backend.

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


## get_auth_azure_role

> get_auth_azure_role(list)
Lists all the roles registered with the backend.

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


## get_auth_azure_role_name

> get_auth_azure_role_name(name)
Register an role with the backend.

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


## get_auth_cert_certs

> get_auth_cert_certs(list)
Manage trusted certificates used for authentication.

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


## get_auth_cert_certs_name

> get_auth_cert_certs_name(name)
Manage trusted certificates used for authentication.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the certificate | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_cert_crls_name

> get_auth_cert_crls_name(name)
Manage Certificate Revocation Lists checked during authentication.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the certificate | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_gcp_config

> get_auth_gcp_config()
Configure credentials used to query the GCP IAM API to verify authenticating service accounts

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


## get_auth_gcp_role

> get_auth_gcp_role(list)
Lists all the roles that are registered with Vault.

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


## get_auth_gcp_role_name

> get_auth_gcp_role_name(name)
Create a GCP role with associated policies and required attributes.

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


## get_auth_gcp_roles

> get_auth_gcp_roles(list)
Lists all the roles that are registered with Vault.

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


## get_auth_github_config

> get_auth_github_config()


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


## get_auth_github_duo_config

> get_auth_github_duo_config()
Configure Duo second factor behavior.

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


## get_auth_github_map_teams

> get_auth_github_map_teams(list)
Read mappings for teams

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


## get_auth_github_map_teams_key

> get_auth_github_map_teams_key(key)
Read/write/delete a single teams mapping

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Key for the teams mapping | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_github_map_users

> get_auth_github_map_users(list)
Read mappings for users

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


## get_auth_github_map_users_key

> get_auth_github_map_users_key(key)
Read/write/delete a single users mapping

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Key for the users mapping | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_github_mfa_config

> get_auth_github_mfa_config()
Configure multi factor backend.

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


## get_auth_jwt_config

> get_auth_jwt_config()
Read the current JWT authentication backend configuration.

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


## get_auth_jwt_oidc_callback

> get_auth_jwt_oidc_callback()
Callback endpoint to complete an OIDC login.

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


## get_auth_jwt_role

> get_auth_jwt_role(list)
Lists all the roles registered with the backend.

The list will contain the names of the roles.

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


## get_auth_jwt_role_name

> get_auth_jwt_role_name(name)
Read an existing role.

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


## get_auth_kubernetes_config

> get_auth_kubernetes_config()
Configures the JWT Public Key and Kubernetes API information.

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


## get_auth_kubernetes_role

> get_auth_kubernetes_role(list)
Lists all the roles registered with the backend.

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


## get_auth_kubernetes_role_name

> get_auth_kubernetes_role_name(name)
Register an role with the backend.

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


## get_auth_ldap_config

> get_auth_ldap_config()
Configure the LDAP server to connect to, along with its options.

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


## get_auth_ldap_duo_config

> get_auth_ldap_duo_config()
Configure Duo second factor behavior.

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


## get_auth_ldap_groups

> get_auth_ldap_groups(list)
Manage additional groups for users allowed to authenticate.

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


## get_auth_ldap_groups_name

> get_auth_ldap_groups_name(name)
Manage additional groups for users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the LDAP group. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_ldap_mfa_config

> get_auth_ldap_mfa_config()
Configure multi factor backend.

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


## get_auth_ldap_users

> get_auth_ldap_users(list)
Manage users allowed to authenticate.

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


## get_auth_ldap_users_name

> get_auth_ldap_users_name(name)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the LDAP user. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_oidc_config

> get_auth_oidc_config()
Read the current JWT authentication backend configuration.

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


## get_auth_oidc_oidc_callback

> get_auth_oidc_oidc_callback()
Callback endpoint to complete an OIDC login.

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


## get_auth_oidc_role

> get_auth_oidc_role(list)
Lists all the roles registered with the backend.

The list will contain the names of the roles.

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


## get_auth_oidc_role_name

> get_auth_oidc_role_name(name)
Read an existing role.

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


## get_auth_okta_config

> get_auth_okta_config()
This endpoint allows you to configure the Okta and its configuration options.  The Okta organization are the characters at the front of the URL for Okta. Example https://ORG.okta.com

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


## get_auth_okta_duo_config

> get_auth_okta_duo_config()
Configure Duo second factor behavior.

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


## get_auth_okta_groups

> get_auth_okta_groups(list)
Manage users allowed to authenticate.

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


## get_auth_okta_groups_name

> get_auth_okta_groups_name(name)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the Okta group. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_okta_mfa_config

> get_auth_okta_mfa_config()
Configure multi factor backend.

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


## get_auth_okta_users

> get_auth_okta_users(list)
Manage additional groups for users allowed to authenticate.

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


## get_auth_okta_users_name

> get_auth_okta_users_name(name)
Manage additional groups for users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the user. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_radius_config

> get_auth_radius_config()
Configure the RADIUS server to connect to, along with its options.

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


## get_auth_radius_duo_config

> get_auth_radius_duo_config()
Configure Duo second factor behavior.

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


## get_auth_radius_mfa_config

> get_auth_radius_mfa_config()
Configure multi factor backend.

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


## get_auth_radius_users

> get_auth_radius_users(list)
Manage users allowed to authenticate.

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


## get_auth_radius_users_name

> get_auth_radius_users_name(name)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the RADIUS user. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_token_accessors

> get_auth_token_accessors(list)
List token accessors, which can then be be used to iterate and discover their properties or revoke them. Because this can be used to cause a denial of service, this endpoint requires 'sudo' capability in addition to 'list'.

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


## get_auth_token_lookup

> get_auth_token_lookup()
This endpoint will lookup a token and its properties.

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


## get_auth_token_lookup_self

> get_auth_token_lookup_self()
This endpoint will lookup a token and its properties.

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


## get_auth_token_roles

> get_auth_token_roles(list)
This endpoint lists configured roles.

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


## get_auth_token_roles_role_name

> get_auth_token_roles_role_name(role_name)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_auth_userpass_duo_config

> get_auth_userpass_duo_config()
Configure Duo second factor behavior.

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


## get_auth_userpass_mfa_config

> get_auth_userpass_mfa_config()
Configure multi factor backend.

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


## get_auth_userpass_users

> get_auth_userpass_users(list)
Manage users allowed to authenticate.

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


## get_auth_userpass_users_username

> get_auth_userpass_users_username(username)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**username** | **String** | Username for this user. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_alicloud_login

> post_auth_alicloud_login(inline_object8)
Authenticates an RAM entity with Vault.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object8** | Option<[**InlineObject8**](InlineObject8.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_alicloud_role_role

> post_auth_alicloud_role_role(role, inline_object9)
Create a role and associate policies to it.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | The name of the role as it should appear in Vault. | [required] |
**inline_object9** | Option<[**InlineObject9**](InlineObject9.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_login

> post_auth_approle_login(inline_object10)
Issue a token based on the credentials supplied

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object10** | Option<[**InlineObject10**](InlineObject10.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name

> post_auth_approle_role_role_name(role_name, inline_object11)
Register an role with the backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object11** | Option<[**InlineObject11**](InlineObject11.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_bind_secret_id

> post_auth_approle_role_role_name_bind_secret_id(role_name, inline_object12)
Impose secret_id to be presented during login using this role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object12** | Option<[**InlineObject12**](InlineObject12.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_bound_cidr_list

> post_auth_approle_role_role_name_bound_cidr_list(role_name, inline_object13)
Deprecated: Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object13** | Option<[**InlineObject13**](InlineObject13.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_custom_secret_id

> post_auth_approle_role_role_name_custom_secret_id(role_name, inline_object14)
Assign a SecretID of choice against the role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object14** | Option<[**InlineObject14**](InlineObject14.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_period

> post_auth_approle_role_role_name_period(role_name, inline_object15)
Updates the value of 'period' on the role

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object15** | Option<[**InlineObject15**](InlineObject15.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_policies

> post_auth_approle_role_role_name_policies(role_name, inline_object16)
Policies of the role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object16** | Option<[**InlineObject16**](InlineObject16.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_role_id

> post_auth_approle_role_role_name_role_id(role_name, inline_object17)
Returns the 'role_id' of the role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object17** | Option<[**InlineObject17**](InlineObject17.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_secret_id

> post_auth_approle_role_role_name_secret_id(role_name, inline_object18)
Generate a SecretID against this role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object18** | Option<[**InlineObject18**](InlineObject18.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_secret_id_accessor_destroy

> post_auth_approle_role_role_name_secret_id_accessor_destroy(role_name, inline_object19)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object19** | Option<[**InlineObject19**](InlineObject19.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_secret_id_accessor_lookup

> post_auth_approle_role_role_name_secret_id_accessor_lookup(role_name, inline_object20)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object20** | Option<[**InlineObject20**](InlineObject20.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_secret_id_bound_cidrs

> post_auth_approle_role_role_name_secret_id_bound_cidrs(role_name, inline_object21)
Comma separated list of CIDR blocks, if set, specifies blocks of IP addresses which can perform the login operation

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object21** | Option<[**InlineObject21**](InlineObject21.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_secret_id_destroy

> post_auth_approle_role_role_name_secret_id_destroy(role_name, inline_object24)
Invalidate an issued secret_id

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object24** | Option<[**InlineObject24**](InlineObject24.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_secret_id_lookup

> post_auth_approle_role_role_name_secret_id_lookup(role_name, inline_object25)
Read the properties of an issued secret_id

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object25** | Option<[**InlineObject25**](InlineObject25.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_secret_id_num_uses

> post_auth_approle_role_role_name_secret_id_num_uses(role_name, inline_object22)
Use limit of the SecretID generated against the role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object22** | Option<[**InlineObject22**](InlineObject22.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_secret_id_ttl

> post_auth_approle_role_role_name_secret_id_ttl(role_name, inline_object23)
Duration in seconds, representing the lifetime of the SecretIDs that are generated against the role using 'role/<role_name>/secret-id' or 'role/<role_name>/custom-secret-id' endpoints.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object23** | Option<[**InlineObject23**](InlineObject23.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_token_bound_cidrs

> post_auth_approle_role_role_name_token_bound_cidrs(role_name, inline_object26)
Comma separated string or list of CIDR blocks. If set, specifies the blocks of IP addresses which can use the returned token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object26** | Option<[**InlineObject26**](InlineObject26.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_token_max_ttl

> post_auth_approle_role_role_name_token_max_ttl(role_name, inline_object27)
Duration in seconds, the maximum lifetime of the tokens issued by using the SecretIDs that were generated against this role, after which the tokens are not allowed to be renewed.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object27** | Option<[**InlineObject27**](InlineObject27.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_token_num_uses

> post_auth_approle_role_role_name_token_num_uses(role_name, inline_object28)
Number of times issued tokens can be used

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object28** | Option<[**InlineObject28**](InlineObject28.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_role_role_name_token_ttl

> post_auth_approle_role_role_name_token_ttl(role_name, inline_object29)
Duration in seconds, the lifetime of the token issued by using the SecretID that is generated against this role, before which the token needs to be renewed.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role. | [required] |
**inline_object29** | Option<[**InlineObject29**](InlineObject29.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_approle_tidy_secret_id

> post_auth_approle_tidy_secret_id()
Trigger the clean-up of expired SecretID entries.

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


## post_auth_aws_config_certificate_cert_name

> post_auth_aws_config_certificate_cert_name(cert_name, inline_object30)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**cert_name** | **String** | Name of the certificate. | [required] |
**inline_object30** | Option<[**InlineObject30**](InlineObject30.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_config_client

> post_auth_aws_config_client(inline_object31)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object31** | Option<[**InlineObject31**](InlineObject31.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_config_identity

> post_auth_aws_config_identity(inline_object32)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object32** | Option<[**InlineObject32**](InlineObject32.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_config_rotate_root

> post_auth_aws_config_rotate_root()


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


## post_auth_aws_config_sts_account_id

> post_auth_aws_config_sts_account_id(account_id, inline_object33)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**account_id** | **String** | AWS account ID to be associated with STS role. If set, Vault will use assumed credentials to verify any login attempts from EC2 instances in this account. | [required] |
**inline_object33** | Option<[**InlineObject33**](InlineObject33.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_config_tidy_identity_whitelist

> post_auth_aws_config_tidy_identity_whitelist(inline_object34)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object34** | Option<[**InlineObject34**](InlineObject34.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_config_tidy_roletag_blacklist

> post_auth_aws_config_tidy_roletag_blacklist(inline_object35)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object35** | Option<[**InlineObject35**](InlineObject35.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_login

> post_auth_aws_login(inline_object36)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object36** | Option<[**InlineObject36**](InlineObject36.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_role_role

> post_auth_aws_role_role(role, inline_object37)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | Name of the role. | [required] |
**inline_object37** | Option<[**InlineObject37**](InlineObject37.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_role_role_tag

> post_auth_aws_role_role_tag(role, inline_object38)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role** | **String** | Name of the role. | [required] |
**inline_object38** | Option<[**InlineObject38**](InlineObject38.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_roletag_blacklist_role_tag

> post_auth_aws_roletag_blacklist_role_tag(role_tag)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_tag** | **String** | Role tag to be blacklisted. The tag can be supplied as-is. In order to avoid any encoding problems, it can be base64 encoded. | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_tidy_identity_whitelist

> post_auth_aws_tidy_identity_whitelist(inline_object39)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object39** | Option<[**InlineObject39**](InlineObject39.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_aws_tidy_roletag_blacklist

> post_auth_aws_tidy_roletag_blacklist(inline_object40)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object40** | Option<[**InlineObject40**](InlineObject40.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_azure_config

> post_auth_azure_config(inline_object41)
Configures the Azure authentication backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object41** | Option<[**InlineObject41**](InlineObject41.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_azure_login

> post_auth_azure_login(inline_object42)
Authenticates Azure Managed Service Identities with Vault.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object42** | Option<[**InlineObject42**](InlineObject42.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_azure_role_name

> post_auth_azure_role_name(name, inline_object43)
Register an role with the backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object43** | Option<[**InlineObject43**](InlineObject43.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_cert_certs_name

> post_auth_cert_certs_name(name, inline_object44)
Manage trusted certificates used for authentication.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the certificate | [required] |
**inline_object44** | Option<[**InlineObject44**](InlineObject44.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_cert_config

> post_auth_cert_config(inline_object45)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object45** | Option<[**InlineObject45**](InlineObject45.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_cert_crls_name

> post_auth_cert_crls_name(name, inline_object46)
Manage Certificate Revocation Lists checked during authentication.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | The name of the certificate | [required] |
**inline_object46** | Option<[**InlineObject46**](InlineObject46.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_cert_login

> post_auth_cert_login(inline_object47)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object47** | Option<[**InlineObject47**](InlineObject47.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_gcp_config

> post_auth_gcp_config(inline_object48)
Configure credentials used to query the GCP IAM API to verify authenticating service accounts

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object48** | Option<[**InlineObject48**](InlineObject48.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_gcp_login

> post_auth_gcp_login(inline_object49)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object49** | Option<[**InlineObject49**](InlineObject49.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_gcp_role_name

> post_auth_gcp_role_name(name, inline_object50)
Create a GCP role with associated policies and required attributes.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object50** | Option<[**InlineObject50**](InlineObject50.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_gcp_role_name_labels

> post_auth_gcp_role_name_labels(name, inline_object51)
Add or remove labels for an existing 'gce' role

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object51** | Option<[**InlineObject51**](InlineObject51.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_gcp_role_name_service_accounts

> post_auth_gcp_role_name_service_accounts(name, inline_object52)
Add or remove service accounts for an existing `iam` role

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object52** | Option<[**InlineObject52**](InlineObject52.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_github_config

> post_auth_github_config(inline_object53)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object53** | Option<[**InlineObject53**](InlineObject53.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_github_duo_access

> post_auth_github_duo_access(inline_object54)
Configure the access keys and host for Duo API connections.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object54** | Option<[**InlineObject54**](InlineObject54.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_github_duo_config

> post_auth_github_duo_config(inline_object55)
Configure Duo second factor behavior.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object55** | Option<[**InlineObject55**](InlineObject55.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_github_login

> post_auth_github_login(inline_object56)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object56** | Option<[**InlineObject56**](InlineObject56.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_github_map_teams_key

> post_auth_github_map_teams_key(key, inline_object57)
Read/write/delete a single teams mapping

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Key for the teams mapping | [required] |
**inline_object57** | Option<[**InlineObject57**](InlineObject57.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_github_map_users_key

> post_auth_github_map_users_key(key, inline_object58)
Read/write/delete a single users mapping

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | Key for the users mapping | [required] |
**inline_object58** | Option<[**InlineObject58**](InlineObject58.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_github_mfa_config

> post_auth_github_mfa_config(inline_object59)
Configure multi factor backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object59** | Option<[**InlineObject59**](InlineObject59.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_jwt_config

> post_auth_jwt_config(inline_object60)
Configure the JWT authentication backend.

The JWT authentication backend validates JWTs (or OIDC) using the configured credentials. If using OIDC Discovery, the URL must be provided, along with (optionally) the CA cert to use for the connection. If performing JWT validation locally, a set of public keys must be provided.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object60** | Option<[**InlineObject60**](InlineObject60.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_jwt_login

> post_auth_jwt_login(inline_object61)
Authenticates to Vault using a JWT (or OIDC) token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object61** | Option<[**InlineObject61**](InlineObject61.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_jwt_oidc_auth_url

> post_auth_jwt_oidc_auth_url(inline_object62)
Request an authorization URL to start an OIDC login flow.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object62** | Option<[**InlineObject62**](InlineObject62.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_jwt_oidc_callback

> post_auth_jwt_oidc_callback(inline_object63)
Callback endpoint to handle form_posts.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object63** | Option<[**InlineObject63**](InlineObject63.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_jwt_role_name

> post_auth_jwt_role_name(name, inline_object64)
Register an role with the backend.

A role is required to authenticate with this backend. The role binds   JWT token information with token policies and settings.   The bindings, token polices and token settings can all be configured   using this endpoint

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object64** | Option<[**InlineObject64**](InlineObject64.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_kubernetes_config

> post_auth_kubernetes_config(inline_object65)
Configures the JWT Public Key and Kubernetes API information.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object65** | Option<[**InlineObject65**](InlineObject65.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_kubernetes_login

> post_auth_kubernetes_login(inline_object66)
Authenticates Kubernetes service accounts with Vault.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object66** | Option<[**InlineObject66**](InlineObject66.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_kubernetes_role_name

> post_auth_kubernetes_role_name(name, inline_object67)
Register an role with the backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object67** | Option<[**InlineObject67**](InlineObject67.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_ldap_config

> post_auth_ldap_config(inline_object68)
Configure the LDAP server to connect to, along with its options.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object68** | Option<[**InlineObject68**](InlineObject68.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_ldap_duo_access

> post_auth_ldap_duo_access(inline_object69)
Configure the access keys and host for Duo API connections.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object69** | Option<[**InlineObject69**](InlineObject69.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_ldap_duo_config

> post_auth_ldap_duo_config(inline_object70)
Configure Duo second factor behavior.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object70** | Option<[**InlineObject70**](InlineObject70.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_ldap_groups_name

> post_auth_ldap_groups_name(name, inline_object71)
Manage additional groups for users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the LDAP group. | [required] |
**inline_object71** | Option<[**InlineObject71**](InlineObject71.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_ldap_login_username

> post_auth_ldap_login_username(username, inline_object72)
Log in with a username and password.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**username** | **String** | DN (distinguished name) to be used for login. | [required] |
**inline_object72** | Option<[**InlineObject72**](InlineObject72.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_ldap_mfa_config

> post_auth_ldap_mfa_config(inline_object73)
Configure multi factor backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object73** | Option<[**InlineObject73**](InlineObject73.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_ldap_users_name

> post_auth_ldap_users_name(name, inline_object74)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the LDAP user. | [required] |
**inline_object74** | Option<[**InlineObject74**](InlineObject74.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_oidc_config

> post_auth_oidc_config(inline_object75)
Configure the JWT authentication backend.

The JWT authentication backend validates JWTs (or OIDC) using the configured credentials. If using OIDC Discovery, the URL must be provided, along with (optionally) the CA cert to use for the connection. If performing JWT validation locally, a set of public keys must be provided.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object75** | Option<[**InlineObject75**](InlineObject75.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_oidc_login

> post_auth_oidc_login(inline_object76)
Authenticates to Vault using a JWT (or OIDC) token.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object76** | Option<[**InlineObject76**](InlineObject76.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_oidc_oidc_auth_url

> post_auth_oidc_oidc_auth_url(inline_object77)
Request an authorization URL to start an OIDC login flow.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object77** | Option<[**InlineObject77**](InlineObject77.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_oidc_oidc_callback

> post_auth_oidc_oidc_callback(inline_object78)
Callback endpoint to handle form_posts.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object78** | Option<[**InlineObject78**](InlineObject78.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_oidc_role_name

> post_auth_oidc_role_name(name, inline_object79)
Register an role with the backend.

A role is required to authenticate with this backend. The role binds   JWT token information with token policies and settings.   The bindings, token polices and token settings can all be configured   using this endpoint

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the role. | [required] |
**inline_object79** | Option<[**InlineObject79**](InlineObject79.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_okta_config

> post_auth_okta_config(inline_object80)
This endpoint allows you to configure the Okta and its configuration options.  The Okta organization are the characters at the front of the URL for Okta. Example https://ORG.okta.com

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object80** | Option<[**InlineObject80**](InlineObject80.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_okta_duo_access

> post_auth_okta_duo_access(inline_object81)
Configure the access keys and host for Duo API connections.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object81** | Option<[**InlineObject81**](InlineObject81.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_okta_duo_config

> post_auth_okta_duo_config(inline_object82)
Configure Duo second factor behavior.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object82** | Option<[**InlineObject82**](InlineObject82.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_okta_groups_name

> post_auth_okta_groups_name(name, inline_object83)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the Okta group. | [required] |
**inline_object83** | Option<[**InlineObject83**](InlineObject83.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_okta_login_username

> post_auth_okta_login_username(username, inline_object84)
Log in with a username and password.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**username** | **String** | Username to be used for login. | [required] |
**inline_object84** | Option<[**InlineObject84**](InlineObject84.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_okta_mfa_config

> post_auth_okta_mfa_config(inline_object85)
Configure multi factor backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object85** | Option<[**InlineObject85**](InlineObject85.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_okta_users_name

> post_auth_okta_users_name(name, inline_object86)
Manage additional groups for users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the user. | [required] |
**inline_object86** | Option<[**InlineObject86**](InlineObject86.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_radius_config

> post_auth_radius_config(inline_object87)
Configure the RADIUS server to connect to, along with its options.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object87** | Option<[**InlineObject87**](InlineObject87.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_radius_duo_access

> post_auth_radius_duo_access(inline_object88)
Configure the access keys and host for Duo API connections.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object88** | Option<[**InlineObject88**](InlineObject88.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_radius_duo_config

> post_auth_radius_duo_config(inline_object89)
Configure Duo second factor behavior.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object89** | Option<[**InlineObject89**](InlineObject89.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_radius_login

> post_auth_radius_login(inline_object90)
Log in with a username and password.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object90** | Option<[**InlineObject90**](InlineObject90.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_radius_login_urlusername

> post_auth_radius_login_urlusername(urlusername, inline_object91)
Log in with a username and password.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**urlusername** | **String** | Username to be used for login. (URL parameter) | [required] |
**inline_object91** | Option<[**InlineObject91**](InlineObject91.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_radius_mfa_config

> post_auth_radius_mfa_config(inline_object92)
Configure multi factor backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object92** | Option<[**InlineObject92**](InlineObject92.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_radius_users_name

> post_auth_radius_users_name(name, inline_object93)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Name of the RADIUS user. | [required] |
**inline_object93** | Option<[**InlineObject93**](InlineObject93.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_create

> post_auth_token_create()
The token create path is used to create new tokens.

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


## post_auth_token_create_orphan

> post_auth_token_create_orphan()
The token create path is used to create new orphan tokens.

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


## post_auth_token_create_role_name

> post_auth_token_create_role_name(role_name)
This token create path is used to create new tokens adhering to the given role.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_lookup

> post_auth_token_lookup(inline_object94)
This endpoint will lookup a token and its properties.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object94** | Option<[**InlineObject94**](InlineObject94.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_lookup_accessor

> post_auth_token_lookup_accessor(inline_object95)
This endpoint will lookup a token associated with the given accessor and its properties. Response will not contain the token ID.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object95** | Option<[**InlineObject95**](InlineObject95.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_lookup_self

> post_auth_token_lookup_self(inline_object96)
This endpoint will lookup a token and its properties.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object96** | Option<[**InlineObject96**](InlineObject96.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_renew

> post_auth_token_renew(inline_object97)
This endpoint will renew the given token and prevent expiration.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object97** | Option<[**InlineObject97**](InlineObject97.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_renew_accessor

> post_auth_token_renew_accessor(inline_object98)
This endpoint will renew a token associated with the given accessor and its properties. Response will not contain the token ID.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object98** | Option<[**InlineObject98**](InlineObject98.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_renew_self

> post_auth_token_renew_self(inline_object99)
This endpoint will renew the token used to call it and prevent expiration.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object99** | Option<[**InlineObject99**](InlineObject99.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_revoke

> post_auth_token_revoke(inline_object100)
This endpoint will delete the given token and all of its child tokens.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object100** | Option<[**InlineObject100**](InlineObject100.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_revoke_accessor

> post_auth_token_revoke_accessor(inline_object101)
This endpoint will delete the token associated with the accessor and all of its child tokens.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object101** | Option<[**InlineObject101**](InlineObject101.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_revoke_orphan

> post_auth_token_revoke_orphan(inline_object102)
This endpoint will delete the token and orphan its child tokens.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object102** | Option<[**InlineObject102**](InlineObject102.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_revoke_self

> post_auth_token_revoke_self()
This endpoint will delete the token used to call it and all of its child tokens.

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


## post_auth_token_roles_role_name

> post_auth_token_roles_role_name(role_name, inline_object103)


### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**role_name** | **String** | Name of the role | [required] |
**inline_object103** | Option<[**InlineObject103**](InlineObject103.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_token_tidy

> post_auth_token_tidy()
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


## post_auth_userpass_duo_access

> post_auth_userpass_duo_access(inline_object104)
Configure the access keys and host for Duo API connections.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object104** | Option<[**InlineObject104**](InlineObject104.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_userpass_duo_config

> post_auth_userpass_duo_config(inline_object105)
Configure Duo second factor behavior.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object105** | Option<[**InlineObject105**](InlineObject105.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_userpass_login_username

> post_auth_userpass_login_username(username, inline_object106)
Log in with a username and password.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**username** | **String** | Username of the user. | [required] |
**inline_object106** | Option<[**InlineObject106**](InlineObject106.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_userpass_mfa_config

> post_auth_userpass_mfa_config(inline_object107)
Configure multi factor backend.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**inline_object107** | Option<[**InlineObject107**](InlineObject107.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_userpass_users_username

> post_auth_userpass_users_username(username, inline_object108)
Manage users allowed to authenticate.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**username** | **String** | Username for this user. | [required] |
**inline_object108** | Option<[**InlineObject108**](InlineObject108.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_userpass_users_username_password

> post_auth_userpass_users_username_password(username, inline_object109)
Reset user's password.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**username** | **String** | Username for this user. | [required] |
**inline_object109** | Option<[**InlineObject109**](InlineObject109.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## post_auth_userpass_users_username_policies

> post_auth_userpass_users_username_policies(username, inline_object110)
Update the policies associated with the username.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**username** | **String** | Username for this user. | [required] |
**inline_object110** | Option<[**InlineObject110**](InlineObject110.md)> |  |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

