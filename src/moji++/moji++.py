import os
import sys
import codecs
import hashlib

MOJIPLUSPLUS_VERSION = 'v0.0.2'
CPP_COMPILER = 'g++'

keywords_map = {
    u'↔': 'alignas',
    u'↩': 'alignof',
    u'☢': 'asm',
    u'🚗': 'auto',
    u'💡': 'bool',
    u'💔': 'break',
    u'💼': 'case',
    u'🚨': 'catch',
    u'🔥': 'char',
    u'🔥16_t': 'char16_t',
    u'🔥32_t': 'char32_t',
    u'🏫': 'class',
    u'💎': 'const',
    u'🗿': 'constexpr',
    u'💣': 'const_cast',
    u'➰': 'continue',
    u'🔎': 'decltype',
    u'😃': 'default',
    u'♻': 'delete',
    u'👇': 'do',
    u'✌': 'double',
    u'🎆_🎣': 'dynamic_cast',
    u'❔': 'else',
    u'📇': 'enum',
    u'💋': 'explicit',
    u'🚀': 'export',
    u'🚪': 'extern',
    u'👎': 'false',
    u'⛵': 'float',
    u'🍀': 'for',
    u'🫂': 'friend',
    u'✈': 'goto',
    u'❓': 'if',
    u'⏳': 'inline',
    u'🔢': 'int',
    u'🐟': 'long',
    u'📻': 'mutable',
    u'📛': 'namespace',
    u'👶': 'new',
    u'🔇': 'noexcept',
    u'☠': 'nullptr',
    u'💿': 'operator',
    u'🏩': 'private',
    u'🏦': 'protected',
    u'⛪': 'public',
    u'☑': 'register',
    u'😈': 'reinterpret_cast',
    u'💩': 'return',
    u'🔬': 'short',
    u'⊖': 'signed',
    u'📏': 'sizeof',
    u'⚡️': 'static',
    u'⚡_💂': 'static_assert',
    u'⚡_🎣': 'static_cast',
    u'🏠': 'struct',
    u'🤔': 'switch',
    u'💪': 'template',
    u'👉': 'this',
    u'🎁': 'thread_local',
    u'🔈': 'throw',
    u'👍': 'true',
    u'🚓': 'try',
    u'📤': 'typedef',
    u'🔍': 'typeid',
    u'⌨️': 'typename',
    u'💍': 'union',
    u'➕': 'unsigned',
    u'📥': 'using',
    u'👻': 'using',
    u'😱': 'void',
    u'⛽️': 'volatile',
    u'w🔥_t': 'wchar_t',
    u'🔁': 'while'
}

def import_sources(path):
    try:
        with codecs.open(path, 'r', encoding='utf-8') as f:
            src = f.readlines()
            enc = str(src).encode(encoding='utf-8')
            hash = hashlib.sha1(enc).hexdigest()
            print("Moji++: Imported sources -> '" + path + "'")
            return src, enc, hash
    except OSError:
        print("Moji++: Failed to import sources -> '" + path + "'")
        exit(-1)
        
def translate_sources(src, path, hash):
    translate_src = list()
    for line in src:
        for key in keywords_map.keys():
            line = line.replace(key, keywords_map[key])
        translate_src.append(line)
    print("Moji++: Translate sources -> '" + path + " to " + hash + ".cpp'")
    return translate_src
    
def export_sources(translate_src, hash):
    file_name = hash + ".cpp"
    try:
        with codecs.open(file_name, 'w', encoding='utf-8') as f:
            for line in translate_src:
                f.write(line)
            print("Moji++: Exported sources -> '" + file_name + "'")
            return file_name
    except OSError:
        print("Moji++: Failed to export translated sources -> '" + file + "'")
        
def clean_up(file_names):
    for file_name in file_names:
        if os.path.exists(file_name):
            try:
                os.remove(file_name)
            except OSError:
                print("Moji++: Failed to clean up exported sources -> '" + file_name + "'")
    print("Moji++: Clean up exported sources -> " + str(file_names))

def process_files(file_pathes):
    try:
        processed_files = []
        print("Moji++: Processing mpp files -> " + str(file_pathes))
        for path in file_pathes:
            src, enc, hash = import_sources(path)
            translate_src = translate_sources(src, path, hash)
            file_name = export_sources(translate_src, hash)
            processed_files.append(file_name)
        print("Moji++: Processed mpp files -> " + str(file_pathes))
        return processed_files
    except OSError:
        print("Moji++: Failed to process mpp files -> " + str(file_pathes))

def compile_sources(handled_args, unhandled):
    try:
        print("Moji++: Compiling sources using " + CPP_COMPILER +" -> " + str(handled_args['-g']))
        processed_files = process_files(handled_args['-g'])
        pos = unhandled.index('-g') + 1
        unhandled[pos:pos] = processed_files
        command = CPP_COMPILER + ' ' + " ".join(unhandled)
        os.system(command)
        print("Moji++: Compilied sources using " + CPP_COMPILER +" -> " + str(handled_args['-g']))
        return processed_files
    except OSError as err:
        print("Moji++: Failed to compile sources -> " + str(handled_args['-g']) + '\n' + err)
        
def version():
    print("Moji++: An emoji AOT compilier for C++ alternative to g++, version -> " + MOJIPLUSPLUS_VERSION)
    command = CPP_COMPILER + ' -v'
    os.system(command)
        
def help():
    print("Moji++: An emoji AOT compilier for C++, the usage is alternative to g++ -> 'g++ --help'")
    command = CPP_COMPILER + ' --help'
    os.system(command)
        
def handle_arguments(args):
    app_next = False
    handled_args = {
        '-g': [],
        '-v': False,
        '--version': False,
        '--help': False
    }
    unhandled = []
    for arg in args:
        for key in handled_args.keys():
            if key == arg:
                if key != '-g':
                    handled_args[key] = True
                else:
                    app_next = True
        if app_next:
            arg_s = str(arg)
            if arg_s.split('.')[-1] == 'mpp':
                handled_args['-g'].append(arg_s)
            else:
                unhandled.append(arg_s)
        else:
            unhandled.append(arg_s)
    if handled_args['-v'] or handled_args['--version']:
        version()
        exit(0)
    elif handled_args['--help']:
        help()
        exit(0)
    else:
        return handled_args, unhandled
    
def main():
    args = sys.argv[1:]
    handled_args, unhandled = handle_arguments(args)
    processed_files = compile_sources(handled_args, unhandled)
    clean_up(processed_files)

if __name__ == '__main__':
    main()
    
