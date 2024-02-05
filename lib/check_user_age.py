from dateutil.relativedelta import relativedelta
from datetime import date, datetime

def check_user_age(date_of_birth):
    # Parameters:
        # A string containing date of birth in the format `YYYY-MM-DD`
    # Returns:
    #     String saying either access granted or access denied

    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d")

        year = date.year
    except ValueError:
        raise Exception("Date is not in the right format")

    today = date.today()
    age = relativedelta(today, date_of_birth)
    age = datetime.today() - dob
    print(dob)
    return age.years

check_user_age("1980-05-06")


