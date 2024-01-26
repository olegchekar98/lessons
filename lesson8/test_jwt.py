import jwt
import datetime


encoded_jwt = jwt.encode({'date': str(datetime.datetime.now())}, 'secret', algorithm='HS256')


print(encoded_jwt)

decoded = jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])

print(decoded)