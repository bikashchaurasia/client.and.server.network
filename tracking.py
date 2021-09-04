import phonenumbers
from phonenumbers import geocoder
phone_numbers1 = phonenumbers.parse("+918809487041")
phone_numbers2 = phonenumbers.parse("+4930901820")
phone_numbers3 = phonenumbers.parse("+13478439904")
print(geocoder.description_for_number(phone_numbers1 , "en"))
print(geocoder.description_for_number(phone_numbers2 , "en"))
print(geocoder.description_for_number(phone_numbers3 , "en"))



