# R-Access-Azure-Data-Lake-Store-with-Multi-Factor-Authentication
This article shows you how to from R script to access Azure Data Lake Store by using individual user's corporation Multi-Factor Authentication (MFA) credentials, thanks to R-Python bridge package Reticulate.

In my previous article, https://github.com/JackXueIndiana/Jupyter-Notebook-Python3-Access-Azure-Data-Lake-Store, we already know how to use MFA to access ADLS from Python script. However, to date, there is no similar Microsoft R packages have been available. After consulted to several Microsoft R experts, I was suggested to use python package Reticulate, https://github.com/rstudio/reticulate, to make a bridge from R script to the Python script. 

One thing I noticed is that the R version should be 3.5 and up to support the Reticulate source_python() function which is the core of our success.

When you run the R script, please pay attention:

1. The loading python script may take some time as it needs to get all dependences and initiate the runtime.

2. You need to quickly start a browser and point to https://microsoft.com/devicelogin and then enter the CODE showed in your R Studio console.


