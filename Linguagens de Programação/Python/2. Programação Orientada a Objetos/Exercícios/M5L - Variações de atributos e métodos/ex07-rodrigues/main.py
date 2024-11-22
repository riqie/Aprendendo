'''7. Crie uma classe chamada Calendar que represente um calendário anual. Essa classe 
deve ter métodos para exibir o calendário de um determinado mês, verificar se uma 
data é feriado e calcular a diferença de dias entre duas datas.'''

from Mycalendar import Calendar

def main():
    cal = Calendar(2024)
    cal.display_month(9)

    print(f"Christmas is holiday?: {cal.is_holiday('25-12-2024')}") 
    print(f"My birthday is holiday?: {cal.is_holiday('27-06-2025')}")
    print(f"New year is holiday?: {cal.is_holiday('1-1-2024')}")

    # Diferença entre duas datas
    print(f"Diference between dates: {cal.days_between('01-01-2024', '25-12-2024')} dias")
    
main()
