
from os.path import join

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('scanner',parent_package,top_path)
    #config.add_extension('regress_ext', join('src','regress_ext.c'))
    return config
