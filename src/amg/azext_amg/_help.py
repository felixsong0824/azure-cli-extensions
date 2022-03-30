# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import


helps['grafana'] = """
    type: group
    short-summary: Commands to manage Azure Grafana instanced.
    long-summary: For optimized experience, not all data plane Apis, documented at https://grafana.com/docs/grafana/latest/http_api/, are exposed. On coverage gap, please reach out to ad4g@microsoft.com
"""

helps['grafana create'] = """
    type: command
    short-summary: Create a Azure Managed Grafana instance.
"""

helps['grafana list'] = """
    type: command
    short-summary: List Azure Managed Grafana instances.
"""

helps['grafana delete'] = """
    type: command
    short-summary: Delete a Azure Managed Grafana instance.
"""

helps['grafana show'] = """
    type: command
    short-summary: Show details of a Azure Managed Grafana instance.
"""

helps['grafana data-source'] = """
    type: group
    short-summary: Commands to manage data sources of an instance.
"""

helps['grafana data-source create'] = """
    type: command
    short-summary: Create a data source.
    examples:
        - name: create a data source of Azure SQL
          text: |
            az grafana data-source create -n MyGrafana --definition '{
              "access": "proxy",
              "database": "testdb",
              "jsonData": {
                "authenticationType": "SQL Server Authentication",
                "encrypt": "false"
              },
              "secureJsonData": {
                "password": "verySecretPassword"
              },
              "name": "Microsoft SQL Server",
              "type": "mssql",
              "url": "testsql.database.windows.net",
              "user": "admin1"
            }'
"""


helps['grafana data-source update'] = """
    type: command
    short-summary: Update a data source.
"""

helps['grafana data-source show'] = """
    type: command
    short-summary: get details of a data source
"""

helps['grafana data-source delete'] = """
    type: command
    short-summary: delete a data source
"""

helps['grafana data-source list'] = """
    type: command
    short-summary: List all data sources of an instance.
"""

helps['grafana data-source query'] = """
    type: command
    short-summary: query a data source having backend implementation
"""

helps['grafana dashboard'] = """
    type: group
    short-summary: Commands to manage dashboards of an instance.
"""

helps['grafana dashboard create'] = """
    type: command
    short-summary: Create a new dashboard.
    examples:
        - name: Create a dashboard with definition in a json file. For quick start, clone from the output of "az grafana dashboard show", remove "id" and "uid", and apply changes.
          text: |
            az grafana dashboard create -g MyResourceGroup -n MyGrafana --title "My dashboard" --folder folder1 --definition '{
              "dashboard": {
                "annotations": {
                    ...
                },
                "panels": {
                    ...
                }
              },
              "message": "Create a new test dashboard"
            }'
"""

helps['grafana dashboard update'] = """
    type: command
    short-summary: Update a dashboard.
    examples:
        - name: Update a dashboard with definition in a json file. For quick start, get existing configuration from "az grafana dashboard show", and apply changes.
                "version" field need to be updated, and "overwrite" field should be true.
          text: |
            az grafana dashboard update -g MyResourceGroup -n MyGrafana --definition @c:\\temp\\dashboard.json
"""

helps['grafana dashboard import'] = """
    type: command
    short-summary: import a dashboard.
    long-summary: CLI command will fill in required parameters for data sources if configured
    examples:
        - name: import the dashboard of "AKS Container Insights" from Grafana gallery.
          text: |
            az grafana dashboard import -g MyResourceGroup -n MyGrafana --definition 12180
        - name: import a dashboard from a file.
          text: |
             az grafana dashboard import -g MyResourceGroup -n MyGrafana --definition @c:\\temp\\dashboard.json
"""

helps['grafana dashboard list'] = """
    type: command
    short-summary: List all dashboards of an instance.
    examples:
        - name: Find the dashboard for K8s API Server and retrieve the unique identifier(in order to invoke "az grafana dashboard show" command)
          text: |
           az grafana dashboard list -g MyResourceGroup -n MyGrafana --query "[?contains(@.title, 'API server')].uid"
"""

helps['grafana dashboard show'] = """
    type: command
    short-summary: show the detail of a dashboard.
    examples:
        - name: Get details of a dashboard specified by an unique identifier(use "az grafana dashboard list" command to retrieve the uid)
          text: |
           az grafana dashboard show -g MyResourceGroup -n MyGrafana --dashboard VdrOA7jGz
"""

helps['grafana dashboard delete'] = """
    type: command
    short-summary: delete a dashboard
    examples:
        - name: Delete a dashboard specified by an unique identifier(use "az grafana dashboard list" command to retrieve the uid)
          text: |
           az grafana dashboard delete -g MyResourceGroup -n MyGrafana --dashboard VdrOA7jGz
"""

helps['grafana folder'] = """
    type: group
    short-summary: Commands to manage folders of an instance.
"""

helps['grafana folder create'] = """
    type: command
    short-summary: create a new folder.
"""

helps['grafana folder show'] = """
    type: command
    short-summary: show the details of a folder.
"""

helps['grafana folder list'] = """
    type: command
    short-summary: list all folders of an instance.
"""

helps['grafana folder update'] = """
    type: command
    short-summary: update a folder.
"""

helps['grafana folder delete'] = """
    type: command
    short-summary: delete a folder.
"""

helps['grafana user'] = """
    type: group
    short-summary: Commands to manage users of an instance.
"""

helps['grafana user actual-user'] = """
    type: command
    short-summary: show details of current user.
"""

helps['grafana user list'] = """
    type: command
    short-summary: list users.
"""

helps['grafana user show'] = """
    type: command
    short-summary: show detail of a user.
"""