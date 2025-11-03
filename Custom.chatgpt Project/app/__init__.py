from flask import Flask

def create_app():
    # ✅ Create the Flask app instance
    app = Flask(
        __name__,
        static_folder="static",        # folder for CSS, JS, images
        template_folder="templates"    # folder for chat.html
    )

    # ✅ Import and register blueprint
    from app.routes.main import main
    app.register_blueprint(main)

    # ✅ Return the app instance
    return app
