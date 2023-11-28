#include <stdio.h>
#include <math.h>
#include <stdbool.h>

struct ComparisonResults {
    bool lgreater;
    bool equal;
    bool rgreater;
};

struct ComparisonResults compare(bool a, bool b) {
    struct ComparisonResults results = {false, false, false};
    if (!a && b) {
        results.rgreater = true;
    }
    else if (!(!a && b || a && !b)) {
        results.equal = true;
    }
    else if (a && !b) {
        results.lgreater = true;
    }
    return results;
}


void main()
{
    struct ComparisonResults results;
    results = compare(false, false);
    printf("%d\n", results.equal);
}
