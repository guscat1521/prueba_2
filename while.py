
import os


x, x_1= 0, 1
while x_1 <= 1597:
    print(x , x_1, end = " ")
    x += x_1
    x_1 +=  x      
print("...")


def simpleArraySum(ar):

    resul sum ar

    return resul
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()