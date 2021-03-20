## Mojicc

An emoji AOT compilier set for C/C++, which helps you to code C/C++ with emojis, inspired by paper ["Enhancing the C++ Basic Character"](https://isocpp.org/files/papers/PO3OOrO.pdf), not the implementation but just play for fun.

Simply write source files extension with `.mpp` that can be compiled with **moji++ compiler**:

```cpp
#include <iostream>
📥 📛 std;
🔢 main(🔢 argc, 🔥 ** argv) { 
   cout << "Hello Emoji 🌍!";
   💩 0;
}
```

Then compile the source code and execute the binary. It’s okey to compile `.mpp` with `.cpp` source files, the compiler will handle sources files and command arguments automatically.

```shell
moji++ -g main.mpp -o main
./main
> Hello Emoji 🌍!
```

## Get started

Install mojicc dependencies:

 - `python3` for running mojicc AOT compiler
 - `gcc` or alternative compiler for compiler translated cpp source files

Download mojicc AOT compiler source code and set up environment variables:

```shell
git clone https://github.com/Unbinilium/Mojicc.git mojicc
alias 'moji++'="python3 $(pwd)/mojicc/src/moji++/moji++.py"
```

Check your mojicc installation by `moji++ -v`. 

The moji++ AOT compiler actually call the cpp compiler after mpp source files translated to cpp source files, so that you could use the arguments as same as the cpp compilers, the only difference is that mojicc AOT compiler filter the source file names with `.mpp` extension and do the translation.

It means this is not something like mojilang, that only C++. You can write code by replacing keywords in C++ to emoji follow the unicode conversions table below, furthermore, you should know that:

- moji++ AOT compiler only replaces the keywords, not the emoji in the "" or '' evenif it is in the unicode conversions table
- moji++ AOT compiler will do changes to your comments if it contains the same emoji in the unicode conversions table

## Unicode conversions table

|  Keyword   | Emoji |   Keyword    | Emoji |  Keyword  | Emoji |     Keyword      | Emoji | Keyword  | Emoji |
| :--------: | :---: | :----------: | :---: | :-------: | :---: | :--------------: | :---: | :------: | :---: |
|  alignas   |   ↔   |   continue   |   ➰   |  friend   |   🫂   |     register     |   ☑   |   true   |   👍   |
|  alignof   |   ↩   |   decltype   |   🔎   |   goto    |   ✈   | reinterpret_cast |   😈   |   try    |   🚓   |
|    asm     |   ☢   |   default    |   😃   |    if     |   ❓   |      return      |   💩   | typedef  |   📤   |
|    auto    |   🚗   |    delete    |   ♻   |  inline   |   ⏳   |      short       |   🔬   |  typeid  |   🔍   |
|    bool    |   💡   |      do      |   👇   |    int    |   🔢   |      signed      |   ➖   | typename |   ⌨   |
|   break    |   💔   |    double    |   ✌   |   long    |   🐟   |      sizeof      |   📏   |  union   |   💍   |
|    case    |   💼   | dynamic_cast |  🎆_🎣  |  mutable  |   📻   |      static      |   ⚡   | unsigned |   ➕   |
|   catch    |   🚨   |     else     |   ❔   | namespace |   📛   |  static_assert   |  ⚡_💂  |  using   |   📥   |
|    char    |   🔥   |     enum     |   📇   |    new    |   👶   |   static_cast    |  ⚡_🎣  | virtual  |   👻   |
|  char16_t  | 🔥16_t |   explicit   |   💋   | noexcept  |   🔇   |      struct      |   🏠   |   void   |   😱   |
|  char32_t  | 🔥32_t |    export    |   🚀   |  nullptr  |   ☠   |      switch      |   🤔   | volatile |   ⛽   |
|   class    |   🏫   |    extern    |   🚪   | operator  |   💿   |     template     |   💪   | wchat_t  | w🔥_t  |
|   const    |   💎   |    false     |   👎   |  private  |   🏩   |       this       |   👉   |  while   |   🔁   |
| constexpr  |   🗿   |    float     |   ⛵   | protected |   🏦   |   thread_local   |   🎁   |          |       |
| const_cast |   💣   |     for      |   🍀   |  public   |   ⛪   |      throw       |   🔈   |          |       |

## License

[MIT License](https://github.com/Unbinilium/Mojicc/blob/main/LICENSE) Copyright (c) 2021 Unbinilium.
