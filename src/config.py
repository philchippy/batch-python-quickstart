# -------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "python_quickstart_client.py "
# Please note that storing the batch and storage account keys in Azure Key Vault
# is a better practice for Production usage.

"""
Configure Batch and Storage Account credentials
"""

BATCH_ACCOUNT_NAME = 'pythonrunner'  # Your batch account name
BATCH_ACCOUNT_KEY = '+cttssE/HabpB/eZsC1XxHoWTNoU3DeBI6U0EPXpAbYpu3e1dfPCcZPXVKkfFMB8nEM6v18pIkyh+ABaqO0QZQ=='  # Your batch account key
BATCH_ACCOUNT_URL = 'https://pythonrunner.uksouth.batch.azure.com'  # Your batch account URL
STORAGE_ACCOUNT_NAME = 'cotsdistillery1'
STORAGE_ACCOUNT_KEY = '+cttssE/HabpB/eZsC1XxHoWTNoU3DeBI6U0EPXpAbYpu3e1dfPCcZPXVKkfFMB8nEM6v18pIkyh+ABaqO0QZQ=='
STORAGE_ACCOUNT_DOMAIN = 'blob.core.windows.net' # Your storage account blob service domain

POOL_ID = 'PythonQuickstartPool'  # Your Pool ID
POOL_NODE_COUNT = 2  # Pool node count
POOL_VM_SIZE = 'STANDARD_DS1_V2'  # VM Type/Size
JOB_ID = 'PythonQuickstartJob'  # Job ID
STANDARD_OUT_FILE_NAME = 'stdout.txt'  # Standard Output file
