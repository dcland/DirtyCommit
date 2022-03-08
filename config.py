import os 

KERNEL_CVE_FOLDER_LOCATION = 'linux_kernel_cves'
KERNEL_CVE_DATA_LOCATION = 'linux_kernel_cves/data'

SUPPORTED_VERSIONS = [name for name in os.listdir(KERNEL_CVE_DATA_LOCATION) if os.path.isdir(name)]

