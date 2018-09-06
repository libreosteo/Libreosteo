# -*- coding: robot -*-
*** Settings ***
Resource   resources.txt

*** Variables ***
${OFFICE_ADDRESS_STREET}        27 rue Haute
${OFFICE_ADDRESS_COMPLEMENT}
${OFFICE_ADDRESS_ZIPCODE}       87110
${OFFICE_ADDRESS_CITY}          Le Vigen
${OFFICE_ADDRESS_PHONE}         05 55 12 13 14
${OFFICE_SIRET}                 52282868700022
${OFFICE_AMOUNT}                55
${OFFICE_CURRENCY}              EUR
${INVOICE_OFFICE_HEADER}        Cabinet 1
${INVOICE_CONTENT}              Template with <amount> <currency>
${INVOICE_FOOTER}               Footer

*** Test Cases ***

Open Settings
  [Documentation]   login a user and check that the user is asked to setup the office
  Open Browser To Login Page 
  Title Should Be     Signin on Libreosteo
  Login with      test   test
  Title Should Be     Libreosteo
  Element Should Not Be Visible     class:alert-danger
  Wait Until Element Is Enabled     jquery:div.popover-content
  Element Should Contain            jquery:div.popover-content      ADELI
  Element Should Be Visible         jquery:ul.dropdown-user
  Edit Settings
  Check Rest Settings
  [TearDown]    Close Browser


*** Keywords ***
Login With
  [Arguments]   ${login}  ${password}
  Input Text    username  ${login}
  Input Text    password    ${password}
  Click Button  login

Edit Settings
  Click Element                   jquery:li.open
  Click Element                   jquery:li#office-settings
  Wait Until Element Contains     jquery:h1.page-header         Office settings
  Input Text                      office_address_street         ${OFFICE_ADDRESS_STREET}
  Input Text                      office_address_complement     ${OFFICE_ADDRESS_COMPLEMENT}
  Input Text                      office_address_zipcode                ${OFFICE_ADDRESS_ZIPCODE}
  Input Text                      office_address_city           ${OFFICE_ADDRESS_CITY}
  Input Text                      office_phone                  ${OFFICE_ADDRESS_PHONE}
  Input Text                      office_siret                  ${OFFICE_SIRET}
  Input Text                      amount                        ${OFFICE_AMOUNT}
  Input Text                      currency                      ${OFFICE_CURRENCY}
  Input Text                      invoice_office_header         ${INVOICE_OFFICE_HEADER}
  Input Text                      invoice_content               ${INVOICE_CONTENT}
  Input Text                      invoice_footer                ${INVOICE_FOOTER}
  Click Button                    jquery:button.btn.btn-primary
  Wait Until Element Is Enabled   jquery:div.growl-item
  Element Should Be Visible       jquery:div.growl-item.alert.alert-success

Check Rest Settings
  Fail 

Logout
  Go To   ${LOGIN_URL}/logout
  Title Should Be     Signin on Libreosteo