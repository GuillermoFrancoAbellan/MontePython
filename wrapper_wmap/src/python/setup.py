from distutils.core import setup
from Cython.Build import cythonize
import numpy
from setuptools.extension import Extension

extensions=[ Extension(
"pywlik",
["pywlik.pyx"],
include_dirs=[numpy.get_include(),"/home/ns302248/montepython_p18sys/montepython/wrapper_wmap/lib"],
libraries=['wlik']
)
]

setup(name='pywlik',
      ext_modules=cythonize(extensions),
      )

'''
setup(name='pywlik',
      ext_modules=cythonize("pywlik.pyx"),
      include_dirs=[numpy.get_include()],
      libraries=['wlik'])
'''
