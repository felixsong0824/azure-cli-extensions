# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "monitor data-collection rule association delete",
    confirmation="Are you sure you want to perform this operation?",
)
class Delete(AAZCommand):
    """Delete an association.

    :example: Delete association
        az monitor data-collection rule association delete --name "myAssociation" --resource "subscr iptions/703362b3-f278-4e4b-9179- c76eaf41ffc2/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVm "
    """

    _aaz_info = {
        "version": "2022-06-01",
        "resources": [
            ["mgmt-plane", "/{resourceuri}/providers/microsoft.insights/datacollectionruleassociations/{}", "2022-06-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return None

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.association_name = AAZStrArg(
            options=["-n", "--name", "--association-name"],
            help="The name of the association. The name is case insensitive.",
            required=True,
        )
        _args_schema.resource_uri = AAZStrArg(
            options=["--resource", "--resource-uri"],
            help="The identifier of the resource.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DataCollectionRuleAssociationsDelete(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class DataCollectionRuleAssociationsDelete(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)
            if session.http_response.status_code in [204]:
                return self.on_204(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/{resourceUri}/providers/Microsoft.Insights/dataCollectionRuleAssociations/{associationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "DELETE"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "associationName", self.ctx.args.association_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceUri", self.ctx.args.resource_uri,
                    skip_quote=True,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-06-01",
                    required=True,
                ),
            }
            return parameters

        def on_200(self, session):
            pass

        def on_204(self, session):
            pass


class _DeleteHelper:
    """Helper class for Delete"""


__all__ = ["Delete"]