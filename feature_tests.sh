pip3 install -r requirements.txt
python3.8 -m logic.flask_create > log.txt 2>&1 &
until answ1=$(curl --silent --location --request POST 'localhost:5000/logic/image_editor' --header 'Content-Type: application/json' --data-raw '{"effect": "hue", "image_name": "image", "file_extension": "png", "is_working_copy": false, "specifications": 180}'); do
	printf '.'
	sleep 1
done
echo $answ1

answ2=$(curl --silent --location --request POST 'localhost:5000/logic/image_editor' --header 'Content-Type: application/json' --data-raw '{"effect": "red-eye-remover", "image_name": "redeye", "file_extension": "png", "is_working_copy": false, "specifications": [35, 110, 150, 150]'})

echo $answ2

answ3=$(curl --silent --location --request POST 'localhost:5000/logic/image_editor' --header 'Content-Type: application/json' --data-raw '{"effect": "vignette", "image_name": "image", "file_extension": "png", "is_working_copy": false'})

echo $answ3

answ4=$(curl --silent --location --request POST 'localhost:5000/logic/nst' --header 'Content-Type: application/json' --data-raw '{"effect": "nst", "image_name": "image", "file_extension": "png", "is_working_copy": false, "nst_type": blank1, "input_image_url": blank2, "filter_image_url": blank3'})

python3.8 -m tests.test_url_editted $answ1 $answ2 $answ3 $answ4

kill $(pgrep -f python3.8)
