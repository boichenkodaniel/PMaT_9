package main

import (
	"encoding/json"
	"math"
	"os"
)

func main() {
	var input struct { N int `json:"n"` }
	json.NewDecoder(os.Stdin).Decode(&input)

	res := 0.0
	for i := 0; i < input.N; i++ {
		res += math.Sqrt(math.Exp(math.Sin(float64(i))))
	}

	json.NewEncoder(os.Stdout).Encode(map[string]float64{"result": res})
}