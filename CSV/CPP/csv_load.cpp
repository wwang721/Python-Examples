//
//  csv_load.cpp
//  CPP
//
//  Created by WW on 2020/01/23.
//  Copyright © 2020 Wang Wei. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>	// stringstream
#include <stdio.h>	// sscanf

using namespace std;

int main(int argc, char ** argv)
{

	string fileName("lambda.csv");
	
	vector< vector<string> > dataString; // data in 2-D String vector
	

	ifstream fin(fileName);
	if(!fin)
	{	
		cout << "Error: <" << fileName << "> is not existing!\n";
		/*
		ofstream fout(fileName);

		fout << S[i] << ",";	
		
		fout.close();
		*/
	}
	else
	{
		cout << "Loading <" << fileName << "> ...\n";
		
		string line;	// every line data in String
		
		while (getline(fin, line)) 
		{
			stringstream ss(line); 	// convert "string" to "stringstream" for getline() function
			
			string data;	// data in String
			
			vector<string> linedataString;	// every line data in String vector
			
			while (getline(ss, data, ','))	// delimiter=','
				linedataString.push_back(data);

			dataString.push_back(linedataString);
     	}
	}
	fin.close();

	int dimension[2];
	dimension[0] = dataString.size();
	dimension[1] = dataString[0].size();

	cout << "Data dimension: " << dimension[0] << "x" << dimension[1] << endl;

	//Data in 2-D vector S(m*n)
	vector< vector<double> > S(dimension[0], vector<double>(dimension[1]));

	for(int i = 0; i < dimension[0]; i++)
	{
		for(int j = 0; j < dimension[1]; j++)
		{			
			// c_str() covert "string" to "char *"
			// sscanf() convert "char *" to "%lf" ("double")			
			sscanf(dataString[i][j].c_str(), "%lf", &S[i][j]);	
			cout << S[i][j] << "\t";
		}
		cout << endl;
	}

	return 0;
	
}
