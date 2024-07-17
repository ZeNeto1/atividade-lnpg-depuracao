def calculate_average(numbers):
  total = sum(numbers)
  return total / len(numbers)

def find_max(numbers):
  max_number = numbers[0]
  for number in numbers:
      if number > max_number:
          max_number = number
  return max_number

def get_numbers():
  numbers = input("Enter numbers separated by spaces: ").split()
  try:
    numbers = [float(num) for num in numbers] 
    #o código não funcionava se o usuário inserir números decimais, então foi usado o float para converter os números em float.
    return numbers
    
  except ValueError:
    print("Entrada inválida. Por favor, insira apenas números separados por espaços.")
    #foi utilizado um tratamento de exceção para garantir que o programa identifique se o usuário inserir um valor inválido como Strings ou Caracteres'''


def main():
          
  numbers = get_numbers()
  print("Average:", calculate_average(numbers))
  print("Maximum:", find_max(numbers))

if __name__ == "__main__":
  main()
