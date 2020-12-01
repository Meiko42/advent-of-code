//Advent of code - puzzle 3
//https://adventofcode.com/2019/day/2
//Correct answer from my input is 3706713

#include "fstream"
#include "iostream"

int main(void){
    int input [] = {1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0};
    int numinputs = sizeof(input) / 4;

    // We need to first patch the input
    input[1] = 12;
    input[2] = 2;

    int i = 0;

    while (i < numinputs && input[i] != 99){
        if(input[i] == 1){
            int inputval1 = input[i + 1];
            int inputval2 = input[i + 2];
            int result =  input[inputval1] + input[inputval2];
            int savespot = input[i+3];
            input[savespot] = result;

        }
        else if(input[i] == 2){
            int inputval1 = input[i + 1];
            int inputval2 = input[i + 2];
            int result =  input[inputval1] * input[inputval2];
            int savespot = input[i+3];
            input[savespot] = result;
        }
        i += 4;
    }
    std::cout << "Value of position 0 is " << input[0] << std::endl;
    return 0;
}