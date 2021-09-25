#include <iostream>
#include <fstream>
#include <sstream>

int main(int argc, char**argv )
{
    std::stringstream str;//(argv[1]);
    str << argv[1];
    int n;
    str >> n;

    std::ofstream p;
    p.open("C:\\Users\\1\\C++\\Model\\f1.txt");
    for(int i = 1; i <= n; i++)
    {
        std::cout << i << " ";
        p << i << " ";
    }
    p.close();
}
