package main

import (
    . "fmt"
    "runtime"
    "time"
)

var i int

func thread1Goroutine() {
    for j := 0; j < 1000000; j++ {
		i += 1
	}
}

func thread2Goroutine() {
    for j := 0; j < 1000000; j++ {
		i -= 1
	}
}

func main() {
    runtime.GOMAXPROCS(runtime.NumCPU()) 

    Println("Before joined threads:", i)

    go thread1Goroutine()
    go thread2Goroutine()
    
    time.Sleep(100*time.Millisecond)
    Println("After joined threads:", i)
}