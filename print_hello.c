#include<stdio.h>

//gcc -fPIC -shared -rdynamic print_hello.c -o print_hello.so

void hello()
{
	printf("Hello World from C\n");
}

void main()
{
	hello();
}

int add_two_values(int a, int b)
{
    return a+b;
}

int add_two_values_return_ref(int a, int b, int *c)
{
   *c=a+b;
   printf("Result is %d from C\n", a+b);
}