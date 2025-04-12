![Cloud Skeleton](./assets/logo.jpg)

[![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![SSL Security A+](https://img.shields.io/badge/SSL_Security-A+-green)](https://www.ssllabs.com/ssltest/)
[![Max_RAM-384M](https://img.shields.io/badge/Max_RAM-384M-violet)]()

# **[Cloud Skeleton](https://github.com/cloud-skeleton/)** ► **[Identity Provider](https://github.com/cloud-skeleton/identity-provider/)** 🛂

> This repository contains the deployment stack for **[ZITADEL](https://zitadel.com/docs/guides/start/quickstart)**, a cloud-native identity and access management solution. It leverages **[Docker](https://docs.docker.com/get-started/)** and **[Docker Compose](https://docs.docker.com/compose/gettingstarted/)** to set up a fully isolated environment, backed by **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)** and integrated into the **[Cloud Skeleton](https://github.com/cloud-skeleton/)** platform via shared network configuration and labels.

## Overview

The **[Identity Provider](https://github.com/cloud-skeleton/identity-provider/)** stack deploys **[ZITADEL](https://zitadel.com/docs/guides/start/quickstart)**, a modern identity provider written in Go and powered by **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)**. It offers features such as:
- **[OAuth2](https://oauth.net/getting-started/)** and **[OpenID Connect](https://openid.net/developers/how-connect-works/)** support.
- Passwordless login.
- Self-hosted identity federation.

It is integrated with:
- A managed **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)** database.
- The shared `proxy_bridge` network to allow routing through the **[Container Proxy](https://github.com/cloud-skeleton/container-proxy/)** using **[Traefik](https://doc.traefik.io/traefik/)**.

> **IMPORTANT:** Before deploying the **[Identity Provider](https://github.com/cloud-skeleton/identity-provider/)**, **you must deploy [Container Proxy](https://github.com/cloud-skeleton/container-proxy/) stack**.

## Deployment Services

This stack deploys two main services defined in `compose.yml`:

- `zitadel`: The identity provider service itself.
- `postgresql`: A dedicated database service with persistent volume storage.

## Environment Variables

The deployment is configured using environment variables defined in the `.env` file:

- **HOST_NAME**  
  *Description:* The hostname for the **[ZITADEL](https://zitadel.com/docs/guides/start/quickstart)** service.  
  *Example:*  
  ```env
  HOST_NAME=identity.example.com
  ```

- **SMTP_SERVER_ENABLE_TLS**  
  *Description:* Whether to use TLS when connecting to the SMTP server.  
  *Default:* `false`  
  *Example:*  
  ```env
  SMTP_SERVER_ENABLE_TLS=true
  ```

- **SMTP_SERVER_HOST_NAME**  
  *Description:* Hostname of the SMTP server used for sending emails.  
  *Example:*  
  ```env
  SMTP_SERVER_HOST_NAME=smtp.example.com
  ```

- **SMTP_SERVER_PORT**  
  *Description:* Port used to connect to the SMTP server.  
  *Default:* `25`  
  *Example:*  
  ```env
  SMTP_SERVER_PORT=587
  ```

- **SMTP_SERVER_USER_NAME**  
  *Description:* Username for authenticating with the SMTP server.  
  *Example:*  
  ```env
  SMTP_SERVER_USER_NAME=admin@example.com
  ```

- **SMTP_SERVER_USER_PASSWORD**  
  *Description:* Password for authenticating with the SMTP server.  
  *Example:*  
  ```env
  SMTP_SERVER_USER_PASSWORD=securepassword
  ```

- **ZITADEL_ORGANIZATION_NAME**  
  *Description:* Name of the default organization to create on first launch.  
  *Example:*  
  ```env
  ZITADEL_ORGANIZATION_NAME=Home
  ```

- **ZITADEL_USER_EMAIL_ADDRESS**  
  *Description:* Email address of the initial admin user.  
  *Example:*  
  ```env
  ZITADEL_USER_EMAIL_ADDRESS=admin@example.com
  ```

- **ZITADEL_USER_FIRST_NAME**  
  *Description:* First name of the initial admin user.  
  *Example:*  
  ```env
  ZITADEL_USER_FIRST_NAME=John
  ```

- **ZITADEL_USER_LAST_NAME**  
  *Description:* Last name of the initial admin user.  
  *Example:*  
  ```env
  ZITADEL_USER_LAST_NAME=Doe
  ```

- **ZITADEL_USER_NAME**  
  *Description:* Username for the initial admin user.  
  *Example:*  
  ```env
  ZITADEL_USER_NAME=john.doe@example.com
  ```

- **ZITADEL_USER_PASSWORD**  
  *Description:* Password for the initial admin user.  
  *Example:*  
  ```env
  ZITADEL_USER_PASSWORD='securePa$$word'
  ```

## Usage

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/cloud-skeleton/identity-provider.git
   cd identity-provider
   ```

2. **Create a `.env` File:**  
   Populate it with all necessary variables for **[ZITADEL](https://zitadel.com/docs/guides/start/quickstart)**, **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)**, and SMTP email integration:

   ```env
   HOST_NAME=identity.example.com
   ZITADEL_ORGANIZATION_NAME=Home
   ZITADEL_USER_NAME=john.doe@example.com
   ZITADEL_USER_PASSWORD='securePa$$word'
   ZITADEL_USER_EMAIL_ADDRESS=admin@example.com
   ZITADEL_USER_FIRST_NAME=John
   ZITADEL_USER_LAST_NAME=Doe
   SMTP_SERVER_HOST_NAME=smtp.example.com
   SMTP_SERVER_PORT=587
   SMTP_SERVER_USER_NAME=admin@example.com
   SMTP_SERVER_USER_PASSWORD=securepassword
   SMTP_SERVER_ENABLE_TLS=true
   ```

3. **Deploy with [Docker Compose](https://docs.docker.com/compose/gettingstarted/):**

   ```sh
   docker compose up -d
   ```

## Integration with Traefik

This repository is designed to be used behind the **[Traefik](https://doc.traefik.io/traefik/)** reverse proxy managed by the **[Container Proxy](https://github.com/cloud-skeleton/container-proxy/)**. Ensure DNS points `identity.example.com` to the proxy host.

## Backup & Persistence

- **State Volume:**  
  Data is stored in the local `./state` directory, which is mounted as a **[Docker](https://docs.docker.com/get-started/)** volume.

- **Environment Config:**  
  Ensure you back up the `.env` file and the entire project directory to restore the service in case of failure.

## Contributing

Contributions are welcome!  
- Fork the repository.
- Create a new branch (e.g., **`feature/my-improvement`**).
- Submit a pull request with your changes.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

---

*This repository is maintained exclusively by the **[Cloud Skeleton](https://github.com/cloud-skeleton/)** project, and it was developed by EU citizens who are strong proponents of the European Federation. 🇪🇺*
