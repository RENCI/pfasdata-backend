# gunicorn_config.py

bind = "0.0.0.0:8000"
module = "pfasdata.wsgi:application"

workers = 4  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

certfile = "/etc/ssl/SSL.crt"
keyfile = "/etc/ssl/SSL.key"
