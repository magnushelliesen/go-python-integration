package main

import (
	"C"
	"fmt"
)

//export print_a_number
func print_a_number(num int) {
	fmt.Print("The number is ", num)
}

func main() {

}
