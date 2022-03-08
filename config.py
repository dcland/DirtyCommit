import os 

KERNEL_CVE_FOLDER_LOCATION = 'linux_kernel_cves'
KERNEL_CVE_DATA_LOCATION = 'linux_kernel_cves/data'
KERNEL_CVE_FULL_LIST = 'linux_kernel_cves/data/kernel_cves.json'

SUPPORTED_VERSIONS = [name for name in os.listdir(KERNEL_CVE_DATA_LOCATION) if os.path.isdir(name)]

#Logging format
FORMAT = "[%(asctime)-10s][%(filename)s:%(lineno)s - %(funcName)s() ] %(message)s"