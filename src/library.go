package main

import (
	"C"
	"fmt"
)

//export print_a_number
func print_a_number(num int) {
	fmt.Print("The number is ", num)
}

//export return_a_number
func return_a_number(num int) int {
	return num + 2
}

func main() {

}
