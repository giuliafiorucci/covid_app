from src.appdash.main import app


class TestApp:
    def test_app_layout(self):
        assert app.layout is not None
