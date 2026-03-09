package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Data struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	var input Data

	err := json.NewDecoder(os.Stdin).Decode(&input)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}

	message := fmt.Sprintf("Привет, %s! Тебе %d лет. Через 10 лет тебе будет %d.", input.Name, input.Age, input.Age+10)

	result := map[string]string{"message": message}

	json.NewEncoder(os.Stdout).Encode(result)
}
