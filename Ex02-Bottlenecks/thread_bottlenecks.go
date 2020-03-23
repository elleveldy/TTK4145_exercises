package main

import (
    . "fmt"
    "runtime"
    "time"
)

var i = make(chan int, 1)

func thread1Goroutine() {
    sum := 0
    for j := 0; j < 1000000; j++ {
        sum += 1
	}

    i <- sum
}

func thread2Goroutine() {
    sum := 0
    for j := 1; j < 1000000; j++ {
		sum -= 1
	}
    
    i <- sum
}

func main() {
    runtime.GOMAXPROCS(runtime.NumCPU()) 
    
    //Println("Before joined threads:", <-i)

    go thread1Goroutine()
    go thread2Goroutine()
    
    time.Sleep(100*time.Millisecond)
   
    a, b := <-i, <-i
    Println("After joined threads:", a + b)
    //Println("After joined threads:", sum)

}