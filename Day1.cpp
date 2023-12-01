#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    string input;
    // Read input from file
    ifstream file("Day1.txt");

    if (file.is_open()) {
        
        int total = 0;
        string temp = "";

        while (getline(file, input)) {
            
            string firstDigit = "";
            string lastDigit = "";

            for(int i = 0; i < input.length(); i++) {

                if(isdigit(input[i])) {
                    if(firstDigit.empty()) {
                        cout << firstDigit;
                        firstDigit = input[i];
                    }
                    lastDigit = input[i];
                }
                
            }
            cout << "First digit is " << firstDigit << " and last digit is " << lastDigit << "\n";
            total += stoi(firstDigit+lastDigit);

        }

    file.close();
    std::cout << total;

    }
    return 0;

}

//60632