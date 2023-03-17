from src.provider.terraform.vender import ProviderVendor


class Resources:
    mode = "mode"
    terraform_type = "type"
    name = "name"
    provider = "provider_name"

    def __init__(self) -> None:
        pass

    def parse(self, json: dict) -> dict:
        mode = json.get(self.mode)
        terraform_type = json.get(self.terraform_type)
        provider = json.get(self.provider, "")
        name = json.get(self.name, "")
        if "aws" in provider:
            provider = ProviderVendor.AWS.value
        else:
            provider = ProviderVendor.NA.value
        return {
            "mode": mode,
            "type": terraform_type,
            "provider": provider,
            "name": name
        }
