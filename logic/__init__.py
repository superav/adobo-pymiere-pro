from app import create_app

flask_app = create_app()
flask_app.run(host='0.0.0.0')