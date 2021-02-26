use vault::apis::secrets_api::{post_secret_data, get_secret_data, GetSecretDataError};
use vault::models::{SecretDataInput, SecretData};
use vault::apis::configuration::Configuration;
use serde_json::json;
use reqwest::header;
use vault::apis::Error;

#[tokio::main]
async fn main() {
    let data = json!({ "reiner": "braun", "eren": "yeager"});
    let input = SecretDataInput {
        data: Some(data),
        options: None,
        version: None
    };

    let mut config = Configuration::new();
    let mut headers = header::HeaderMap::new();
    // let token = std::env::var("VAULT_TOKEN").unwrap_or("".parse().unwrap());
    headers.insert("X-Vault-Token", header::HeaderValue::from_static("test"));
    config.client = reqwest::Client::builder().default_headers(headers).build().unwrap();
    config.base_path = std::env::var("VAULT_ADDR").unwrap_or("".parse().unwrap()) + "/v1";

    let result = post_secret_data(&config, "aot", Some(input)).await.is_ok();
    println!("done posting, success={:?}", result);

    let secret_data = get_secret_data(&config, "aot").await.unwrap();
    println!("{}", secret_data.data.unwrap())
}
