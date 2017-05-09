 #include <cmath>
 #include <istream>
 #include <iomanip>
 using namespace std;
 
 #include "nonlin.hpp"
 using namespace cpt;
 
 const double pi = 4* atan(1.0);
 
 double func(Matrix<double,1>& point) {
     double x = point[0]; 
     double y = point[1];
     return .25*(x*x*x*x+y*y*y*y)+.5*x*x*y*y-.5*(x*x-y*y);
     }
 
 void dfunc(Matrix<double,1>& point, Matrix<double,1>& dpoint) {
     double x = point[0];
     double y = point[1];
     dpoint[0] = x*x*x+x*y*y-x;
     dpoint[1] = y*y*y+x*x*y-y;
     return;
 }
 
 int main()
 {
     Matrix<double,1> point(2);
     cin >> point[0] >> point[1];
     double gtol = 0.0001;
     double f_min;
     int iterations;
     minimize_BFGS(point, gtol, iterations, f_min, func, dfunc);
     cout << " func(" << point[0] << ", " << point[1] << ") = " << f_min
          << " in " << iterations << " iterations" << endl;
 }
