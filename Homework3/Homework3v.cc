#include <iostream>
#include <cmath>
#include <limits>
using namespace std;


float vec2d (float x, float y) {

	float magnitude = sqrt(pow(x, 2) + pow(y, 2));
//	cout << "magnitude" << " " << x << " " << y << " ";
	return magnitude;
}

int main() {


	
	float minimum_mag = numeric_limits<float>::max();
	float min_vx = 0.0;
	float min_vy = 0.0;
	
	float xi=0 ,yi=0 ;  
    while( cin >> xi >> yi ) {    
   // cout << xi << "," << yi << endl;  
    
    if (minimum_mag > vec2d(xi,yi)){
        
        minimum_mag = vec2d(xi,yi);
        min_vx = xi;
        min_vy = yi;
        
        cout << "Hey! that's our minimum magnitude " << minimum_mag <<" , for the points "<< xi << "," << yi << endl;
    
        }

    }
    
    return 0;

}
