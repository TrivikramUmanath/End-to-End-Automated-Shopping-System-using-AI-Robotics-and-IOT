from firebase import firebase

url='https://testproject-6b442.firebaseio.com/'
firebase=firebase.FirebaseApplication(url)
result=firebase.put("/Test Val","Value",200)
print(result)

data=firebase.get('/Member',None)
print(data)
