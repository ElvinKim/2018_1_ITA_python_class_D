# import my_statistics
#
# print(my_statistics.add(10, 20))
# print(my_statistics.abc)
# print("in my_code: ", __name__)
# import my_statistics

import root_package.module
from root_package.sub_package1.module1 import *
root_package.module.print_module()
print_module1()

from root_package.sub_package1 import *
module1.print_module1()
module2.print_module2()
