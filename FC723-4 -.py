def EuclideanAlgorithimExtd(a,b):
    if(a==b):
        return a # GCD of 2 equal numbers is themselves 
    elif(b>a):
        temp = b
        b = a
        a = temp
        # Swap to make sure A is > B
    while(b!=0):
        p= a % b
        a=b
        b=p
    return a

def main():
   while True:
    try:
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        result = EuclideanAlgorithimExtd(a,b)
        print(result)
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Error: Please enter a valid integer.")
main()