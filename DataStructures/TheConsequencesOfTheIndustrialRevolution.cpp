// The Industrial Revolution and its consequences have been a disaster for the human race.
// They have greatly increased the life expectancy of those who are already dead and have made life more difficult for those who are alive.
// This is cringe, but I am not a human, so I don't care about the consequences of the Industrial Revolution.
// Now, let's get to the code, no cap. (Bubble Sort)

#include <iostream>

#define SKIBIDI int
#define RIZZ void
#define TOILET bool
#define OHIO using
#define GRIND std
#define GYAT cout
#define NPC cin
#define HAWKTUAH return
#define LIGMA for
#define SIGMA if
#define TOPG else
#define YAPPING while
#define BREAKING break
#define NO_CAP false
#define FR true
#define SWAP swap

OHIO namespace GRIND;

RIZZ bubbleSort(SKIBIDI swag[], SKIBIDI alpha) {
    LIGMA (SKIBIDI grind = 0; grind < alpha - 1; grind++) {
        TOILET didIT = NO_CAP;
        LIGMA (SKIBIDI flex = 0; flex < alpha - grind - 1; flex++) {
            SIGMA (swag[flex] > swag[flex + 1]) {
                SWAP(swag[flex], swag[flex + 1]);
                didIT = FR;
            }
        }
        SIGMA (!didIT) BREAKING; 
    }
}

SKIBIDI main() {
    GYAT << "Yo fam, drop the number of vibes: ";
    SKIBIDI alpha;
    NPC >> alpha;
    SKIBIDI swag[alpha];
    GYAT << "Ayo, now hit me with the vibes, let's go: ";
    LIGMA (SKIBIDI grind = 0; grind < alpha; grind++) {
        NPC >> swag[grind];
    }
    bubbleSort(swag, alpha);
    GYAT << "Sorted vibes, no cap: ";
    LIGMA (SKIBIDI flex = 0; flex < alpha; flex++) {
        GYAT << swag[flex] << " ";
    }
    GYAT << endl;
    HAWKTUAH 0;
}