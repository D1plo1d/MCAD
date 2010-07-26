import py, re

mod_re = (r"\bmodule\s+(", r")\s*\(\s*")
func_re = (r"\bfunction\s+(", r")\s*\(")

def extract_mod_names(fpath, name_re=r"\w+"):
    regex = name_re.join(mod_re)
    print regex
    matcher = re.compile(regex)
    return (m.group(1) for m in matcher.finditer(fpath.read()))

def extract_func_names(fpath, name_re=r"\w+"):
    regex = name_re.join(func_re)
    print regex
    matcher = re.compile(regex)
    return (m.group(1) for m in matcher.finditer(fpath.read()))

def collect_test_modules():
    dirpath = py.path.local("./")
    print "Collecting openscad test module names"
    
    test_files = {}
    for fpath in dirpath.visit('*.scad'):
        #print fpath
        modules = extract_mod_names(fpath, r"test\w*")
        #functions = extract_func_names(fpath, r"test\w*")
        test_files[fpath] = modules
    return test_files

collect_test_modules()
