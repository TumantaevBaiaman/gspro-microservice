from src.presentation.cli.user import app

if __name__ == "__main__":
    app()


"""
docker compose exec user_service \
  python cli.py \
  --email admin@mail.com \
  --password 123456 \
  --role admin
"""