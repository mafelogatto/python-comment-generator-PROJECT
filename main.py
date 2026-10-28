# Created by: Maria Fernanda Ribeiro

import re
from datetime import datetime
from dateutil.parser import parse

# Date validation using the dateutil library. The user is prompted to enter a date in the mm/yyyy format.

def validate_date(prompt):
    while True:
        date = input(prompt).strip()

        if re.fullmatch(r'\d{2}/\d{4}', date):
            try:
                parse(
                    date,
                    default=datetime(2000, 1, 1),
                    dayfirst=False
                )
                return date

            except (ValueError, OverflowError):
                pass

        print('Invalid date. Enter the date in mm/yyyy format.')

# Comment generation based on user input.

def generate_comment():
    first_record = validate_date('First record date (mm/yyyy): ')
    last_record = validate_date('Last record date (mm/yyyy): ')

    # Validate the number of records and equipment.

    while True:
        try:
            record_count = int(input('Number of records: '))

            if record_count < 0:
                print('Invalid number of records. Try again.')
            else:
                break

        except ValueError:
            print('Enter whole numbers only.')

    while True:
        try:
            equipment_count = int(input('Number of equipment units: '))

            if equipment_count < 0:
                print('Invalid number of equipment units. Try again.')
            else:
                break

        except ValueError:
            print('Enter whole numbers only.')

    case_classification = input(
        'Case classification (1 - New, 2 - Recurring, 3 - Reopen, 4 - Under Analysis, 5 - Analysis Completed): ').strip()

    while case_classification not in ['1', '2', '3', '4', '5']:
        print('Invalid classification. Try again.')
        case_classification = input(
            'Case classification (1 - New, 2 - Recurring, 3 - Reopen, 4 - Under Analysis, 5 - Analysis Completed): ').strip()

    case_name = input('Case name: ').strip()

    # Adjust singular and plural forms.

    if record_count == 1:
        irregularity_word = 'irregularity'
    else:
        irregularity_word = 'irregularities'

    if equipment_count == 1:
        equipment_word = 'equipment unit'
    else:
        equipment_word = 'equipment units'

    # Generate a comment based on the case classification.

    if case_classification == '1':
        print(f'Case: {case_name}')
        print(
            f'This is a new case with report attached. Between {first_record} and {last_record}, {record_count} {irregularity_word} were identified across {equipment_count} {equipment_word}. The case will remain under analysis until it is ready to proceed.')

    elif case_classification == '2':
        print(f'Case: {case_name}')
        print(
            f'This case was previously reviewed, and an agreement was reached. However, the company continues to show irregularities. Between {first_record} and {last_record}, {record_count} new {irregularity_word} were identified across {equipment_count} {equipment_word}. The case will remain under analysis until it is ready for notification.')

    elif case_classification == '3':
        print(f'Case: {case_name}')
        print(
            f'This case was previously reviewed, but no agreement was reached. Between {first_record} and {last_record}, {record_count} {irregularity_word} were identified across {equipment_count} {equipment_word}.')

    elif case_classification == '4':
        print(f'Case: {case_name}')
        print('The company has been identified, but only a limited number of irregularities have been found. The case has been flagged for notification if further irregularities are identified. The company will be notified when the appropriate time comes. The case will remain under analysis until then.')

    elif case_classification == '5':
        print(f'Case: {case_name}')
        print('Additional irregularities have been identified, and the case is expected to be notified soon. Although there have been no recent records and further irregularities do not seem likely, the notification will be sent soon to avoid missing the appropriate timing.')


# Structure to allow users to generate multiple comments.

continue_program = 's'

while continue_program in ['s', 'sim']:
    generate_comment()

    continue_program = input(
        'Generate another comment? (y/n): '
    ).strip().lower()

    while continue_program not in ['y', 'yes', 'n', 'no', 's', 'sim']:
        print('Invalid option. Enter y or n.')
        continue_program = input(
            'Generate another comment? (y/n): '
        ).strip().lower()

    if continue_program in ['y', 'yes']:
        continue_program = 's'
