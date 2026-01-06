package main

import (
	"fmt"
	"time"
	"runtime"
	"os"
)

func main() {
	hostname, _ := os.Hostname()
	osname := runtime.GOOS

	fmt.Printf("Hostname: %s\n", hostname[:len(hostname)-6])
	fmt.Printf("OS: %s\n", osname)
	fmt.Printf("Uptime: %s\n", time.Now())
}
