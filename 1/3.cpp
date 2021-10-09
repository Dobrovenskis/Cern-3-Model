#include <iostream>
#include <fstream>

int main()
{
    std::ofstream p;
    p.open("C:\\Users\\1\\C++\\Model\\f1.txt");
    for(int i = 1; i <= 30; i++)
    {
        std::cout << i << " ";
        p << i << " ";
    }
    p.close();
}
