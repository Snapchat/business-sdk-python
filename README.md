# CAPI Business SDK in Python

## Introduction
The Snapchat Conversions API (CAPI) allows you to pass web, app, and offline events to Snap via a Server-to-Server (S2S) integration. Similar to our other Direct Data Integrations, Snap Pixel and App Ads Kit (SDK), by passing these events, you can access post-view and post-swipe campaign reporting to measure performance and incrementality. Depending on the data shared and timeliness of integration, it’s also possible to leverage events passed via Conversions API for solutions such as custom audience targeting, campaign optimization, Dynamic Ads, and more.

Business SDK is an API client that facilitates requests and authentication processes with CAPI as if they were local functions of the supported languages. There have been similar products (e.g. Facebook Business SDK for Conversion API), which largely simplified the integration for advertising platforms. To improve the developer experience and CAPI adoption, we bundle the dedicated CAPI client, hashing libraries, and code examples into one SDK that is available in multiple languages. In addition, our CAPI Business SDK paves the way for Privacy-Enhancing Technologies in CAPI v2, with seamless integration of the Launch Pad.
## Installation
The CAPI Business SDK will be available for download through pip. (For pilot users, please contact us for the pre-build wheel file before the official release). Please use the code snippet below to import the pip dependencies.

`pip install TODO`

## Code Example
### Sending Production Events
Please use the code example below as a template on sending your conversion events to Snap Conversion API. More conversion parameters are expected to be provided in practice.

Example 1: Send a single CAPI event
```
from snap_business_sdk.public.conversion_api import ConversionApi
from snap_business_sdk.public.conversion_event import ConversionEvent

# Configure Bearer authorization (JWT): bearerAuth
access_token = 'TOKEN_WITHOUT_BEARER_PREFIX'

# Create an instance of the API class
api_instance = ConversionApi(
   access_token=access_token,
   # launchpad_url="TEST_LAUNCHPAD_URL"
)

# (Optional) Enable debug mode for conversion event
api_instance.set_debug_mode(enabled=True)

event = ConversionEvent(
       pixel_id="TEST_PIXEL_ID",
       event_type="PURCHASE",
       event_conversion_type="WEB",
       event_tag="event_tag_example",
       timestamp=1656022510346,
       uuid_c1="34dd6077-e3a0-4b1c-9f91-a690ea0e335d",
       # we support pass in plaintext email (it will be hashed and set to hashed_email automatically)
       email="test@example.com",
       # you can also pass hashed email if preferred
       # hashed_email="f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a",

       # we support pass in plaintext phone number (it will be hashed and set to hashed_phone_number automatically)
       phone="1234567890",
       # you can also pass hashed phone number if preferred
       # hashed_phone_number="a2b5e507dfb65941ff4be6e4fc089313cbbb640da5fd6fbc4e3d2e2f3abe92cc",

       # we support pass in plaintext ip address (it will be hashed and set to hashed_ip_address automatically)
       ip_address="12.34.56.78",
       # you can also pass hashed ip address if preferred
       # hashed_ip_address="f1412386aa8db2579aff2636cb9511cacc5fd9880ecab60c048508fbe26ee4d9",
       item_category="item_category_example",
       item_ids="item_ids_example",
       description="description_example",
       number_items="number_items_example",
       price="price_example",
       currency="USD",
       transaction_id="transaction_id_example",
       level="level_example",
       client_dedup_id="client_dedup_id_example",
       search_string="search_string_example",
       page_url="page_url_example",
       sign_up_method="sign_up_method_example",
       first_name="test_first",
       # hashed_first_name_sha="d99156483b6a99eb5f5a1707f7330e1c979a648b47a379d56a0d6850a9a9c76c"，
       # hashed_first_name_sdx="T231",
       middle_name="",
       # hashed_middle_name_sha="",
       # hashed_middle_name_sdx="",
       last_name="test_last",
       # hashed_last_name_sha="19fc3d9f9f6fad30ccbbebd51f67515dc95d8a5ef363fd35c34a2f47064d43bd",
       # hashed_last_name_sdx="T234",
       city="Los Angeles",
       # hashed_city_sha="9f2608067816e38c85edfb0c3985feff32def8b5dc17bb522ffc2e877e9b386b",
       # hashed_city_sdx="L252",
       state="CA",
       # hashed_state_sha="6959097001d10501ac7d54c0bdb8db61420f658f2922cc26e46d536119a31126",
       # hashed_state_sdx="C000",
       zip="00000",
       # hashed_zip="e7042ac7d09c7bc41c8cfa5749e41858f6980643bc0db1a83cc793d3e24d3f77",
       click_id="click_id_example",
   )

# send event in asynchronous way
api_instance.send_event(event)

# (Optional) If you would like to get the async result
# async_res = api_instance.send_event(event);
# result = async_res.get();
```


Example 2: Send a batch of CAPI events (up to 2000)
```
import time
from snap_business_sdk.public.conversion_api import ConversionApi
from snap_business_sdk.public.conversion_event import ConversionEvent

# Configure Bearer authorization (JWT): bearerAuth
access_token = 'TOKEN_WITHOUT_BEARER_PREFIX'

# Create an instance of the API class
api_instance = ConversionApi(
    access_token=access_token,
    # launchpad_url="TEST_LAUNCHPAD_URL"
)

# (Optional) Enable debug mode for conversion event
api_instance.set_debug_mode(enabled=True)

events = [
    ConversionEvent(
        pixel_id="9633c2ae-0115-495a-aca9-b976db485fc8",
        event_type="PURCHASE",
        event_conversion_type="WEB",
        event_tag="event_tag_example",
        timestamp=str(round(time.time()*1000.0)),
        uuid_c1="34dd6077-e3a0-4b1c-9f91-a690ea0e335d",
        # we support pass in plaintext email (it will be hashed and set to hashed_email automatically)
        email="test@example.com",
        # you can also pass hashed email if preferred
        # hashed_email="f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a",

        # we support pass in plaintext phone number (it will be hashed and set to hashed_phone_number automatically)
        phone="1234567890",
        # you can also pass hashed phone number if preferred
        # hashed_phone_number="a2b5e507dfb65941ff4be6e4fc089313cbbb640da5fd6fbc4e3d2e2f3abe92cc",

        # we support pass in plaintext ip address (it will be hashed and set to hashed_ip_address automatically)
        ip_address="12.34.56.78",
        # you can also pass hashed ip address if preferred
        # hashed_ip_address="f1412386aa8db2579aff2636cb9511cacc5fd9880ecab60c048508fbe26ee4d9",
        item_category="item_category_example",
        item_ids="item_ids_example",
        description="description_example",
        number_items="number_items_example",
        price="price_example",
        currency="USD",
        transaction_id="transaction_id_example",
        level="level_example",
        client_dedup_id="client_dedup_id_example",
        search_string="search_string_example",
        page_url="page_url_example",
        sign_up_method="sign_up_method_example",
        first_name="test_first",
        # hashed_first_name_sha="d99156483b6a99eb5f5a1707f7330e1c979a648b47a379d56a0d6850a9a9c76c"，
        # hashed_first_name_sdx="T231",
        middle_name="",
        # hashed_middle_name_sha="",
        # hashed_middle_name_sdx="",
        last_name="test_last",
        # hashed_last_name_sha="19fc3d9f9f6fad30ccbbebd51f67515dc95d8a5ef363fd35c34a2f47064d43bd",
        # hashed_last_name_sdx="T234",
        city="Los Angeles",
        # hashed_city_sha="9f2608067816e38c85edfb0c3985feff32def8b5dc17bb522ffc2e877e9b386b",
        # hashed_city_sdx="L252",
        state="CA",
        # hashed_state_sha="6959097001d10501ac7d54c0bdb8db61420f658f2922cc26e46d536119a31126",
        # hashed_state_sdx="C000",
        zip="00000",
        # hashed_zip="e7042ac7d09c7bc41c8cfa5749e41858f6980643bc0db1a83cc793d3e24d3f77",
        click_id="click_id_example",
    ),
    ConversionEvent(
        pixel_id="9633c2ae-0115-495a-aca9-b976db485fc8",
        event_type="ADD_CART",
        event_conversion_type="WEB",
        event_tag="event_tag_example",
        timestamp=str(round(time.time()*1000.0)),
        uuid_c1="34dd6077-e3a0-4b1c-9f91-a690ea0e335d",
        # we support pass in plaintext email (it will be hashed and set to hashed_email automatically)
        email="test2@example.com",
        # you can also pass hashed email if preferred
        # hashed_email="f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a",

        # we support pass in plaintext phone number (it will be hashed and set to hashed_phone_number automatically)
        phone="1234567890",
        # you can also pass hashed phone number if preferred
        # hashed_phone_number="a2b5e507dfb65941ff4be6e4fc089313cbbb640da5fd6fbc4e3d2e2f3abe92cc",

        # we support pass in plaintext ip address (it will be hashed and set to hashed_ip_address automatically)
        ip_address="12.34.56.78",
        # you can also pass hashed ip address if preferred
        # hashed_ip_address="f1412386aa8db2579aff2636cb9511cacc5fd9880ecab60c048508fbe26ee4d9",
        item_category="item_category_example",
        item_ids="item_ids_example",
        description="description_example",
        number_items="number_items_example",
        price="price_example",
        currency="USD",
        transaction_id="transaction_id_example",
        level="level_example",
        client_dedup_id="client_dedup_id_example",
        search_string="search_string_example",
        page_url="page_url_example",
        sign_up_method="sign_up_method_example",
        first_name="test_first",
        # hashed_first_name_sha="d99156483b6a99eb5f5a1707f7330e1c979a648b47a379d56a0d6850a9a9c76c"，
        # hashed_first_name_sdx="T231",
        middle_name="",
        # hashed_middle_name_sha="",
        # hashed_middle_name_sdx="",
        last_name="test_last",
        # hashed_last_name_sha="19fc3d9f9f6fad30ccbbebd51f67515dc95d8a5ef363fd35c34a2f47064d43bd",
        # hashed_last_name_sdx="T234",
        city="Los Angeles",
        # hashed_city_sha="9f2608067816e38c85edfb0c3985feff32def8b5dc17bb522ffc2e877e9b386b",
        # hashed_city_sdx="L252",
        state="CA",
        # hashed_state_sha="6959097001d10501ac7d54c0bdb8db61420f658f2922cc26e46d536119a31126",
        # hashed_state_sdx="C000",
        zip="00000",
        # hashed_zip="e7042ac7d09c7bc41c8cfa5749e41858f6980643bc0db1a83cc793d3e24d3f77",
        click_id="click_id_example",
    )
]

api_instance.send_events(events)

# (Optional) If you would like to get the async result
# async_res = api_instance.send_events(events);
# result = async_res.get();
```

### Sending Test Events
Snap’s Conversion API provides the validate, log, and stats endpoints for advertisers to test their events and obtain more information on how each of the test event was processed.

Creating and setting up a test event is the same as setting up to send a production event. Clients must simply call the SendTestEvent function instead of the production functions.

The stats and logs should be called after sending and receiving a successful response from the test event endpoint.

```
# sends single event to test endpoint synchronously
api_instance.send_test_event(event)

# (Optional) If you would like to get the synchronous request result
# res = api_instance.send_event(event);

# Example to grab the stats and logs
res_stats = api_instance.get_test_event_stats(pixel_id)
res_logs = api_instance.get_test_event_logs(pixel_id)
```

## Notes:
1) Initiate ConversionApi

```
api_instance = ConversionApi(
   access_token=access_token,
   # launchpad_url="TEST_LAUNCHPAD_URL"
)
```
   * if the Launch Pad has been set up under your domain. Conversion events will be forwarded to Snap transparently. (Other MPC features will be introduced in later versions).
   * Otherwise, you can initiate the instance using only the long lived token.Conversion events are sent back to Snap from the business SDK directly. 
   * It’s recommended to create a dedicated instance per thread to avoid any potential issues.
2) API Token
   * To use the Conversions API, you need to use the access token for auth. See [here](https://marketingapi.snapchat.com/docs/conversion.html#auth-requirements) to generate the token.
3) Build CapiEvent
   * Please check with the section [Conversion Parameters](https://marketingapi.snapchat.com/docs/conversion.html#additional-data-formatting-guidelines) and provide as much information as possible when creating the CapiEvent object.
   * At least one of the following parameters is required in order to successfully send events via the Conversions API. When possible, we recommend passing all of the below parameters to improve performance:
     * hashed_email
     * hashed_phone
     * hashed_ip and user_agent
     * hashed_mobile_ad_id
   * Any setter starting with the prefix of “hashed” (e.g. `hashedEmail()`) accepts the hashing PII value only (see [Data Hygiene](https://marketingapi.snapchat.com/docs/conversion.html#data-hygiene)). Please use the unhashed setter (e.g. `email()`) if you want the business sdk to normalize and hash the PII field on your behalf. 
   * We highly recommend passing cookie1 `uuid_c1`, if available, as this will increase your match rate. You can access a 1st party cookie by looking at the _scid value under your domain if you are using the Pixel SDK.
4) Send event(s) asynchronously
   * Conversion events can be sent individually via `api_instance.send_event(event)` 
   * Conversion events can be reported in batch using `api_instance.send_events(events)`  if they are buffered in your application. Please check example/send_events.py for more details. We recommend a 1000 QPS limit for sending us requests. You may send up to 2000 events per batch request, and can thus send up to 2M events/sec. Sending more than 2000 events per batch will result in a 400 error. 
   * Events are encapsulated in an asynchronous request in both solutions by which your application won’t be blocked. The response is logged by a default callback (under debugging mode) 
5) Test Events, Logs, and Stats
   * Conversion events can be sent for testing and validation via the `api_instance.send_test_event(event)`.
   * Conversion API also provides logging endpoint. It provides a summary of test CAPI events sent to the test endpoint within the past day
   * Conversion API’s stats endpoint provides basic stats and summary of the test events sent.
6) Debugging Mode
   * When debugging mode is turned on, we will log the events, api call response and exceptions using pythons logging library.
