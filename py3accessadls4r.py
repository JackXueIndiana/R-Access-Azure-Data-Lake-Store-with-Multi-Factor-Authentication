
# coding: utf-8

# ** This is an example to show how to access Azure Data Lake Store from Python 3 **
# 
# Jack Xue
# 
# 2018-08-13
# 
# You need to first install three packages from Microsoft
# 
# pip install azure-mgmt-resource
# 
# pip install azure-mgmt-datalake-store
# 
# pip install azure-datalake-store
# 
# A good Microsfot document to follow is here: 
# https://docs.microsoft.com/en-us/azure/data-lake-store/data-lake-store-data-operations-python
# 
# The interactive login is discussed here:
# https://stackoverflow.com/questions/48208389/python-code-to-access-azure-data-lake-store

# In[ ]:

## Use this only for Azure AD service-to-service authentication
from azure.common.credentials import ServicePrincipalCredentials

## Use this only for Azure AD end-user authentication
from azure.common.credentials import UserPassCredentials

## Use this only for Azure AD multi-factor authentication
from msrestazure.azure_active_directory import AADTokenCredentials

## Required for Azure Data Lake Store account management
from azure.mgmt.datalake.store import DataLakeStoreAccountManagementClient
from azure.mgmt.datalake.store.models import DataLakeStoreAccount

## Required for Azure Data Lake Store filesystem management
from azure.datalake.store import core, lib, multithread

# Common Azure imports
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.resource.resources.models import ResourceGroup

## Use these as needed for your application
import logging, getpass, pprint, uuid, time


# In[ ]:

def login():
    return lib.auth();


# In[ ]:

# Create a filesystem client object
def uploadfiletoadls(store_name, adls_dir, l_path, r_path):
    adlsFileSystemClient = core.AzureDLFileSystem(credentials, store_name=store_name)
    adlsFileSystemClient.mkdir(adls_dir)
    multithread.ADLUploader(adlsFileSystemClient, lpath=l_path, rpath=r_path, nthreads=64, overwrite=True, buffersize=4194304, blocksize=4194304)
    return 0;


# In[ ]:

credentials = login()


# In[ ]:

#status = uploadfiletoadls('jacktestsbdls', '/mysampledirectory', 'C:\\Users\\xinxue\\data\\test.txt', '/mysampledirectory/mysamplefile.txt')


# In[ ]:

#status


# In[ ]:



