from openscad_utils import *

def pytest_generate_tests(metafunc):
    if "mod_name" in metafunc.funcargnames:
        for fpath, mod_names in collect_test_modules().items():
            for mod_name in mod_names:
                metafunc.addcall(funcargs=dict(mod_name=mod_name, mod_file=fpath))

temppath = py.test.ensuretemp('MCAD')

def test_func(mod_name, mod_file, capfd):
    fpath = temppath.join(mod_file.base_name)
    
    call_openscad(path=fpath)
