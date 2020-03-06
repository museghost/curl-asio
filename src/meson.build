lib_src = [
    'easy.cpp',
    'error_code.cpp',
    'form.cpp',
    'initialization.cpp',
    'multi.cpp',
    'share.cpp',
    'string_list.cpp',
]

curlasio_lib = library(
    'curlasio',
    lib_src,
    dependencies: deps,
    include_directories: inc,
    cpp_args : extra_cpp_args,
    install: true,
)
