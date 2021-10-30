#include <iostream>
#include <vector>
#include <ctime>
#include <fstream>

void print_nxm_mat_double(std::vector<std::vector<double>> Mat)
{
    for(std::vector<double> el : Mat)
    {
        for(double num : el)
        {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }
}


int main()
{


    //int my_size = 10000; //100000
    int R = 5;
    float dt = 0.0009;
    float k = 2;
    float t0 = 100;

    int my_size = int(t0/dt);

    std::ofstream file("C:/Users/1/C++/Model/2/2simple_task_c++/file.txt");
    //file.open("C:\\Users\\1\\C++\\Model\\2\\2simple_task_c++\\file.txt");
    file << "k= " << k << "\n";
    file << "dt= " << dt << "\n";
    file << "t0= " << t0 << "\n";

    float a = R;
    float b = 0.0;
    //float a_pred;
    //float b_pred;
    float xi;
    float vi;
    float xin_zv;
    float vin_zv;

    file <<"a= "<< a << " ";
    file <<"b= "<< b << "\n";

    //print_nxm_mat_double(Mat);
    int start_time = clock();
    for(int i = 0; i < my_size - 1; i++)
    {
        /*
        a_pred = a;
        b_pred = b;

        a = a_pred + b_pred * dt;
        b = b_pred - a_pred * k * dt;

        file <<"a= "<< a << " ";
        file <<"b= "<< b << "\n";
        */
        xi = a;
        vi = b;

        xin_zv = xi + dt * vi;
        vin_zv = vi + dt* (-k) * xi;

        a = xi + 1./2*dt*(vi + vin_zv);
        b = vi + 1./2*dt*(-k*xi - k*xin_zv);
        //std::cout << xin_zv;

        file <<"a= "<< a << " ";
        file <<"b= "<< b << "\n";

    }
    //print_nxm_mat_double(Mat);

    int end_time = clock();
    std::cout << (end_time - start_time)/((double)CLOCKS_PER_SEC);
    file.close();


}
