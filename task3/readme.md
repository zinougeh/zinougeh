How to run it 

install pip3 install flask requests

To get data run python3 3a-fetch-api.py

it will create posts.csv file


To run api run python3 3b-update-csv.py

Open another terminal to PUT or POST and see updates on posts.csv file
This will update first entry
curl -X PATCH -H "Content-Type: application/json" -d '{"title": "Updated Title"}' http://127.0.0.1:5000/api/record/1

This will add new record at last line of id 101
curl -X POST -H "Content-Type: application/json" -d '{"id": 2, "title": "New Title", "body": "New Body Content"}' http://127.0.0.1:5000/api/record/101