import os

from selene import browser, be, have

import tests


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def select_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    def select_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_picture(self, value):
        browser.element("#uploadPicture").set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f'resources/{value}')
            )
        )

    def insert_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def select_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def submit(self):
        browser.element('#submit').press_enter()

    def check_submitting_the_form(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def check_input_data(self, first_name, last_name, email, gender,
                                                   number, date, subject, hobby,
                                                   picture, address, state, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts((f'{first_name}, {last_name}', email, gender,
                                                   number,date, subject, hobby,
                                                   picture,
                                                   address, f'{state} {city}')))

    print("Выполнено успешно")
