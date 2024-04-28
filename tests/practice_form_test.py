from selene.support.shared import browser
from selene import have
from selene import command
from demoqa_tests import resource
from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import user


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name(user.name).fill_last_name('YA')
    registration_page.fill_email(user.email)
    registration_page.fill_gender(user.gender)
    registration_page.fill_number(user.number)
    registration_page.fill_subject(user.subject)
    registration_page.fill_date_of_birth('1999', 'May', '11')
    registration_page.fill_hobbies(user.hobby)
    registration_page.fill_picture('foto.jpg')
    registration_page.fill_address('Moscowskaya Street 18')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')
    registration_page.submits()

    # THEN
    registration_page.should_registered_user_with(
        'Yasha YA',
        'name@example.com',
        'Female',
        '1234567891',
        '11 May,1999',
        'Computer Science',
        'Reading',
        'foto.jpg',
        'Moscowskaya Street 18',
        'NCR Delhi',
    )

    '''
    # example of implementing assertion-free pageobjects
    registration_page.registered_user_data.should(
        have.exact_texts(
            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science',
            'Reading',
            'foto.jpg',
            'Moscowskaya Street 18',
            'NCR Delhi',
        )
    )
    '''
