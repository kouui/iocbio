
from os.path import join
def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('analysis',parent_package,top_path)
    config.add_extension('lineinterp', sources = [join('src','lineinterp.c')])
    config.add_extension('imageinterp', sources = [join('src','imageinterp.c')],
                         define_macros = [('PYTHON_EXTENSION', None)])

    config.add_extension('fperiod', sources = [
            join('src','fperiod.pyf'),
            join('src','fperiod.c')])

    config.add_extension('dp', sources = [
            join('src','dp.pyf'),
            join('src','iocbio_detrend.c'),
            join('src','iocbio_fperiod.c'),
            join('src','iocbio_ipwf.c'),
            ])

    config.add_extension('ipwf', sources = [
            join('src','ipwf.pyf'),
            join('src','iocbio_ipwf.c'),
            ])
    return config
