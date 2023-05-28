from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
if __name__ == '__main__':
    dt_now = datetime.datetime.now()
    print(dt_now.strftime('%d/%m/%Y'))
    print('start main')
    calculate_salary()
    get_employees()
