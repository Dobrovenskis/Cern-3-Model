#include <iostream>
#include <fstream>

unsigned __int64 fibonachi_next(unsigned __int64 f1, unsigned __int64 f2)
{
    return (f1 + f2);
}

int main()
{
    int amount;
    std::cin >> amount;
    std::ofstream file;
    file.open("C:\\Users\\1\\C++\\Model\\1\\7.txt");
    unsigned __int64 f1 = 0;
    unsigned __int64 f2 = 1;
    unsigned __int64 f3;
    for(int i = 0; i < amount; i++)
    {
        f3 = fibonachi_next(f1, f2);
        file << i << "    ";
        file << f3 << std::endl;
        f1 = f2;
        f2 = f3;
    }
    file.close();
}
