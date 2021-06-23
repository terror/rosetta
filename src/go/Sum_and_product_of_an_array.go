package main

import "fmt"

type yeet func(int, int) int

func main() {
  var arr [10]int

  for i := range arr {
    arr[i] = i
  }

  // fmt.Println(sum(arr))
  // fmt.Println(prod(arr))

  fmt.Println(reduce(arr, func(x int, y int) int { return x + y }))
  fmt.Println(reduce(arr, func(x int, y int) int { return x * y }))
}

// func sum(arr [10]int) int {
//   var ans int
//   for i := range arr {
//     ans += arr[i]
//   }
//   return ans
// }

// func prod(arr [10]int) int {
//   var ans int
//   for i := range arr {
//     ans *= arr[i]
//   }
//   return ans
// }

func reduce(arr [10] int, fn yeet) int {
  ans := arr[0]
  for i := 1; i < len(arr); i++ {
    ans = fn(arr[i], ans)
  }
  return ans
}
