#include<iostream>
#include <cmath>
using namespace std;

int factorial(int n){
    if (n >= 20){
        cout << "ERROR !!! " << endl;
        cout << "Please enter a number below 20 :) " << " " << endl;
        cin >> n ;
        
    }
    if( n == 0){
        return 1;
    }
    else {
    return n*factorial(n-1);
    
   }
    
}
int main(){
   int n;
   cout << "positive integer: ";
   cin >> n;
   cout << factorial(n);
}

