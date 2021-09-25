#include <vector>
#include <iomanip>
#include <iostream>

void print_scientific_notation(double number)
{
    std::cout << std::scientific << number;
}

int main()
{
    int size_vec = 1000;
    std::vector<double> vec(size_vec);

    for(int i = 0; i < size_vec; i ++)
    {
        vec[i] = 1.0/(i+1);
    }

    for(double el: vec )
    {
        print_scientific_notation(el);
        std::cout << std::endl;
    }
}

