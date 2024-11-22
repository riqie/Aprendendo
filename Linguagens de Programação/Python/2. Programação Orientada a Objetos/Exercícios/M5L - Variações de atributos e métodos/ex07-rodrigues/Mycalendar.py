import calendar
from datetime import datetime, date

class Calendar:
    holidays = [date(2024, 1, 1), date(2024, 12, 25)]
    
    def __init__(self, year):
        self.year = year
    
    @staticmethod
    def is_holiday(check_date):
        if isinstance(check_date, str):
            check_date = datetime.strptime(check_date, '%d-%m-%Y').date()
        return check_date in Calendar.holidays
    
    @staticmethod
    def days_between(date1, date2):
        """Calcula a quantidade de dias entre duas datas."""
        if isinstance(date1, str):
            date1 = datetime.strptime(date1, '%d-%m-%Y').date()
        if isinstance(date2, str):
            date2 = datetime.strptime(date2, '%d-%m-%Y').date()
        return abs((date2 - date1).days)
    
    def display_month(self, month):
        """Exibe o calendário do mês especificado."""
        print(calendar.month(self.year, month))