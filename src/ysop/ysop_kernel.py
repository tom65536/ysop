"""MetaKernel implementation for YSOP."""
import sys

from metakernel import MetaKernel

from ._version import __version__
from .engine import YsopScriptEngine

class MetaKernelYsop(MetaKernel):
    """Jupyter Kernel for the YSOP language."""
    implementation = 'MetaKernelYsop'
    implementation_version = __version__
    language = 'ysop'
    language_version = '0.1'
    banner = 'YSOP - yet some other programming language'
    language_info = {
        'mimetype': 'text/plain',
        'name': 'ysop',
        'file_extension': '.ys',
        'help_links': MetaKernel.help_links,
    }
    kernel_json = {
        'argv': [
            sys.executable, '-m', 'ysop.ysop_kernel', '-f', '{connection_file}'],
        'display_name': 'MetaKernelYsop',
        'language': 'ysop',
        'name': 'ysop_kernel'
    }

    def __init__(self, *args, **kwargs) -> None:
        """Initialize an instance."""
        super().__init__(*args, **kwargs)
        self.engine = YsopScriptEngine()

    def get_usage(self):
        return 'This is the YSOP kernel.'

    def do_execute_direct(self, code):
        return self.engine.eval(code)

    def repr(self, data):
        return repr(data)


if __name__ == '__main__':
    MetaKernelYsop.run_as_main()
