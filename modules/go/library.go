package main

/*
#include <stdlib.h>
*/
import "C"
import (
	"math/big"
	"unsafe"
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

//export fibonacci_recursive
func fibonacci_recursive(num int) int {
	if num < 2 {
		return num
	}
	return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)
}

//export de_mean
func de_mean(array *C.double, length C.int) *C.double {
	// Convert input array to Go slice
	goSlice := (*[1 << 30]float64)(unsafe.Pointer(array))[:length:length]

	// Compute mean
	var sum float64
	for _, value := range goSlice {
		sum += value
	}
	mean := sum / float64(length)

	// Allocate memory for the output array
	outArray := C.malloc(C.size_t(length) * C.size_t(unsafe.Sizeof(C.double(0))))
	if outArray == nil {
		return nil // Return nil if allocation fails
	}

	resultArray := (*[1 << 30]C.double)(outArray)[:length:length]

	// Subtract mean and store results
	for i, value := range goSlice {
		resultArray[i] = C.double(value - mean)
	}

	return (*C.double)(outArray)
}

//export free_array
func free_array(arr *C.double) {
	C.free(unsafe.Pointer(arr))
}

func main() {
	// This main function is required for the Go program, but it can remain empty
}
