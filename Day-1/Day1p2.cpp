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
        string numbers[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine"};

        while (getline(file, input)) {
            
            string firstDigit = "";
            string lastDigit = "";
            string word = "";
            
            
         
            for(int i = 0; i < input.length(); i++) {

                if(isdigit(input[i])) {
                    if(firstDigit.empty()) {
                        firstDigit = input[i];
                    }
                    lastDigit = input[i];
                    word = "";
                }

                else {
                    word += input[i];
                    for (int j = 0; j < size(numbers); j++) {
                        if(word.find(numbers[j]) != string::npos) {
                            if(firstDigit.empty()) {
                                firstDigit = to_string(j);
                            }
                            lastDigit = to_string(j);
                            word = word.substr(word.length()-2,word.length()-1);
                        }
                    } 
                }
                
            }
            cout << "First digit is " << firstDigit << " and last digit is " << lastDigit << "\n";
            total += stoi(firstDigit+lastDigit);
            cout << "Total is " << total << "\n";

        }

    file.close();
    cout << total;

    }
    return 0;

}