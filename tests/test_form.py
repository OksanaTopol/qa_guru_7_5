import allure
from allure_commons.types import Severity

from qa_guru.data.user import User
from qa_guru.pages.registration_form import RegistrationPage


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'aksana')
@allure.feature('Allure')
@allure.story('Allure with steps')
def test_form_submission(setup_browser):
    student = User(first_name='test_name',
                   last_name='test_lastName',
                   email='test@mail.com',
                   gender='Male',
                   number='1234567890',
                   date_of_birth_day='01',
                   date_of_birth_month='January',
                   date_of_birth_year='1999',
                   subject='Maths',
                   hobby='Music',
                   picture='cat.png',
                   address='test',
                   state='NCR',
                   city='Delhi',
                   )
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_form(student)
    registration_page.submit()
    registration_page.check_submitting_the_form()
    registration_page.check_input_data(student)

    print("Выполнено успешно")
