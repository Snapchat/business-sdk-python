"""
Conversion API Client
"""
import multiprocessing
import logging
from snap_business_sdk.api.default_api import DefaultApi
from snap_business_sdk.api_client import ApiClient, Configuration
from snap_business_sdk.capi_utils import (
    is_empty_string,
    ErrorCallback
)

SDK_LANGAUGE = "python"
SDK_VERSION = "1.0.0"
API_VERSION = "v2"

# headers
HEADER_SDK_VERSION = "X-CAPI-BusinessSDK"
HEADER_CAPI_PATH = "X-CAPI-Path"

# user agent
USER_AGENT = "BusinessSDK/Python/{sdk_version}".format(sdk_version=SDK_VERSION)
USER_AGENT_WITH_PAD = "{user_agent} (LaunchPAD)".format(user_agent=USER_AGENT)

# capi url
PROD_URL = "https://tr.snapchat.com/{api_version}".format(api_version=API_VERSION)
STAGING_URL = "https://tr-shadow.snapchat.com/{api_version}".format(api_version=API_VERSION)

# Add task to the set. This creates a strong reference.
background_tasks = set()


class ConversionApi(object):
    logger = None

    def __init__(self, access_token=None, launchpad_url=None):
        self.configuration = Configuration(
            access_token=access_token,
            host=launchpad_url
        )

        self.api_client = ApiClient(self.configuration)
        # Set header
        # User-Agent: BusinessSDK/Python/{sdk-version}
        self.api_client.user_agent = USER_AGENT
        # X-CAPI-BusinessSDK: python/{sdk-version}
        self.api_client.set_default_header(
            HEADER_SDK_VERSION,
            '{sdk_language}/{sdk_version}'.format(sdk_language=SDK_LANGAUGE, sdk_version=SDK_VERSION))

        # Create default api instance
        self.default_api = DefaultApi(self.api_client)

    @classmethod
    def set_debug_mode(cls, enabled=False):
        # disable logging
        if not enabled:
            cls.logger = None
            return

        # set default basic logger
        logging.basicConfig(format='%(asctime)s %(levelname)s \n%(message)s', datefmt='%H:%M:%S')
        cls.logger = logging.getLogger(__name__)
        cls.logger.setLevel(logging.INFO)

    @classmethod
    def log(cls, info):
        if cls.logger is not None:
            cls.logger.info(info)

    @classmethod
    def warn(cls, info):
        if cls.logger is not None:
            cls.logger.warn(info)

    @classmethod
    def error(cls, info):
        if cls.logger is not None:
            cls.logger.error(info)

    @classmethod
    def validate_and_create_events(cls, raw_events):
        # validate and convert raw events to capi events
        capi_events = list(map(lambda event: (None if event is None else event.getCapiEvent()), raw_events))
        # filter all events that are invalid (None)
        capi_events = list(filter(lambda event: event is not None, capi_events))
        return capi_events

    def logEvents(self, capi_events):
        ConversionApi.log(
            'Host: {host} '
            '\nAccess_token: {access_token} '
            '\nHeaders: {headers} '
            '\nConversion events: {events}'.format(
                host=self.default_api.api_client.configuration.host,
                access_token=self.default_api.api_client.configuration.access_token,
                headers=self.default_api.api_client.default_headers,
                events=capi_events
            )
        )

    def send_test_event(self, raw_event):
        self.send_test_events([raw_event])

    def send_test_events(self, raw_events):
        if raw_events is None:
            resp = ErrorCallback('Conversion event cannot be empty')
            ConversionApi.error('Send Test Exception: {message}'.format(message=resp.get()))
            return resp

        # validate event attributes
        capi_events = self.validate_and_create_events(raw_events)

        # log events
        self.logEvents(capi_events)

        try:
            resp = self.default_api.send_test_data(body=capi_events)
            ConversionApi.log('Send Test Result: {resp}'.format(resp=resp))
        except Exception as e:
            resp = ErrorCallback(e.__str__())
            ConversionApi.error('Send Test Exception: {message}'.format(message=e.__str__()))

        return resp

    def get_test_event_logs(self, asset_id):
        try:
            resp = self.default_api.conversion_validate_logs(asset_id=asset_id)
            ConversionApi.log('Get Test Logs Result: {resp}'.format(resp=resp))
        except Exception as e:
            resp = ErrorCallback(e.__str__())
            ConversionApi.error('Get Test Logs Exception: {message}'.format(message=e.__str__()))
        return resp

    def get_test_event_stats(self, asset_id):
        try:
            resp = self.default_api.conversion_validate_stats(asset_id=asset_id)
            ConversionApi.log('Get Test Stats Result: {resp}'.format(resp=resp))
        except Exception as e:
            resp = ErrorCallback(e.__str__())
            ConversionApi.error('Get Test Stats Exception: {message}'.format(message=e.__str__()))
        return resp

    # send single event in synchronous mode
    def send_event_sync(self, raw_event):
        return self.send_events_sync([raw_event])

    # send multiple events in synchronous mode
    def send_events_sync(self, raw_events):
        return self.send_events(raw_events, async_req=False)

    # send single event in asynchronous mode
    def send_event(self, raw_event):
        return self.send_events([raw_event])

    # send multiple events in asynchronous mode
    def send_events(self, raw_events, async_req=True):
        if raw_events is None:
            resp = ErrorCallback('Conversion event cannot be empty')
            ConversionApi.error('Exception: {message}'.format(message=resp.get()))
            return resp

        # validate event attributes
        capi_events = self.validate_and_create_events(raw_events)

        # log events
        self.logEvents(capi_events)

        try:
            resp = self.default_api.send_data(body=capi_events, async_req=async_req)
            ConversionApi.log('Result: {resp}'.format(resp=resp))
        except Exception as e:
            resp = ErrorCallback(e.__str__())
            ConversionApi.error('Exception: {message}'.format(message=e.__str__()))
        return resp

