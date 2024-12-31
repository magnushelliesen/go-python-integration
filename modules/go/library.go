package main

import (
	"C"
	"math/big"
	"unsafe"
)

//export fibonacci_iterative_go
func fibonacci_iterative_go(num int) *C.char {
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

//export fibonacci_recursive_go
func fibonacci_recursive_go(num int) int {
	if num < 2 {
		return num
	} else {
		return fibonacci_recursive_go(num-1) + fibonacci_recursive_go(num-2)
	}
}

//export de_mean_go
func de_mean_go(array *C.double, length C.int) float64 {
	slice := (*[1 << 30]float64)(unsafe.Pointer(array))[:length:length]
	var mean float64 = 0
	for _, value := range slice {
		mean += value
	}
	return mean / float64(len(slice))
}

func main() {

}
