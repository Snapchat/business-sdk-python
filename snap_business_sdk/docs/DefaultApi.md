# snap_business_sdk.DefaultApi

All URIs are relative to *https://tr.snapchat.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_data**](DefaultApi.md#send_data) | **POST** /conversion | 


# **send_data**
> Response send_data()



### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import snap_business_sdk
from snap_business_sdk.api import default_api
from snap_business_sdk.model.capi_event import CapiEvent
from snap_business_sdk.model.response import Response
from pprint import pprint
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

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.send_data(body=body)
        pprint(api_response)
    except snap_business_sdk.ApiException as e:
        print("Exception when calling DefaultApi->send_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**[CapiEvent]**](CapiEvent.md)| Snap Conversions API | [optional]

### Return type

[**Response**](Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**0** | unsuccessful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

