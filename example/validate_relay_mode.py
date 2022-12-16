import json
import subprocess
import time
import string
import random
import sys
import urllib3
from snap_business_sdk.public.conversion_api import ConversionApi
from snap_business_sdk.public.conversion_event import ConversionEvent

# Please modify the placeholders below.
access_token = 'INSERT_YOUR_API_TOKEN'
pixel_id = 'INSERT_YOUR_PIXEL_ID'
launchpad_url = 'INSERT_YOUR_LAUNCHPAD_URL'

# Ping the health check endpoint
http = urllib3.PoolManager()
hc_path = launchpad_url + '/health'
health_check = http.request('GET', hc_path)
print("[STEP 1/4] Health check on %s: [%d]\n" % (hc_path, health_check.status))

# send mocking pixel event
headers = {
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'http://localhost:10001/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Content-Type': 'application/json',
}

json_data = {
    'pid': '194e8c7a-0334-4401-8c48-4c2bd7029d83',
    'ev': 'VIEW_CONTENT',
    'e_iids': [
        '14',
    ],
    'pl': 'http://localhost:10001/product.html',
    'bt': '__B_TAG__',
    'if': False,
    'm_dcl': 346,
    'm_fcps': 336,
    'm_pi': 342,
    'm_pl': 0,
    'm_pv': 'v2',
    'm_rd': 531,
    'm_sl': 364,
    'rf': 'http://localhost:10001/',
    'trackId': '41ee5af1-1a0e-48d7-b13b-75687418ff71',
    'ts': 1668449199558,
    'u_c1': 'ad63a442-690c-4973-a3ce-cae797c1a8af',
    'u_sclid': '2122ea9e-bec4-4dd2-99b1-cd2da04bb0b1',
    'u_scsid': 'd7878845-8bd1-405e-9755-ee21438abb9a',
    'v': '2.0.0',
}

p_path = launchpad_url + '/gateway/p'
response = http.request('POST',  p_path, headers=headers, body=json.dumps(json_data))
print("[STEP 2/4] Send a mocking pixel event to %s: [%d]\n" % (p_path, response.status))


# Create an instance of the API class
api_instance = ConversionApi(
    access_token=access_token,
    launchpad_url=launchpad_url
)

gen_hashed_email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=64))
gen_timestamp = str(round(time.time() * 1000.0))

event = ConversionEvent(
    pixel_id=pixel_id,
    event_type="PURCHASE",
    event_conversion_type="WEB",
    event_tag="event_tag_example",
    timestamp=gen_timestamp,
    uuid_c1="34dd6077-e3a0-4b1c-9f91-a690ea0e335d",
    hashed_email=gen_hashed_email,

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

# sends single event to test endpoint synchronously
print("[Step 3/4] Sending a mocking CAPI event with the random fields below ... ")
print("\ttimestamp = %s\n\thashed_email = %s\n" % (gen_timestamp, gen_hashed_email))
res = api_instance.send_test_event(event)

if res.status != 'SUCCESS':
    print(res.error_message)

else:
    countdown = 30
    print("Please wait for %ss before querying the logs endpoint." % countdown)
    for remaining in range(countdown, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n\n")

    api_instance.get_test_event_stats(pixel_id)
    logs = api_instance.get_test_event_logs(pixel_id)

    for log in logs['logs']:
        if log['event_metadata']['hashed_email'] == gen_hashed_email:
            def color(s):
                return '\x1b[6;30;42m' + s + '\x1b[0m'

            log_str = log.to_str() \
                .replace(gen_timestamp, color(gen_timestamp)) \
                .replace(gen_hashed_email, color(gen_hashed_email))

            print("[Step 4/4] Succeeded! Found a log record with the matched timestamp and hashed_email.\n%s" % log_str)
            break
        else:
            print('[Step 4/4] Failed to find any matched log record.')



