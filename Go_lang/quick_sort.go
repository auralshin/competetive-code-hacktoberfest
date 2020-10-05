package main
 

import (
    "fmt"
    "math/rand  "
)
 
func main() {
 
    _array:=[]int{6,1,0,18,3,129,53,21,55,100}
    fmt.Println("\nUnsorted\n\n", _array)
    _sorted:=quicksort(_array)
    fmt.Println("\nSorted\n\n", _sorted, "\n")
}
  
func quicksort(a []int) []int {
    if len(a) < 2 {
        return a
    }
      
    left, right := 0, len(a)-1
      
    pivot := rand.Int() % len(a)
      
    a[pivot], a[right] = a[right], a[pivot]
      
    for i, _ := range a {
        if a[i] < a[right] {
            a[left], a[i] = a[i], a[left]
            left++
        }
    }
      
    a[left], a[right] = a[right], a[left]
      
    quicksort(a[:left])
    quicksort(a[left+1:])
      
    return a
}