from flask_testing import TestCase
from flask import current_app, url_for

from main import app

class MainTest(TestCase):
    def create_app(self):
        # Configure Flask to be in the testing environment
        app.config["TESTING"] = True

        # Deactivate the active session of a user (not use the token in WTF)
        app.config["WTF_CSRF_ENABLED"] = False

        return app
    
    # It is important to start with test_ to run the test correctly
    def test_app_exists(self):
        self.assertIsNotNone(current_app)
    
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))
        self.assertEquals(response.location, '/hello')
    
    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)
    
    def test_hello_post(self):
        response = self.client.post(url_for('wtf_form'))
        self.assertEquals(response.status_code, 405)
    
    def test_bad_post(self):
        fake_form = {"uuid": "0b435789-1eaf-43d0-888b-0c859369fc86",
                     "username": "123456",
                     "password": "FakePassword",
                     "email": "fulanito@gmail.com"}
        response = self.client.post(url_for('wtf_form'), data=fake_form)
        self.assertIsNone(response.location)
    
    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)
    
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))
        self.assert200(response)

    def test_auth_login_template(self):
        self.client.get(url_for('auth.login'))

        # This test only needs the name, it is for that reason that the response
        # is not being stored
        self.assertTemplateUsed('login.html')
    
    def test_auth_login_form(self):
        fake_form = {"uuid": "0b435789-1eaf-43d0-888b-0c859369fc86",
                     "username": "FakeUsername",
                     "password": "FakePassword",
                     "email": "fulanito@gmail.com"}
        response = self.client.post(url_for('auth.login'), data=fake_form)
        self.assertEquals(response.location, '/auth/hello')