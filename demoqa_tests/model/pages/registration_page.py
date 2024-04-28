from selene import have, command
from selene.support.shared import browser
from demoqa_tests import resource
from demoqa_tests.data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.state = browser.element('#state')



    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self
    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def should_registered_user_with(self,  user: User):
        # todo: refactor to reuse parameters
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                user.name,
                user.email,
                user.gender,
                user.number,
                user.date_of_birth,
                user.subject,
                user.hobby,
                user.photo,
                user.address,
                user.city,
                user.state
            )
        )
        return self

    def fill_gender(self, gender: str):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()
        return self

    def fill_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def fill_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def fill_picture(self,value):
        browser.element('#uploadPicture').set_value(resource.path(value))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def submits(self):
        browser.element('#submit').perform(command.js.click)
        return self
    
    def register(self, user: User):
        self.fill_first_name(user.name).fill_last_name('YA')
        self.fill_email(user.email)
        self.fill_gender(user.gender)
        self.fill_number(user.number)
        self.fill_subject(user.subject)
        self.fill_date_of_birth('1999', 'May', '11')
        self.fill_hobbies(user.hobby)
        self.fill_picture('foto.jpg')
        self.fill_address('Moscowskaya Street 18')
        self.fill_state('NCR')
        self.fill_city('Delhi')
        self.submits()
        
        
        
        