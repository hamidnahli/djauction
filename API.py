import requests

response = requests.post(
    url='http://127.0.0.1:8000/api/auth/register',
    json={
        "email": "user1@1234563.com",
        "username": "user1732156_853",
        "password": "1231231323",
        "first_name": "Chone",
        "last_name": "Spipah",
        "address": "4282 43 SW",
        "city": "Tacoma",
        "country": "USA",
        "zipcode": "12-2142",
        "phone": "+6778887788"
    }
)
json_data = {
    'status': 'success',
    'username': 'user1732156_853',
    'email': 'user1@1234563.com',
    'first_name': 'Chone',
    'last_name': 'Spipah',
    'address': '4282 43 SW',
    'zipcode': '12-2142',
    'city': 'Tacoma',
    'phone': '+6778887788',
    'country': 'USA'
}

response = requests.post(
    url='http://127.0.0.1:8000/api/auth/login',
    json={
        "email": "user1@123456.com",
        "username": "user1732156_85",
        "password": "1231231323"

    }
)

response = requests.post(
    url='http://127.0.0.1:8000/api/auth/token/token_verify',
    json={
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyODA0MjE4LCJpYXQiOjE2NTI4MDA2MTgsImp0aSI6ImU1ZTk0MDEwOTQ2MzQ5Mjk5MjE3MThkNjM4MWY4ODQ0IiwiaWQiOjEzLCJ1c2VybmFtZSI6InVzZXIxNzMyMTU2Xzg1IiwiZW1haWwiOiJ1c2VyMUAxMjM0NTYuY29tIiwiZmlyc3RfbmFtZSI6IkNob25lIiwibGFzdF9uYW1lIjoiViIsImFkZHJlc3MiOiI0MjgyIDQzIFNXIiwiemlwY29kZSI6IjEyLTIxNDIiLCJjaXR5IjoiVGFjb21hIiwicGhvbmUiOiIrMjEyNjc3ODg4Nzc4OCIsImNvdW50cnkiOiJVU0EifQ.jDBlj3UXnKfncuWXBsseVexgtb-9Td3asd4CaXof3xw"
    }
)

response = requests.get(
    url='http://127.0.0.1:8000/api/account/user/13/info',
    headers={
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyODA0MjE4LCJpYXQiOjE2NTI4MDA2MTgsImp0aSI6ImU1ZTk0MDEwOTQ2MzQ5Mjk5MjE3MThkNjM4MWY4ODQ0IiwiaWQiOjEzLCJ1c2VybmFtZSI6InVzZXIxNzMyMTU2Xzg1IiwiZW1haWwiOiJ1c2VyMUAxMjM0NTYuY29tIiwiZmlyc3RfbmFtZSI6IkNob25lIiwibGFzdF9uYW1lIjoiViIsImFkZHJlc3MiOiI0MjgyIDQzIFNXIiwiemlwY29kZSI6IjEyLTIxNDIiLCJjaXR5IjoiVGFjb21hIiwicGhvbmUiOiIrMjEyNjc3ODg4Nzc4OCIsImNvdW50cnkiOiJVU0EifQ.jDBlj3UXnKfncuWXBsseVexgtb-9Td3asd4CaXof3xw'},

)

response = requests.patch(
    url='http://127.0.0.1:8000/api/account/user/update/13',
    headers={
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyODA0MjE4LCJpYXQiOjE2NTI4MDA2MTgsImp0aSI6ImU1ZTk0MDEwOTQ2MzQ5Mjk5MjE3MThkNjM4MWY4ODQ0IiwiaWQiOjEzLCJ1c2VybmFtZSI6InVzZXIxNzMyMTU2Xzg1IiwiZW1haWwiOiJ1c2VyMUAxMjM0NTYuY29tIiwiZmlyc3RfbmFtZSI6IkNob25lIiwibGFzdF9uYW1lIjoiViIsImFkZHJlc3MiOiI0MjgyIDQzIFNXIiwiemlwY29kZSI6IjEyLTIxNDIiLCJjaXR5IjoiVGFjb21hIiwicGhvbmUiOiIrMjEyNjc3ODg4Nzc4OCIsImNvdW50cnkiOiJVU0EifQ.jDBlj3UXnKfncuWXBsseVexgtb-9Td3asd4CaXof3xw'},
    json={
        "title": "Dr.p.",
        "company": "SCC",
        "office_phone": "2060022002"

    }
)

response = requests.patch(
    url='http://127.0.0.1:8000/api/account/user/changepassword/13',
    headers={
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyODA0MjE4LCJpYXQiOjE2NTI4MDA2MTgsImp0aSI6ImU1ZTk0MDEwOTQ2MzQ5Mjk5MjE3MThkNjM4MWY4ODQ0IiwiaWQiOjEzLCJ1c2VybmFtZSI6InVzZXIxNzMyMTU2Xzg1IiwiZW1haWwiOiJ1c2VyMUAxMjM0NTYuY29tIiwiZmlyc3RfbmFtZSI6IkNob25lIiwibGFzdF9uYW1lIjoiViIsImFkZHJlc3MiOiI0MjgyIDQzIFNXIiwiemlwY29kZSI6IjEyLTIxNDIiLCJjaXR5IjoiVGFjb21hIiwicGhvbmUiOiIrMjEyNjc3ODg4Nzc4OCIsImNvdW50cnkiOiJVU0EifQ.jDBlj3UXnKfncuWXBsseVexgtb-9Td3asd4CaXof3xw'},
    json={
        "password": "1231231323",
        "password2": "1231231323",
        "old_password": "gsd1231231323"
    }
)
