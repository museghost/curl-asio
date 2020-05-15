project('curl-asio',
        ['c', 'cpp'],
        version: '0.1.0',
        meson_version : '>= 0.52',
        default_options : [
		    'cpp_std=c++17',
        ]
)

# variables tracking sources and libraries
inc = [include_directories('include')]

# compile options
# meson.get_compiler('c').get_id()
cc = meson.get_compiler('cpp')
if cc.get_id() == 'msvc'
    # pedantic compile flags
    extra_cpp_args = []
else
    extra_cpp_args = ['-Wshadow', '-pedantic', '-Wgnu-statement-expression', '-Wgnu-zero-variadic-macro-arguments']
    extra_cpp_args += ['-fvisibility-inlines-hidden']
endif

# dependencies
deps = [
    dependency('OpenSSL', required: true),
    dependency('boost', required: true),
    dependency('libcurl', required: true),
]

# library
subdir('src')

# examples
if get_option('with-example')
    subdir('examples')
endif

# performance
#if get_option('with-benchmark')
#    subdir('performance')
#endif

# tests
#if get_option('with-tests')
#    subdir('tests')
#endif

# TODO: how to handle pdb in msvc

# TODO: doxygen