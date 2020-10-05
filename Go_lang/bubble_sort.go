package main
 
import "fmt"
 
func main() {
 
    _array:=[]int{6,1,0,18,3,129,53,21,55,100} //Only as an example
    fmt.Println("\nUnsorted\n\n", _array)
    _sorted:=bubblesort(_array)
    fmt.Println("\nSorted\n\n", _sorted, "\n")
}
  
func bubblesort(items []int) []int{
    var (
        n = len(items)
        sorted = false
    )
    for !sorted {
        swapped := false
        for i := 0; i < n-1; i++ {
            if items[i] > items[i+1] {
                items[i+1], items[i] = items[i], items[i+1]
                swapped = true
            }
        }
        if !swapped {
            sorted = true
        }
        n = n - 1
    }

    return items
}