def EuclideanAlgorithim(a,b):
    original_a=a
    original_b=b
    # Keep track of the original numbers for the LCM
    res = [ ]
    if(a==b):
        res.append(a)
        res.append(a)
        return res
        # GCD and LCM of 2 equal numbers are therselves
    elif(b>a):
        temp = b
        b = a
        a = temp
        # Swap to make sure A is > B
    while(b!=0):
        p= a % b
        a=b
        b=p
        # Find the remainder of A/B , switch it and keep iterating until B is =0 and then add it to the array
    res.append(a)
    lcm_result = (original_a*original_b) // a # As an addition to our algorithm we improved it by finding the LCM also which is the original value of a and b multiplied and divided by the GCD
    res.append(lcm_result)
    return res


def main():
    while True:
     try:
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        result = EuclideanAlgorithim(a,b)
        print("The GCD is euqal to:",result[0])
        print("The LCM is euqal to:",result[1])
        break  # Exit the loop if the input is valid
     except ValueError:
        print("Error: Please enter a valid integer.")

main()
