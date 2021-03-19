# Mojicc

An emoji AOT compilier set for C/C++, which helps you to code C/C++ with emojis, inspired by paper ["Enhancing the C++ Basic Character"](https://isocpp.org/files/papers/PO3OOrO.pdf), not the implementation but just play for fun.

Simply write source files extension with `.mpp` that can be compiled with **moji++ compiler**:

```cpp
#include <iostream>
📥 📛 std;
🔢 main(🔢 argc, 🔥 ** argv) { 
   cout << "Hello Emoji World!";
   💩 0;
}
```

Then compile the source code and execute the binary. It’s okey to compile `.mpp` with `.cpp` source files, the compiler will handle sources files and command arguments automatically.

```shell
moji++ -g main.mpp -o main
./main
> Hello Emoji World!
```

## Get started

Install mojicc dependencies:
 - `python3` for running mojicc AOT compiler
 - `gcc` or alternative compiler for compiler translated cpp source files

Download mojicc AOT compiler source code and set up environment variables:

```shell
git clone https://github.com/Unbinilium/Mojicc.git mojicc
export moji++="python3 $(pwd)/mojicc/src/moji++/moji++.py"
```

Check your mojicc installation by `moji++ -v`. 

The moji++ AOT compiler actually call the cpp compiler after mpp source files translated to cpp source files, so that you could use the arguments as same as the cpp compilers, the only difference is that mojicc AOT compiler filter the source file names with `.mpp` extension and do the translation.

## License

[MIT License](https://github.com/Unbinilium/Mojicc/blob/main/LICENSE) Copyright (c) 2021 Unbinilium.





