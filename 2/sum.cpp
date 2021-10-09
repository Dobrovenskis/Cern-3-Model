#include <math.h>
#include <iostream>
#include <iomanip>

main()
{
    int infinity = 60;
    double sum = 0;
    std::cout << std::setprecision(100);
    double a = 1;
    for(int i = 0; (sum + a) != sum; i++)
    {
        sum += a;
        a = a/2;
        std::cout << sum << std::endl;
    }
    std::cout << std::endl << "Answer: " <<sum << std::endl << std::endl;


    float sum2 = 0;
//    int j;
    for(double i = 1; (sum2 + 1.0/i) != sum2; i++)
    {
        sum2 += 1.0/i;
//        j = i;
//        std::cout << sum2 << "\n";
    }
    std::cout << "Answer2: " << sum2<< "  Nomber: " << j;

}
