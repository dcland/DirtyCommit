import sys
import json
import git
import argparse
import logging 
from gitwrapper import GitWrapper
from config import FORMAT, KERNEL_CVE_FOLDER_LOCATION, KERNEL_CVE_FULL_LIST

logging.basicConfig(level=logging.DEBUG, format=FORMAT)

def list_from_file(file_path):
	print(file_path)
	f = open(file_path, 'r')
	res = f.read()
	f.close()
	return res.split('\n').sort()


def load_cve_json(file_path):
	f = open(file_path, 'r')
	y = json.load(f)
	return y


def list_compere(a, b):
	"""
    this function returns uniqe argument only
	:param a: list
	:param b: list
	:return: list
	"""
	return [i for i, j in zip(a, b) if i == j]


def update_db():
	logging.info("Updating DB")
	repo = git.Repo(KERNEL_CVE_FOLDER_LOCATION)
	o = repo.remotes.origin
	o.pull()
	logging.info("CVE_DB updated")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Dirty Commit help msg')
	parser.add_argument('-f',type=str, dest='folder',
						help='source code folder')
	parser.add_argument('--update',dest='update',
						action='store_true',
						help='if update needed')

	args = parser.parse_args()

	logging.info("Welcome to Dirty commit")

	if args.update:
		update_db()

	if not args.folder:
		parser.print_help(sys.stderr)
		exit(1)

	counter = 0
	git = GitWrapper(args.folder)
	commits = git.get_full_commits_list()

	cve_json = load_cve_json(KERNEL_CVE_FULL_LIST)
	for cve in cve_json:
		try :
			if git.is_commit_existing(cve_json.get(cve)['breaks']) and not git.is_commit_existing(cve_json.get(cve)['fixes']):
				logging.info("Found CVE {}".format(cve))
				counter += 1
		except:
			logging.warning("no tag for {}".format(cve))

	logging.info("Founded {} vulnerabilites".format(counter))


