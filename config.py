import os 

CVE_FOLDER_LOCATION = 'linux_kernel_cves/data'

SUPPORTED_VERSIONS = [name for name in os.listdir(CVE_FOLDER_LOCATION) if os.path.isdir(name)]