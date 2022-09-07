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

event = ConversionEvent(
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
)

# sends single event in synchronous mode
api_instance.send_event_sync(event)

# (Optional) If you would like to get the sync result
# res = api_instance.send_event(event);
