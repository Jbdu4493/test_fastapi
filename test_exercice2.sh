echo -n "\n --------------All user------------- \n"
curl -X GET -i 'http://127.0.0.1:8000/users'

echo -n "\n --------------Add user 1------------- \n"

curl -X 'POST' -i \
  'http://127.0.0.1:8000/users' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "name": "Jonathan",
  "age": 34
}'

echo -n "\n --------------Add user 2------------- \n"
curl -X 'POST' -i \
  'http://127.0.0.1:8000/users' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 2,
  "name": "Jonhs"
}'

echo -n "\n -----------------All user------------ \n"
curl -X GET -i 'http://127.0.0.1:8000/users'

echo -n "\n -----------------delete user 1------------ \n"
curl -X "DELETE" -i 'http://127.0.0.1:8000/users/1'

echo -n "\n -----------------All user------------ \n"
curl -X GET -i 'http://127.0.0.1:8000/users'

echo -n "\n -----------------Update user------------ \n"
curl -X 'POST' -i 'http://127.0.0.1:8000/users/2' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 2,
  "name": "Dorothee",
  "age": 42
  }'


curl -X GET -i 'http://127.0.0.1:8000/users'
echo -n "\n -----------------Header ------------ \n"
curl -X GET -i http://127.0.0.1:8000/header  -H 'usr: joe anne' -H 'pwd: biz efe' 