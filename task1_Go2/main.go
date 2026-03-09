package main

import (
	"encoding/json"
	"os"
	"time"
)

type Input struct {
	Numbers []int `json:"numbers"`
}

type Output struct {
	Sum int `json:"sum"`
}

func main() {
	var input Input
	if err := json.NewDecoder(os.Stdin).Decode(&input); err != nil {
		return
	}

	resultChan := make(chan int)

	for _, n := range input.Numbers {
		go func(val int) {
			time.Sleep(100 * time.Millisecond)
			resultChan <- val * val
		}(n)
	}

	totalSum := 0
	for i := 0; i < len(input.Numbers); i++ {
		totalSum += <-resultChan
	}

	json.NewEncoder(os.Stdout).Encode(Output{Sum: totalSum})
}
