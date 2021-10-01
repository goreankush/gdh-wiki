# coding=utf-8
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_authentication_async.py

DESCRIPTION:
    This sample demonstrates how to authenticate to the Conversational Language Understanding service.
    We authenticate using an AzureKeyCredential from azure.core.credentials.

    See more details about authentication here:
    https://docs.microsoft.com/azure/cognitive-services/authentication

    Note: the endpoint must be formatted to use the custom domain name for your resource:
    https://<NAME-OF-YOUR-RESOURCE>.cognitiveservices.azure.com/

USAGE:
    python sample_authentication_async.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_CONVERSATIONS_ENDPOINT - the endpoint to your Conversational Language Understanding resource.
    2) AZURE_CONVERSATIONS_KEY - your Conversational Language Understanding API key
"""

import os
import asyncio


async def sample_authentication_api_key_async():
    # [START create_clu_client_with_key_async]
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.language.conversations.aio import ConversationAnalysisClient

    endpoint = os.environ["AZURE_CONVERSATIONS_ENDPOINT"]
    key = os.environ["AZURE_CONVERSATIONS_KEY"]

    clu_client = ConversationAnalysisClient(endpoint, AzureKeyCredential(key))
    # [END create_clu_client_with_key_async]


async def main():
    await sample_authentication_api_key_async()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
