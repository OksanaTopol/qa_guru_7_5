import os

from selene import browser
from selene.support.conditions import have, be


def test_form_submission(setup_browser):
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')
    browser.element('#firstName').should(be.blank).type('test_name')
    browser.element('#lastName').should(be.blank).type('test_lastName')
    browser.element('#userEmail').should(be.blank).type('test@mail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__month-select>option[value='1']").click()
    browser.element(".react-datepicker__year-select>option[value='1999']").click()
    browser.element('.react-datepicker__day--019').click()
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/cat.png'))
    browser.element('#currentAddress').type("test")
    browser.element('#react-select-3-input').type('ncr').press_enter()
    browser.element('#react-select-4-input').type('delhi').press_enter()
    browser.element('#submit').press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('test_name test_lastName' and 'test@mail.com' and 'Male' and
                                               '1234567890' and '1 January,1999' and 'Maths' and 'Music' and
                                               'cat.png' and
                                               'test' and 'NCR Delhi'))
    print("Выполнено успешно")