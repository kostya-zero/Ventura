#include "arch.h"
#include <iostream>
namespace arch {
    // Instace of class
    arch::arch () {}

    // Checking if system 64-bit
    void arch::CheckArch() {
        auto size = sizeof(void *);
        if (size == 4) {
            std::cout << "VENTURA: Architecture of CPU doesnt match requirements." << std::endl;
            exit(0);
        }
    }
}