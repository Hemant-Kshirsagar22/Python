'''
@Author : Hemant Ganesh Kshirsagar
@Goal : To create a Basic PC class that will have information about Personal Computer
@Date : 16 / 08 / 2025
'''

class PC :
    def __init__(self, init_memory_size : int, init_storage_size : int, init_CPU : str, init_GPU : str) :
        self.memory_size = init_memory_size
        self.storage_size = init_storage_size
        self.CPU = init_CPU
        self.GPU = init_GPU
    
    def __str__(self):
        return f'{self.memory_size}GB, {self.storage_size}GB, CPU : {self.CPU}, GPU : {self.GPU}'
    
    def show(self) :
        print(f'{self.memory_size}GB, {self.storage_size}GB, CPU : {self.CPU}, GPU : {self.GPU}')

pc = PC(16, 1024, 'AMD Ryzen 5600 X', 'Nvidia RTX 3060 Ti')
pc.show()
print(pc)