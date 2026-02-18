package main

import (
	"fmt"
	"os"

	"golang.org/x/term"
)

func main() {
	oldState, err := term.MakeRaw(int(os.Stdin.Fd()))
	if err != nil {
		panic(err)
	}
	defer term.Restore(int(os.Stdin.Fd()), oldState)

	fmt.Print("Press any key (Press 'q' or 'Ctrl+C' to quit)...\r\n")

	b := make([]byte, 1)
	for {
		_, err := os.Stdin.Read(b)
		if err != nil {
			break
		}

		char := b[0]
		switch char {
		case 'a':
			fmt.Println("AAAA")
		case 'b':
			fmt.Println("BBBB")
		default:
			fmt.Printf("%c\n", char)
		}

		if char == 'q' || char == 3 {
			fmt.Print("\r\nExiting...\r\n")
			break
		}

		fmt.Printf("Key pressed: %c  (ASCII: %d)\r\n", char, char)
	}
}
