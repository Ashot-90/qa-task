import multiprocessing
from typing import List
# Below ones need to be here, as using reflection
from tests.test_member import TestMemberPage
from tests.test_catalog import TestCatalogPage


class Main(object):

    @staticmethod
    def run() -> None:
        cpu_count = multiprocessing.cpu_count()
        print("CPU Count is '{}'".format(cpu_count))
        classes = ('TestCatalogPage', 'TestMemberPage')
        pool = multiprocessing.Pool(processes=cpu_count)
        for class_ in classes:
            test_class_object = eval(class_ + '()')
            for test_function in Main.get_test_functions(class_name=class_):
                pool.apply_async(func=eval('.'.join([class_, test_function])),
                                 args=(test_class_object, ))
        pool.close()
        pool.join()

    @staticmethod
    def get_test_functions(class_name: str) -> List[str]:
        test_functions = []
        for name, instance_type in eval('.'.join([class_name, '__dict__', 'items()'])):
            if callable(instance_type) and str(name).startswith('test_'):
                test_functions.append(str(name))
        return test_functions


if __name__ == "__main__":
    main = Main()
    main.run()
