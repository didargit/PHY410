#include<iostream>
using namespace std;

double x1,x2,y1,y2
double midpoint1,midpoint2,eqofline,slope,yintercept

  int mian (){

  cout << "x1= ";
  cin >> x1;
  
  cout << "x2= ";
  cin >> x2;

  cout << "y1= ";
  cin >> y1;
  
  cout << "y2= ";
  cin >> y2;

  midpoint1 = ((x1+x2)/2);
  midpoint2 = ((y1+y2)/2);
  slope = (y2-y1)/(x2-x1);
  yintercept = y1-(slope*x1);
  eqofline = (slope*x1)+yintercept;

  cout << "Midpoint: " << midpoint1 << "," << midpoint2 << endl;
  cout << "Slope: " << slope << endl;
  cout << "Y intercept: " << yintercept << endl;
  cout << "Equation of line: " << "Y= " << eqofline << endl;
} 
