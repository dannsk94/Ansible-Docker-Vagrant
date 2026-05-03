#include <fmt/core.h>
using namespace fmt;
//fmt::print не встроена в с++ и ее мы загрузим через conan.
int main() {
    print("Результат работы задания {}\n", 8);
    return 0;
}