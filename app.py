from app import create_app
from app.logger import logger

app = create_app()

if __name__ == '__main__':
    logger.info("Starting the application.")
    app.run(port=3000, debug=True)
