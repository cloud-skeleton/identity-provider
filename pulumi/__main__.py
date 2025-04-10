from os import getenv

from pulumi import RunError, ResourceOptions
from pulumiverse_zitadel import Provider, MachineUser

if not (ZITADEL_DOMAIN := getenv("ZITADEL_DOMAIN")):
    raise RunError(f"Environment variable 'ZITADEL_DOMAIN' is not set.")
if not (ZITADEL_JWT_PROFILE_FILE := getenv("ZITADEL_JWT_PROFILE_FILE")):
    raise RunError(f"Environment variable 'ZITADEL_JWT_PROFILE_FILE' is not set.")

zitadel: Provider = Provider(
    "zitadel",
    domain = ZITADEL_DOMAIN,
    jwt_profile_file = ZITADEL_JWT_PROFILE_FILE
)

MachineUser(
    "testuser",
    user_name = "testuser",
    description = "test USER",
    opts = ResourceOptions(provider = zitadel)
)
