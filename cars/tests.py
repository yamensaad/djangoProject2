from django.test import TestCase

# Create your tests here.


def t(n1,n2):
    for i in range(n1,n2+1):
        if i % 2 ==0 and i%4 !=0:
            print(i, end= '')