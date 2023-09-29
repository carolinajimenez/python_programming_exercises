"""
es: Programa que lee n-números reales del teclado y encuentre el promedio, el máximo y el mínimo de esos valores.
en: Algorithm that reads n-real numbers from the keyboard and finds the average, maximum and minimum of those values.
"""

__author__ = "Carolina Jiménez Moreno"
__email__ = "CJimenezm0794@gmail.com"

class NumberAnalysis:
  def __init__(self, numbers):
    self.numbers = numbers
  
  def calMean(self):
    total_nums = len(self.numbers)
    sum_nums = sum(self.numbers)
    mean = sum_nums / total_nums
    return mean
  
  def getMax(self):
    max_value = max(self.numbers)
    return max_value
  
  def getMin(self):
    min_value = min(self.numbers)
    return min_value


if __name__ == "__main__":
  print("---- Analysis of real n-numbers ----")
  correct = False
  limit = 0
  while(not correct):
    try:
      limit = int(input("Enter the number of numbers to analyze: "))
      correct = True
    except ValueError:
      print('Error. You must enter a number.')
  
  numbers = []
  for i in range(limit):
    correct = False
    num = 0
    while(not correct):
      try:
        num = int(input(f"Enter the number #{i+1}: "))
        correct = True
      except ValueError:
        print('Error, enter a real number.')
      numbers.append(num)
  
  number_analysis = NumberAnalysis(numbers)

  run = True
  while run:
    print ("""
    ---- MENU ----
    1. Calculate the average of the values entered.
    2. Calculate the maximum of the values entered.
    3. Calculate the minimum of the values entered.
    4. Exit menu.
    """)

    option = input("Enter the number corresponding to the calculation you wish to perform: ")
    if option == "1":
      mean = number_analysis.calMean()
      print(f"\n==> The average between the numbers {numbers} is {mean}\n")
    elif option == "2":
      maximun = number_analysis.getMax()
      print(f"\n==> The maximum number between the numbers {numbers} is {maximun}\n")
    elif option=="3":
      minimun = number_analysis.getMin()
      print(f"\n==> The minimum number between the numbers {numbers} is {minimun}\n")
    elif option=="4":
      print("\n---- Thank you very much ----")
      run = False 
    elif option != "":
      print("\n* * * This is not a valid option. Please try again. * * *\n")
