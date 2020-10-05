package main
 
import "fmt"
 
func main() {
 
    _array :=[]int{6,1,0,18,3,129,53,21,55,100}
    fmt.Println("\nUnsorted\n\n", _array)
    _sorted:=insertionsort(_array)
    fmt.Println("\nSorted\n\n", _sorted, "\n")
}
   
func insertionsort(items []int) []int{
    var n = len(items)
    for i := 1; i < n; i++ {
        j := i
        for j > 0 {
            if items[j-1] > items[j] {
                items[j-1], items[j] = items[j], items[j-1]
            }
            j = j - 1
        }
    }

    return items
}