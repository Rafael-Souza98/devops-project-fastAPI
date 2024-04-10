from application import create_app
from config import ProdConfig, DevConfig
import os


if os.getenv('FLASK_ENV') == "development":
    app = create_app(DevConfig)
else:
    app = create_app(ProdConfig)


if __name__ == "__main__":
    app.run("0.0.0.0", port=os.getenv('PORT', 5000), debug=False)