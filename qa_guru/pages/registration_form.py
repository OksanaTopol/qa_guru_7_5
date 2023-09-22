import os

from selene import browser, be, have


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

    def select_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self):
        browser.element('#dateOfBirthInput').click()
        browser.element(".react-datepicker__month-select>option[value='1']").click()
        browser.element(".react-datepicker__year-select>option[value='1999']").click()
        browser.element('.react-datepicker__day--019').click()

    def select_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    def select_hobbies(self):
        browser.element("[for='hobbies-checkbox-3']").click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(value))

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

    def check_input_data(self):
        browser.element('.table').should(have.text('test_name test_lastName' and 'test@mail.com' and 'Male' and
                                                   '1234567890' and '1 January,1999' and 'Maths' and 'Music' and
                                                   'cat.png' and
                                                   'test' and 'NCR Delhi'))

    print("Выполнено успешно")
