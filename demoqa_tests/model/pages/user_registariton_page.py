from demoqa_tests.model.pages.profile_page import ProfilePage


class: RegistrationPage:
    def __init__(self, profile_page: ProfilePage):
        self.name = profile_page.name
        self.email = profile_page.email
        self.gender = profile_page.gender
        self.number = profile_page.number
        self.date_of_birth = profile_page.date_of_birth
        self.subject = profile_page.subject
        self.hobby = profile_page.hobby
        self.photo = profile_page.photo
        self.address = profile_page.address
        self.city = profile_page.city
        self.state = profile_page.state


    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, name):
        self.first_name.type(name)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_state(self, state):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()
        return self



    def fill_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
        return self

    def fill_number(self, number):
        browser.element('#userNumber').type(number)
        return self

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self

    def fill_hobbies(self, hobby):
        browser.all('.custom-checkbox').element_by(have.exact_text(hobby)).click()
        return self

    def fill_picture(self, hobby):
        browser.element('#uploadPicture').set_value(resource.path(value))
        return self

    def fill_address(self, adress):
        browser.element('#currentAddress').type(adress)
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def summits(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def should_have_submited(self, full_name, email):
        pass


def should_registered_user_with(self, full_name, email, gender, number, date_of_birth, subject, hobby, photo, address,
                                city, state):
    # todo: refactor to reuse parameters
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            full_name,
            email,
            gender,
            number,
            date_of_birth,
            subject,
            hobby,
            photo,
            address,
            city,
            state
        )
    )
    return self

def register(self):
    SimpleUserRegistrationPage()
    return self
