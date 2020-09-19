##Author: Sarthak Singh sxs6666@psu.edu

 

def digit_sum(n):
    if int(n/10) == 0:
      return n
    else:
      sum = (n % 10) + (digit_sum(n//10))

      return sum


def run():
  n = int(input("Enter an int: "))
  print(f"sum of digits of {n} is {digit_sum(n)}.")
  

if __name__ == "__main__":
  run()


