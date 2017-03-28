
#include <iostream>
#include <vector>
#inlcude <fstream>
#inlcude <string>
#include <algorithm>
#inlcude <memory>
#include <list>
#include <cstdlib>
#include "StudentRecord.h"
#include "StudentRecordPhysics.h"
#include "StudentRecordLiterature.h"
#include "StudentRecordHIstory.h"
using  namespace std;

bool input  (istream&);
bool lessthan (shared_ptr <StudentRecord> const *left , shared_ptr <StudentRecord> const *right){ return &left < &right; };
vector shared_ptr <StudentRecord> precords,hrecords,lrecords ; // defining 3 objects of type StudentRecord class

int main (int argc , char *argv[]){
  ifstream input (argv [1]);
  while (insert (input)){
    insert (input);
  }
  // initializing
  double pavg = 0.0;
  double havg = 0.0;
  double lavg = 0.0;
  double totalavg = 0.0;
  double finaltotalavg = 0.0;
  //calculating average
  for (int i = 0;i<(precords.size());i++){
    pavg =pavg+ precords.at(i)-> score();
    totalavg = totalavg + precords.at(i)-> score():
    pavg = pavg / precords.size();
  }
  for (int i = 0;i<(hrecords.size());i++){
    havg =havg+ hrecords.at(i)-> score();
    totalavg = totalavg + hrecords.at(i)-> score():
    havg = havg / hrecords.size();
  }
  for (int i = 0;i<(lrecords.size());i++){
    lavg =lavg+ lrecords.at(i)-> score();
    totalavg = totalavg + lrecords.at(i)-> score():
    lavg = lavg / lrecords.size();
  }
  
  finaltotalavg = totalavg / ((precords.size())+(hrecords.size())+(lrecords.size());

			     
sort( precords.begin(),precords.end(),lessthan);
sort( lrecords.begin(),lrecords.end(),lessthan);
sort( hrecords.begin(),hrecords.end(),lessthan);

cout << "Physics Score" << std::endl;
for(int i=0;i<(precords.size());i++){
precords.at(i)->print();
}
cout << "Total GPA for Physics is " << pavg << endl;

cout <<"History Scores" <<endl;
for(int i=0;i<(hrecords.size());i++){
precords.at(i)->print();
  }
cout << "Total GPA for History is " << havg << endl;
  
cout <<  "Literature Scores" <<endl;
  for(int i=0;i<(lrecords.size());i++){
 lrecords.at(i)->print();
  }
cout << "Total GPA for Literature is " << lavg << endl;
  
cout <<"The Total Average For All Classes Is: " << finaltotalavg << endl;	                      
  
 }
