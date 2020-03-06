curlasio_asynchronous_bin = executable(
    'asynchronous',
    ['asynchronous.cpp'],
    dependencies: deps,
    include_directories : inc,
    cpp_args: extra_cpp_args,
    link_with : curlasio_lib,
)

curlasio_synchronous_bin = executable(
    'synchronous',
    ['synchronous.cpp'],
    dependencies: deps,
    include_directories : inc,
    cpp_args: extra_cpp_args,
    link_with : curlasio_lib,
)
