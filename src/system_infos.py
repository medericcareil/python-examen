import platform
from cpuinfo import get_cpu_info
import numpy as np
import wmi
import psutil

class SystemInfos:
    def __init__(self) -> None:
        self._os = platform.system()
        self._release = platform.release()
        self._name = platform.node()
        self._processor = get_cpu_info()['brand_raw']
        self._ram = int(np.round(psutil.virtual_memory().total / (1024. **3)))
        self._gpu = wmi.WMI().Win32_VideoController()[0].name

    # === OS release === #
    def get_os(self) -> str:
        return self._os
    
    def set_os(self, new_os : str) -> str:
        self._os = new_os

    # === OS release === #
    def get_release(self) -> str:
        return self._release
    
    def set_release(self, new_release : str) -> str:
        self._release = new_release

    # === Computer name === #
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, new_name : str) -> str:
        self._name = new_name

    # === Processor === #
    def get_processor(self) -> str:
        return self._processor
    
    def set_processor(self, new_processor : str) -> str:
        self._processor = new_processor

    # === RAM === #
    def get_ram(self) -> float:
        return self._ram
    
    def set_ram(self, new_ram : float) -> float:
        self._ram = new_ram

    # === GPU === #
    def get_gpu(self) -> str:
        return self._gpu
    
    def set_gpu(self, new_gpu : str) -> str:
        self._gpu = new_gpu
        