# stylelens_product.HostApi

All URIs are relative to *http://product.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_host**](HostApi.md#add_host) | **POST** /hosts | Add a new HOst


# **add_host**
> AddHostResponse add_host(body)

Add a new HOst



### Example 
```python
from __future__ import print_function
import time
import stylelens_product
from stylelens_product.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_product.HostApi()
body = stylelens_product.Host() # Host | Host object that needs to be added to the db.

try: 
    # Add a new HOst
    api_response = api_instance.add_host(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostApi->add_host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Host**](Host.md)| Host object that needs to be added to the db. | 

### Return type

[**AddHostResponse**](AddHostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
