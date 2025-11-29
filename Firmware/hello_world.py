#include <stdio.h>
#include "pico/stdlib.h"

int main() {
    // Initialize all standard serial I/O (defaults to USB CDC if connected)
    stdio_init_all();

    while (true) {
        printf("Hello, World!\n");
        // Pause for 1 second (1000 milliseconds)
        sleep_ms(1000); 
    }
    return 0; // The loop is infinite, but a return 0 is good practice
}