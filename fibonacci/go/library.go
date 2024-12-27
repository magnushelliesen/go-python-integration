package main

import (
	"C"
	"math/big"
)

//export fibonacci_iterative
func fibonacci_iterative(num int) *C.char {
	var n0 = big.NewInt(0)
	var n1 = big.NewInt(1)
	var n2 = big.NewInt(0)

	for i := 0; i <= num; i++ {
		if i < 2 {
			n0.SetInt64(int64(i))
		} else {
			n0.Add(n1, n2)
			n2.Set(n1)
			n1.Set(n0)
		}
	}

	return C.CString(n0.String())
}

func main() {

}
