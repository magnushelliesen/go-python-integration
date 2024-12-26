package main

import (
	"C"
	"fmt"
)

//export helloWorld
func helloWorld() {
	fmt.Print("Hello World")
}

func main() {

}
