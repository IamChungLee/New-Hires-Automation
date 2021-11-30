import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#using PANDAS we read the csv that contains all the needed information to input new hires into Empeon
data = pandas.read_csv("test-new-hire.csv")


#We use selenium here to obtain the Empeon site.

chrome_driver_path = "/Users/chunglee/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://empeon.com/signin/")

#open in full screen
driver.maximize_window()

# Store the ID of the original window
original_window = driver.current_window_handle

#login
sign_in = driver.find_element_by_xpath('//*[@id="post-2639"]/div[1]/div/div/div/div/section/div/div/div/div/div/section/div/div/div[1]/div/div/div[3]/div/div/a/span/span')
sign_in.click()


#Go to new tab that is opened from clicking client sign in
# Loop through until we find the new window's handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#enter sign in details
time.sleep(3)
sign_in_email = "email stored in os.env"
password = "password stored in os.env"
email_field = driver.find_element_by_xpath('//*[@id="Input_Email"]')
email_field.send_keys(sign_in_email)
password_field = driver.find_element_by_xpath('//*[@id="Input_Password"]')
password_field.send_keys(password)
sign_in_button = driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/button')
sign_in_button.click()

#company tabs
company = "hidden for git purposes"

time.sleep(20)
if company == "hidden for git purposes":
    x = driver.find_element_by_xpath('//*[@id="app_body"]/app-home/div[2]/div[2]/dx-list/div[1]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]')
    x.click()
else:
    y = driver.find_element_by_xpath('//*[@id="app_body"]/app-home/div[2]/div[2]/dx-list/div[1]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[1]')
    y.click()


time.sleep(3)
people_tab = driver.find_element_by_xpath('//*[@id="app_nav_bar"]/div[2]/div/a[3]')
people_tab.click()

#ADDING NEW EMPLOYEE "FOR LOOP" STARTS HERE

#ITTERATE OVER DATAFRAME FOR EACH EMPLOYEES INFORMATION
for i, row in data.iterrows():

#EMPLOYEE INFORMATION---------------------------------------#

    #Personal
    ssn = ''.join(row['ssn'].split("-"))
    first_name = row['first name']
    middle_name = row['middle name']
    last_name = row['last name']
    birth_date = row['birthdate']
    gender = row['gender']

    #address
    address = row['address']
    city = row['city']
    state = row['state']
    apt = row['apt']
    zipcode = row['zipcode']

    #contact - use for loop below to obtain just the digits of home phone
    home_phone_unedited = row['home phone']
    home_phone = ''
    for i in home_phone_unedited:
        if i != '(' and i != ')' and i != '-':
            home_phone += i
    email = row['email']

    #employment status
    hire_date = row['hire date']
    aca = row[' aca']

    #payinfo
    hours = 0
    rate = 0

    #cost center
    department = row['department']
    bill_to_name = row['bill to name']
    position = row['position']
    work_state = 'NY'

    #federal tax
    federal_Status = row['federal status']
    dependent_credits = row['dependent credits']

    #state_tax
    state_status = row['state status']
    exemptions = row['exemptions']


    #-----END INFORMATION START ADDING--------------------------#

    time.sleep(5)
    new_employee = driver.find_element_by_xpath('//*[@id="app_body"]/app-company-wrapper/app-people/app-employees/employee-list/div/employee-list-toolbar/div[1]/dx-button/div/span')
    new_employee.click()

    #PERSONAL ENTRIES--------------------------
    time.sleep(2)
    ssn_entry = driver.find_element_by_xpath('//*[@id="ssnTextBox"]/div[1]/div[1]/input')
    ssn_entry.send_keys(ssn)
    first_name_entry = driver.find_element_by_xpath('//*[@id="personal"]/div[2]/app-card-item/div/div/div[1]/div[2]/app-dynamic-field[1]/div/div[2]/dx-text-box/div/div[1]/input')
    first_name_entry.send_keys(first_name)
    middle_name_entry = driver.find_element_by_xpath('//*[@id="personal"]/div[2]/app-card-item/div/div/div[1]/div[2]/app-dynamic-field[2]/div/div[2]/dx-text-box/div/div[1]/input')
    middle_name_entry.send_keys(middle_name)
    last_name_entry = driver.find_element_by_xpath('//*[@id="personal"]/div[2]/app-card-item/div/div/div[1]/div[2]/app-dynamic-field[3]/div/div[2]/dx-text-box/div/div[1]/input')
    last_name_entry.send_keys(last_name)
    birth_date_entry = driver.find_element_by_xpath('//*[@id="personal"]/div[2]/app-card-item/div/div/div[1]/div[3]/app-dynamic-field[1]/div/div[2]/dx-date-box/div/div/div[1]/input')
    birth_date_entry.send_keys(birth_date)
    if gender == 'female':
        female_button = driver.find_element_by_xpath('//*[@id="personal"]/div[2]/app-card-item/div/div/div[1]/div[3]/app-dynamic-field[2]/div/div[2]/app-radio-group/div/label[2]')
        female_button.click()

    #ADDRESS--------------------------
    address_entry = driver.find_element_by_xpath('//*[@id="address"]/div[2]/app-card-item/div/div/div[1]/div[1]/app-dynamic-field[1]/div/div[2]/app-address-autocomplete/dx-text-box/div/div[1]/input')
    address_entry.send_keys(address)
    apt_entry = driver.find_element_by_xpath('//*[@id="address"]/div[2]/app-card-item/div/div/div[1]/div[1]/app-dynamic-field[2]/div/div[2]/dx-text-box/div/div[1]/input')
    apt_entry.send_keys(apt)
    city_entry = driver.find_element_by_xpath('//*[@id="address"]/div[2]/app-card-item/div/div/div[1]/div[2]/app-dynamic-field[1]/div/div[2]/dx-text-box/div/div[1]/input')
    city_entry.send_keys(city)
    #dropdown
    time.sleep(1)
    state_drop_down = driver.find_element_by_xpath('//*[@id="address"]/div[2]/app-card-item/div/div/div[1]/div[2]/app-dynamic-field[2]/div/div[2]/dx-select-box/div[1]/div/div[1]/input')
    state_drop_down.send_keys(state)
    state_drop_down.send_keys(Keys.TAB)
    zip_entry = driver.find_element_by_xpath('//*[@id="address"]/div[2]/app-card-item/div/div/div[1]/div[2]/app-dynamic-field[3]/div/div[2]/dx-text-box/div/div[1]/input')
    zip_entry.send_keys(zipcode)
    zip_entry.send_keys(Keys.TAB)

    #CONTACT--------------------------
    home_phone_entry = driver.find_element_by_xpath('//*[@id="contact"]/div[2]/app-card-item/div/div/div[1]/div[1]/app-dynamic-field[1]/div/div[2]/dx-text-box/div/div[1]/input')
    home_phone_entry.send_keys(int(home_phone))
    email_entry = driver.find_element_by_xpath('//*[@id="contact"]/div[2]/app-card-item/div/div/div[1]/div[1]/app-dynamic-field[3]/div/div[2]/dx-text-box/div/div[1]/input')
    email_entry.send_keys(email)

    #EMPLOYMENT--------------------------
    hire_date_entry = driver.find_element_by_xpath('//*[@id="employment-status"]/div[2]/app-card-item/div/div/div[1]/div[1]/app-dynamic-field[1]/div/div[2]/dx-date-box/div/div/div[1]/input')
    hire_date_entry.send_keys(hire_date)
    aca_entry = driver.find_element_by_xpath('//*[@id="employment-status"]/div[2]/app-card-item/div/div/div[1]/div[1]/app-dynamic-field[4]/div/div[2]/dx-select-box/div[1]/div/div[1]/input')
    aca_entry.send_keys(aca)
    aca_entry.send_keys(Keys.TAB)

    #PAY INFO--------------------------
    default_hours = driver.find_element_by_xpath('//*[@id="pay-info"]/div[2]/app-card-item[1]/div/div/div[1]/div[1]/app-dynamic-field[3]/div/div[2]/dx-number-box/div/div[1]/input')
    default_hours.send_keys(0)
    default_rate = driver.find_element_by_xpath('//*[@id="pay-info"]/div[2]/app-card-item[2]/div/div/div[1]/div/app-dynamic-field[1]/div/div[2]/dx-number-box/div/div[1]/input')
    default_rate.send_keys(0)

    #cost centers
    time.sleep(2)
    department_entry = driver.find_element_by_xpath('//*[@id="cost-centers"]/div[2]/app-card-item/div/div/div[1]/div/app-dynamic-field[1]/div/div[2]/dx-select-box/div[1]/div/div[1]/input')
    department_entry.send_keys(department)
    department_entry.send_keys(Keys.UP) #sending the UP will keep text from disappearing
    department_entry.send_keys(Keys.TAB)
    bill_to_name = driver.find_element_by_xpath('//*[@id="cost-centers"]/div[2]/app-card-item/div/div/div[1]/div/app-dynamic-field[2]/div/div[2]/dx-select-box/div/div/div[1]/input')
    bill_to_name.send_keys(bill_to_name)
    bill_to_name.send_keys(Keys.UP)
    bill_to_name.send_keys(Keys.TAB)
    position_entry = driver.find_element_by_xpath('//*[@id="cost-centers"]/div[2]/app-card-item/div/div/div[1]/div/app-dynamic-field[3]/div/div[2]/dx-select-box/div[1]/div/div[1]/input')
    position_entry.send_keys(position)
    position_entry.send_keys(Keys.UP)
    position_entry.send_keys(Keys.TAB)
    work_state_entry = driver.find_element_by_xpath('//*[@id="cost-centers"]/div[2]/app-card-item/div/div/div[1]/div/app-dynamic-field[4]/div/div[2]/dx-select-box/div[1]/div/div[1]/input')
    work_state_entry.send_keys(work_state)
    work_state_entry.send_keys(Keys.UP)
    work_state_entry.send_keys(Keys.TAB)


    #FEDERAL TAX--------------------------
    filing_status_entry = driver.find_element_by_xpath('//*[@id="taxes"]/div[2]/app-card-item[2]/div/div/div[1]/div[1]/app-dynamic-field[1]/div/div/div/div[2]/dx-select-box/div/div/div[1]/input')
    filing_status_entry.send_keys(federal_Status)
    filing_status_entry.send_keys(Keys.UP)
    dependent_credits_entry = driver.find_element_by_xpath('//*[@id="taxes"]/div[2]/app-card-item[2]/div/div/div[1]/div[1]/app-dynamic-field[2]/div/div[2]/dx-number-box/div/div[1]/input')
    dependent_credits_entry.send_keys(int(dependent_credits))

    #STATE TAX
    state_status_entry = driver.find_element_by_xpath('//*[@id="taxes"]/div[2]/app-card-item[3]/div/div/div[1]/div[2]/app-dynamic-field[1]/div/div[2]/dx-select-box/div[1]/div/div[1]/input')
    state_status_entry.send_keys(state_status)
    state_status_entry.send_keys(Keys.UP)
    state_status_entry.send_keys(Keys.TAB)
    exemption_entry = driver.find_element_by_xpath('//*[@id="taxes"]/div[2]/app-card-item[3]/div/div/div[1]/div[2]/app-dynamic-field[2]/div/div[2]/dx-number-box/div/div[1]/input')
    exemption_entry.send_keys(int(exemptions))

    #SAVE
    save_button = driver.find_element_by_xpath('//*[@id="app_body"]/app-company-wrapper/app-people/app-employees/app-new-hire/div/form/div[2]/div/app-split-button/dx-button[1]/div')
    save_button.click()
    #from here the loop starts over again for each new hire in the csv until all are entered

