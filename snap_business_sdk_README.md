# capi
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The `snap_business_sdk` package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage

This python library package is generated without supporting files like setup.py or requirements files

To be able to use it, you will need these dependencies in your own package that uses this library:

* urllib3 >= 1.25.3
* python-dateutil

## Getting Started

In your own code, to use this library to connect and interact with capi,
you can run the following:

```python

import time
import snap_business_sdk
from pprint import pprint
from snap_business_sdk.api import default_api
from snap_business_sdk.model.capi_event import CapiEvent
from snap_business_sdk.model.response import Response
# Defining the host is optional and defaults to https://tr.snapchat.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = snap_business_sdk.Configuration(
    host = "https://tr.snapchat.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = snap_business_sdk.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)


# Enter a context with an instance of the API client
with snap_business_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    body = [
        CapiEvent(
            pixel_id="pixel_id_example",
            app_id="app_id_example",
            snap_app_id="snap_app_id_example",
            event_type="PURCHASE",
            event_conversion_type="WEB",
            event_tag="event_tag_example",
            timestamp=1,
            hashed_email="hashed_email_example",
            hashed_mobile_ad_id="hashed_mobile_ad_id_example",
            uuid_c1="uuid_c1_example",
            hashed_idfv="hashed_idfv_example",
            hashed_phone_number="hashed_phone_number_example",
            user_agent="user_agent_example",
            hashed_ip_address="hashed_ip_address_example",
            item_category="item_category_example",
            item_ids="item_ids_example",
            description="description_example",
            number_items="number_items_example",
            price="price_example",
            currency="USD",
            transaction_id="transaction_id_example",
            level="level_example",
            client_dedup_id="client_dedup_id_example",
            data_use=["lmu"],
            search_string="search_string_example",
            page_url="page_url_example",
            sign_up_method="sign_up_method_example",
            hashed_first_name_sha="hashed_first_name_sha_example",
            hashed_first_name_sdx="hashed_first_name_sdx_example",
            hashed_middle_name_sha="hashed_middle_name_sha_example",
            hashed_middle_name_sdx="hashed_middle_name_sdx_example",
            hashed_last_name_sha="hashed_last_name_sha_example",
            hashed_last_name_sdx="hashed_last_name_sdx_example",
            hashed_city_sha="hashed_city_sha_example",
            hashed_city_sdx="hashed_city_sdx_example",
            hashed_state_sha="hashed_state_sha_example",
            hashed_state_sdx="hashed_state_sdx_example",
            hashed_zip="hashed_zip_example",
            hashed_dob_month="hashed_dob_month_example",
            hashed_dob_day="hashed_dob_day_example",
            integration="integration_example",
            click_id="click_id_example",
        ),
    ] # [CapiEvent] | Snap Conversions API (optional)

    try:
        api_response = api_instance.send_data(body=body)
        pprint(api_response)
    except snap_business_sdk.ApiException as e:
        print("Exception when calling DefaultApi->send_data: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://tr.snapchat.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**send_data**](snap_business_sdk/docs/DefaultApi.md#send_data) | **POST** /conversion | 


## Documentation For Models

 - [CapiEvent](snap_business_sdk/docs/CapiEvent.md)
 - [Response](snap_business_sdk/docs/Response.md)
 - [ResponseErrorRecords](snap_business_sdk/docs/ResponseErrorRecords.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication (JWT)


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in snap_business_sdk.apis and snap_business_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from snap_business_sdk.api.default_api import DefaultApi`
- `from snap_business_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import snap_business_sdk
from snap_business_sdk.apis import *
from snap_business_sdk.models import *
```
