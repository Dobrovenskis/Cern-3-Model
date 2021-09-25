#include<iostream>
#include <array>
#include <iomanip>

void print_scientific_notation(double number)
{
    std::cout << std::scientific << number;
}

int main()
{
    const int size_arr = 1000;
    std::array<double, size_arr> arr;

    for(int i = 0; i < size_arr; i ++)
    {
        arr[i] = 1.0/(i+1);
    }

    for(double el: arr )
    {
        print_scientific_notation(el);
        std::cout << ", ";
    }
}
