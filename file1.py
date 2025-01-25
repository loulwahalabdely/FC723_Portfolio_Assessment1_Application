def EuclideanAlgorithim():
    a=270
    b=192
    while(b!=0):
        p= a % b
        a=b
        b=p
    return a

def main():
    result = EuclideanAlgorithim()
    print(result)

main()