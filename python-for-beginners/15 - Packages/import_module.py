# 모듈을 네임스페이스로 import
import helpers
helpers.display('Not a warning')

# 모든 항목들을 현재의 네임스페이스로 import
from helpers import *
display('Not a warning')

# 특정 항목들을 현재의 네임스페이스로 import
from helpers import display
display('Not a warning')