#include <iostream>
#include <fstream>

int main()
{
    int n;
    std::cin >> n;
    std::ofstream p;
    p.open("C:\\Users\\1\\C++\\Model\\f1.txt");
    for(int i = 1; i <= n; i++)
    {
        std::cout << i << " ";
        p << i << " ";
    }
    p.close();
}

