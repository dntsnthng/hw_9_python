from selene.support.shared import browser

from demoqa_tests.model.components import Panel
from demoqa_tests.model.pages.profile_page import ProfilePage
from demoqa_tests.model.pages.RegistrationPage import (
    RegistrationPage,
)


class Application:
    def __init__(self):
        self.registration = RegistrationPage()
        self.profile = ProfilePage()
        self.panel = Panel()

    def open(self):
        browser.open('/')
        return self


app = Application()
