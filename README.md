![Cloud Skeleton](./assets/logo.jpg)

[![GPLv3 License](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![SSL Security A+](https://img.shields.io/badge/SSL_Security-A+-green)](https://www.ssllabs.com/ssltest/)
[![Max_RAM-384M](https://img.shields.io/badge/Max_RAM-384M-violet)]()

# **[Cloud Skeleton](https://github.com/cloud-skeleton/)** ► **[Identity Provider](https://github.com/cloud-skeleton/identity-provider/)** 🛂

> This repository contains the deployment stack for **[ZITADEL](https://zitadel.com/docs/guides/start/quickstart)**, a cloud-native identity and access management solution. It leverages **[Docker](https://docs.docker.com/get-started/)** and **[Docker Compose](https://docs.docker.com/compose/gettingstarted/)** to set up a fully isolated environment, backed by **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)** and integrated into the **[Cloud Skeleton](https://github.com/cloud-skeleton/)** platform via shared network configuration and labels.

## Overview

The **[Identity Provider](https://github.com/cloud-skeleton/identity-provider/)** stack deploys **[ZITADEL](https://zitadel.com/docs/guides/start/quickstart)**, a modern identity provider written in Go and powered by **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)**. It offers features such as:
- OAuth2 and OpenID Connect support.
- Passwordless login.
- Self-hosted identity federation.

It is integrated with:
- A managed **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)** database.
- The shared `proxy_bridge` network to allow routing through the **[Container Proxy](https://github.com/cloud-skeleton/container-proxy/)** using **[Traefik](https://doc.traefik.io/traefik/)**.

## Deployment Services

This stack deploys two main services defined in `compose.yml`:

- `zitadel`: The identity provider service itself.
- `postgresql`: A dedicated database service with persistent volume storage.

## Environment Variables

The deployment is configured using environment variables defined in the `.env` file:

- **ZITADEL_DATABASE_USER**  
  *Description:* **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)** user name for **[ZITADEL](https://zitadel.com/docs/guides/start/quickstart)** database access.  
  *Example:*  
  ```env
  ZITADEL_DATABASE_USER=zitadel_user
  ```

- **ZITADEL_DATABASE_PASSWORD**  
  *Description:* Password for the database user.  
  *Example:*  
  ```env
  ZITADEL_DATABASE_PASSWORD=secretpassword
  ```

- **ZITADEL_DATABASE_HOST**  
  *Description:* Hostname of the **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)** service.  
  *Default:* `postgres`  
  *Example:*  
  ```env
  ZITADEL_DATABASE_HOST=postgres
  ```

- **ZITADEL_DATABASE_PORT**  
  *Description:* Port on which the **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)** server is listening.  
  *Default:* `5432`  
  *Example:*  
  ```env
  ZITADEL_DATABASE_PORT=5432
  ```

- **ZITADEL_DATABASE_NAME**  
  *Description:* Name of the database to use.  
  *Example:*  
  ```env
  ZITADEL_DATABASE_NAME=zitadel
  ```

- **ZITADEL_EXTERN_URL**  
  *Description:* Public URL under which **[ZITADEL](https://zitadel.com/docs/guides/start/quickstart)** will be reachable.  
  *Example:*  
  ```env
  ZITADEL_EXTERN_URL=https://id.example.com
  ```

- **ZITADEL_TLS_ENABLED**  
  *Description:* Whether **[ZITADEL](https://zitadel.com/docs/guides/start/quickstart)** should use TLS internally.  
  *Default:* `false`  
  *Example:*  
  ```env
  ZITADEL_TLS_ENABLED=false
  ```

## Usage

1. **Create External Network:**  
   If not already created by **[Container Proxy](https://github.com/cloud-skeleton/container-proxy/)**, set up the shared network:

   ```sh
   docker network create proxy_bridge
   ```

2. **Clone the Repository:**

   ```sh
   git clone https://github.com/cloud-skeleton/identity-provider.git
   cd identity-provider
   ```

3. **Create a `.env` File:**  
   Populate with necessary variables for **[ZITADEL](https://zitadel.com/docs/guides/start/quickstart)** and **[PostgreSQL](https://www.postgresql.org/docs/current/index.html)**:

   ```env
   ZITADEL_DATABASE_USER=zitadel_user
   ZITADEL_DATABASE_PASSWORD=secretpassword
   ZITADEL_DATABASE_HOST=postgres
   ZITADEL_DATABASE_PORT=5432
   ZITADEL_DATABASE_NAME=zitadel
   ZITADEL_EXTERN_URL=https://id.example.com
   ZITADEL_TLS_ENABLED=false
   ```

4. **Deploy with [Docker Compose](https://docs.docker.com/compose/gettingstarted/):**

   ```sh
   docker compose up -d
   ```

## Integration with Traefik

This repository is designed to be used behind the **[Traefik](https://doc.traefik.io/traefik/)** reverse proxy managed by the **[Container Proxy](https://github.com/cloud-skeleton/container-proxy/)**.

Labels in the `zitadel` service route requests based on hostname:

```yaml
labels:
  - traefik.enable=true
  - traefik.http.routers.zitadel.rule=Host(`id.example.com`)
  - traefik.http.routers.zitadel.entrypoints=websecure
  - traefik.http.routers.zitadel.tls.certresolver=letsencrypt
```

Ensure DNS points `id.example.com` to the proxy host and that your **[Let's Encrypt](https://letsencrypt.org/getting-started/)** certificates are properly configured via the shared Traefik service.

## Database Initialization

On first startup, the database is initialized automatically via the entrypoint. Persistent storage is mounted at `./volumes/postgresql/`.

## Backup & Persistence

- **Database Volume:**  
  PostgreSQL data is stored in the local `volumes/postgresql/` directory, which is mounted as a Docker volume.

- **Environment Config:**  
  Ensure you back up the `.env` file and the entire project directory to restore the service in case of failure.

## Contributing

We welcome contributions from the community!  
- Fork this repository.
- Create a branch (e.g., `fix/typo` or `feature/add-oidc-support`).
- Submit a pull request and describe your change.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

---

*This identity provider deployment is maintained by **[Cloud Skeleton](https://github.com/cloud-skeleton/)** and designed to provide a unified authentication solution for EU citizen-led services. 🇪🇺*
