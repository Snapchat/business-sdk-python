"""
Capi utils including constants and hash functions
"""
import hashlib
import re
import jellyfish

# phone number patterns
phone_number_ptn_str1 = "^((\\+|00)(\\d+)[\\-\\s])?0?(.+)"
phone_number_ptn_str2 = "[^\\d.]"


def is_empty_string(input_str):
    return input_str is None or input_str.strip() == ""


def sha256(input_string):
    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()


def soundex(input_string):
    return jellyfish.soundex(input_string)


def norm_and_hash_string(input_str):
    if is_empty_string(input_str):
        return ""
    return sha256(input_str.strip().lower())


def norm_and_soundex_string(input_str):
    if is_empty_string(input_str):
        return ""
    return soundex(input_str.strip().lower())


def norm_and_hash_phone_number(phone_number):
    if is_empty_string(phone_number):
        return ""
    return sha256(normalize_phone_num(phone_number))


def normalize_phone_num(phone_number):
    if is_empty_string(phone_number):
        return ""
    match = re.search(phone_number_ptn_str1, phone_number)
    if match:
        country_code = match.group(3)
        num = match.group(4)

        if country_code is not None:
            country_code = re.sub(phone_number_ptn_str2, "", country_code)

        if num is not None:
            num = re.sub(phone_number_ptn_str2, "", num)

        if country_code is None or country_code.strip() == "":
            country_code = "1"

        if num is not None:
            return country_code + num

    return ""


class ErrorCallback(object):
    def __init__(self, error_message):
        self.error_message = error_message
        self.status = "ERROR"

    def get(self):
        return {
            "reason": self.error_message,
            "status": self.status
        }
