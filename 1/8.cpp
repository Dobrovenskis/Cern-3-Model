#include <fstream>
#include <iostream>
#include <array>

unsigned __int64 fibonachi_next(unsigned __int64 f1, unsigned __int64 f2)
{
    return (f1 + f2);
}

int main()
{
    int const amount = 200;

    unsigned __int64 f1 = 0;
    unsigned __int64 f2 = 1;
    unsigned __int64 f3;
    std::array<unsigned __int64, amount> arr;
    arr[0] = f1;
    arr[1] = f2;
    for(int i = 0; i < amount; i++)
    {
        f3 = fibonachi_next(f1, f2);
        arr[i+2] = f3;
        f1 = f2;
        f2 = f3;
    }
    for(unsigned __int64 fib : arr)
    {
        std::cout << fib << std::endl;
    }
}

