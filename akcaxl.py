from ciscoaxl import axl

import os
from dotenv import load_dotenv
load_dotenv()

ucm = axl(username=os.getenv('username'),password=os.getenv('password'),cucm=os.getenv('cucm'),cucm_version=os.getenv('version'))

# Fields are filtered by default but if you need additional fields returned, add tagfilter={}
# for phone in ucm.get_phones(tagfilter={ "name": "",
#             "product": "",
#             "description": "",
#             "protocol": "",
#             "locationName": "",
#             "callingSearchSpaceName": "",
#             "devicePoolName": ""
#             }):
#     print(phone)

# # Get all phones with the name and descriptions
# for phone in ucm.get_phones():
#     print(f'{phone.name} --> {phone.description}')

# # Get all users
# for user in ucm.get_users():
#     print(f'{user.firstName}{user.lastName} --> {user.userid}')  

# # Get specific user
# user = ucm.get_user(userid='DGamboa')
# print(user)

# # Get specific phone
# phone = ucm.get_phone(name='SEPCC9891D08480')
# print (phone)

# # Get Directory Numbers
# for dn in ucm.get_directory_numbers():
#     print(f'{dn.pattern}:{dn.description}')
# # hot to sort results?

# Get user device profiles
# for udp in ucm.get_device_profiles():
#     print(udp.name)
# this didnt work on my environment