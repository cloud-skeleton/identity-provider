from os import getenv

from pulumi import RunError

if not (ZITADEL_DOMAIN := getenv("ZITADEL_DOMAIN")):
    raise RunError(f"Environment variable 'ZITADEL_DOMAIN' is not set.")
if not (ZITADEL_JWT_PROFILE_FILE := getenv("ZITADEL_JWT_PROFILE_FILE")):
    raise RunError(f"Environment variable 'ZITADEL_JWT_PROFILE_FILE' is not set.")

# print(ZITADEL_DOMAIN, ZITADEL_JWT_PROFILE_FILE)

# from pulumi import Config
# from pulumiverse_zitadel import MachineUser

# MachineUser("testuser", user_name = "testuser", description = "test USER")

# zitadel_config: Config = Config("zitadel")
# print(zitadel_config.require("jwtProfileFile"))
