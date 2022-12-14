from logging import getLogger

from src.libs.pretty import pretty_array, pretty_json

logger = getLogger("src").getChild(__name__)


class Iam:
    iam_type = ["aws_iam_instance_profile", "aws_iam_role",
                "aws_iam_policy", "aws_iam_policy_document"]

    def __init__(self) -> None:
        pass

    # aws_iam_role
    def role_parser(self, json: dict, iam_type: str) -> dict:
        schema_version = "schema_version"
        attributes = "attributes"
        attributes_arn = "arn"
        attributes_assume_role_policy = "assume_role_policy"
        attributes_description = "description"
        attributes_tags = "tags"
        dependencies = "dependencies"

        return {
            "type": iam_type,
            schema_version:                json.get(schema_version),
            attributes_arn:                json.get(attributes, {}).get(attributes_arn),
            attributes_assume_role_policy: pretty_json(json.get(attributes, {}).get(attributes_assume_role_policy, {})),
            attributes_description:        json.get(attributes, {}).get(attributes_description),
            attributes_tags:               json.get(attributes, {}).get(attributes_tags),
            dependencies:                  pretty_array(
                json.get(dependencies, []))
        }

    # aws_iam_policy
    def policy_parser(self, json: dict, iam_type: str) -> dict:
        schema_version = "schema_version"
        attributes = "attributes"
        attributes_arn = "arn"
        attributes_name = "name"
        attributes_assume_role_policy = "assume_role_policy"
        attributes_description = "description"
        attributes_tags = "tags"
        attributes_policy = "policy"
        dependencies = "dependencies"

        return {
            "type": iam_type,
            schema_version:  json.get(schema_version),
            attributes_arn:  json.get(attributes, {}).get(attributes_arn),
            attributes_name: json.get(attributes, {}).get(attributes_name),
            attributes_assume_role_policy: json.get(attributes, {}).get(attributes_assume_role_policy),
            attributes_description:        json.get(attributes, {}).get(attributes_description),
            attributes_tags:               json.get(attributes, {}).get(attributes_tags),
            attributes_policy:             pretty_json(json.get(attributes, {}).get(attributes_policy, "")),
            dependencies:                  pretty_array(
                json.get(dependencies, []))
        }

    # aws_iam_instance_profile
    def instance_profile_parser(self, json: dict, iam_type: str) -> dict:
        return {}

    # aws_iam_policy_document
    def policy_document_parser(self, json: dict, iam_type: str) -> dict | None:
        schema_version = "schema_version"
        attributes = "attributes"
        attributes_id = "id"
        attributes_json = "json"
        attributes_state = "statement"
        attributes_tags = "tags"
        attributes_condition = "condition"
        attributes_principals = "principals"
        resources = "resources"

        return {
            "type":                iam_type,
            schema_version:        json.get(schema_version),
            attributes_id:         json.get(attributes, {}).get(attributes_id),
            attributes_json:       pretty_json(json.get(attributes, {}).get(attributes_json, "")),
            attributes_state:      json.get(attributes, {}).get(attributes_state, []),
            attributes_condition:  json.get(attributes, {}).get(attributes_condition),
            attributes_tags:       json.get(attributes, {}).get(attributes_tags),
            attributes_principals: pretty_json(json.get(attributes, {}).get(attributes_principals, "")),
            resources:             json.get(resources)
        }

    # aws_iam_role_policy_attachment
    def role_policy_attachment_parser(self, json: dict, iam_type: str) -> dict | None:
        schema_version = "schema_version"
        attributes = "attributes"
        attributes_id = "id"
        attributes_role = "role"
        attributes_policy_arn = "policy_arn"
        attributes_tags = "tags"
        dependencies = "dependencies"

        attributes = json.get("attributes", {})

        return {
            "type":                  iam_type,
            schema_version:        json.get(schema_version),
            attributes_id:         attributes.get(attributes_id),
            attributes_role:       attributes.get(attributes_role),
            attributes_policy_arn: attributes.get(attributes_policy_arn),
            attributes_tags:       attributes.get(attributes_tags),
            dependencies:          pretty_array(json.get(dependencies, []))
        }

    # aws_iam_user_policy_attachment
    def iam_user_policy_attachment_parser(self, json: dict, iam_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        attributes_id = "id"
        attributes_policy_arn = "policy_arn"
        dependencies = "dependencies"

        attributes = json.get("attributes", {})

        return {
            "type":                iam_type,
            schema_version:        json.get(schema_version),
            attributes_id:         attributes.get(attributes_id),
            attributes_policy_arn: attributes.get(attributes_policy_arn),
            dependencies:          pretty_array(json.get(dependencies, []))
        }

    # aws_iam_user
    def iam_user_parser(self,  json: dict, iam_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        attributes_arn = "arn"
        attributes_id = "id"
        attributes_name = "name"
        attributes_tags = "tags"
        dependencies = "dependencies"

        attributes = json.get("attributes", {})

        return {
            "type":                iam_type,
            schema_version:        json.get(schema_version),
            attributes_arn:        attributes.get(attributes_arn),
            attributes_id:         attributes.get(attributes_id),
            attributes_name:       attributes.get(attributes_name),
            attributes_tags:       attributes.get(attributes_tags),
            dependencies:          pretty_array(json.get(dependencies, []))
        }

    # aws_iam_policy_attachment
    def iam_policy_attachment(self,  json: dict, iam_type: str):
        schema_version = "schema_version"
        attributes = "attributes"
        attributes_id = "id"
        attributes_name = "name"
        attributes_policy_arn = "policy_arn"
        attributes_tags = "tags"
        attributes_roles = "roles"
        attributes_users = "users"
        dependencies = "dependencies"

        attributes = json.get("attributes", {})

        return {
            "type":                  iam_type,
            schema_version:        json.get(schema_version),
            attributes_id:         attributes.get(attributes_id),
            attributes_name:       attributes.get(attributes_name),
            attributes_policy_arn: attributes.get(attributes_policy_arn),
            attributes_tags:       attributes.get(attributes_tags),
            attributes_roles:      attributes.get(attributes_roles),
            attributes_users:      attributes.get(attributes_users),
            dependencies:          pretty_array(json.get(dependencies, []))
        }

    # unknow type

    def unknown_type(self, json: dict, iam_type: str):
        logger.warning(f"{iam_type} is not defined")
        # raise Exception(f"{iam_type} is not defined in iam type")
        return json

    def parse(self, json: dict, iam_type: str):
        switcher = {
            "aws_iam_instance_profile": self.instance_profile_parser,
            "aws_iam_role": self.role_parser,
            "aws_iam_policy": self.policy_parser,
            "aws_iam_policy_document": self.policy_document_parser,
            "aws_iam_role_policy_attachment": self.role_policy_attachment_parser,
            "aws_iam_user": self.iam_user_parser,
            "aws_iam_user_policy_attachment": self.iam_user_policy_attachment_parser,
            "aws_iam_policy_attachment": self.iam_policy_attachment,

        }
        return switcher.get(iam_type, self.unknown_type)(json=json, iam_type=iam_type)
