#include<stdio.h>

int add_two_values(int a, int b)
{
    return a+b;
}

int add_two_values_return_ref(int a, int b, int *c)
{
   *c=a+b;
   printf("Result is %d from C\n", a+b);
}