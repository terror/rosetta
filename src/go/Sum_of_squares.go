package main

import ("fmt"; "math")

func main() {
  var arr [10]float64

  for i := range arr {
    arr[i] = float64(i * 20)
  }

  fmt.Println(s(arr))
}

func s(arr [10]float64) float64 {
  if len(arr) == 0 {
    return 0
  }

  var ans float64
  for i := range arr {
    ans += math.Pow(arr[i], 2)
  }

  return ans
}
