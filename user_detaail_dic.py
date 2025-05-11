'''Q2: WAP to create dictionary containing user details , access each
details manually using keys &amp; via loop?'''

user_detail  = {

    "name" : "username",
    "age" : "userage",
    "number":9754337511,
    "gender":"M/F",
    "aadar no":1234567890,
    "city":"indore"

}

print("name",user_detail["name"])
print("age",user_detail["age"])
print("number",user_detail["number"])
print("gender",user_detail["gender"])
print("aadar no",user_detail["aadar no"])
print("city",user_detail["city"])
print("thanks for access this dictionary")




for key in user_detail:
    print(f"{key.capitalize()}: {user_detail[key]}")