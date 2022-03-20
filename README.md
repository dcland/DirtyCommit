# DirtyCommit
## Free vulnerability scanner for Linux kernel source code

DirtyCommit is the first git-based vulnerability scanner for Linux kernel source code, as far as I know, there is no project similar to DirtyCommit. 
DirtyCommit uses git commits list of Linux-based kernel repo. every Linux-based project could enjoy DirtyCommit, by just running this simple script, you will be able to know which vulnerabilities exist in your project. 

## How it Works
DirtyCommit uses [Linux_kernel_cves](https://github.com/nluedtke/linux_kernel_cves) project which tracks Linux kernel vulnerability from several different data streams and collects them all into a single repo. 
DirtyCommit compares all vulnerable commits and fix commits to detect which commit doesn't have been fixed yet.

## Features
- Search for any Linux-based kernel repo (e.g. Ubuntu, Debian, Yocto, etc.)
- Lookup for known vulnerabilities
- Show vulnerabilities detailed 

## Tech

DirtyCommit uses a number of open-source projects to work properly:
- [Linux_kernel_cves](https://github.com/nluedtke/linux_kernel_cves)

And of course, DirtyCommit itself is an open-source repository on GitHub.

## Installation and Updateing

DirtyCommit is easy to install tool

### Install the dependencies.
 
```sh
git clone https://github.com/dcland/DirtyCommit.git
cd DirtyCommit
pip install -r requirements.txt
git clone --recursive --jobs 8 https://github.com/nluedtke/linux_kernel_cves.git
```

### Updateing 
Updating the CVE database, is done by running the update command 
```sh
python DirtyCommit.py --update
```

### How To Use
Just run the following command on a local git repo of linux kernel 
```sh
python DirtyCommit.py -f PATH_TO_FOLDER
```

## Development

Want to contribute? Let's go!

DirtyCommit welcomes everyone who wants to collaborate and add more features 

## License
MIT
