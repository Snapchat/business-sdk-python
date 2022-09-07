from snap_business_sdk.model.capi_event import CapiEvent
from snap_business_sdk.public.conversion_api import ConversionApi
from snap_business_sdk.capi_utils import (
    norm_and_hash_string,
    norm_and_soundex_string,
    norm_and_hash_phone_number
)

# conversion event integration
INTEGRATION = "business-sdk"


class ConversionEvent(object):
    norm_and_hash_string_vars = {
        "email": "hashed_email",
        "mobile_ad_id": "hashed_mobile_ad_id",
        "idfv": "hashed_idfv",
        "ip_address": "hashed_ip_address",
        "first_name": "hashed_first_name_sha",
        "middle_name": "hashed_middle_name_sha",
        "last_name": "hashed_last_name_sha",
        "city": "hashed_city_sha",
        "state": "hashed_state_sha",
        "zip": "hashed_zip"
    }

    norm_and_hash_phone_number_vars = {
        "phone_number": "hashed_phone_number"
    }

    @classmethod
    def norm_and_hash_var(cls, var_name, var_value):
        if var_name in cls.norm_and_hash_string_vars:
            return [cls.norm_and_hash_string_vars.get(var_name), norm_and_hash_string(var_value)]
        elif var_name in cls.norm_and_hash_phone_number_vars:
            return [cls.norm_and_hash_phone_number_vars.get(var_name), norm_and_hash_phone_number(var_value)]
        else:
            return [var_name, var_value]

    norm_and_soundex_string_vars = {
        "first_name": "hashed_first_name_sdx",
        "middle_name": "hashed_middle_name_sdx",
        "last_name": "hashed_last_name_sdx",
        "city": "hashed_city_sdx",
        "state": "hashed_state_sdx",
    }

    @classmethod
    def norm_and_soundex_var(cls, var_name, var_value):
        if var_name in cls.norm_and_soundex_string_vars:
            return [cls.norm_and_soundex_string_vars.get(var_name), norm_and_soundex_string(var_value)]
        else:
            return [var_name, var_value]

    @classmethod
    def norm_and_hash(cls, **kwargs):
        # set integration to business-sdk
        kwargs.setdefault("integration", INTEGRATION)

        # normalize and hash some variables if plaintext is passed in
        for var_name, var_value in list(kwargs.items()):
            hashed_name, hashed_val = cls.norm_and_hash_var(var_name, var_value)
            if hashed_name != var_name:
                kwargs.setdefault(hashed_name, hashed_val)
                if kwargs.get(var_name) is not None:
                    kwargs.pop(var_name)  # remove the plaintext one

            soundex_name, soundex_val = cls.norm_and_soundex_var(var_name, var_value)
            if soundex_name != var_name:
                kwargs.setdefault(soundex_name, soundex_val)
                if kwargs.get(var_name) is not None:
                    kwargs.pop(var_name)  # remove the plaintext one
        return kwargs

    def __init__(self, *args, **kwargs):
        # normalize and hash the event
        kwargs = self.norm_and_hash(**kwargs)

        self.capiEvent = None
        try:
            self.capiEvent = CapiEvent(*args, **kwargs)
        except Exception as e:
            ConversionApi.error("Error creating event {event} \nReason: {err}".format(event=kwargs, err=e.__str__()))

    def getCapiEvent(self):
        return self.capiEvent
