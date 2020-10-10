package main
 
import "fmt"
 
func main() {
 
    _array :=[]int{6,1,0,18,3,129,53,21,55,100}
    fmt.Println("\nUnsorted\n\n", _array)
    _sorted:=selectionsort(_array)
    fmt.Println("\nSorted\n\n", _sorted, "\n")
} 
func selectionsort(items []int) []int {
    var n = len(items)
    for i := 0; i < n; i++ {
        var minIdx = i
        for j := i; j < n; j++ {
            if items[j] < items[minIdx] {
                minIdx = j
            }
        }
        items[i], items[minIdx] = items[minIdx], items[i]
    }

    return items
}