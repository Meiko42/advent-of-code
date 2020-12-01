//Advent of code - puzzle 1
#include "fstream"
#include "iostream"

int main(void){
    std::ifstream infile("atc-1-input.txt");
    int input;
    int calc;
    int result;

    result = 0;

    while (infile >> input){
        calc = input / 3 - 2;
        result += calc;
    }
    std::cout << result << std::endl;
    return 0;
}