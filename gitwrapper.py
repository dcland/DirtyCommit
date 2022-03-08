import sys, os 
from Exception import GitWrapperException
from git import Repo

CODE_FILE_EXTENTIONS = ['.c', '.cpp', '.h', '.hpp', '.hxx', '.py', '.sh']

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)

        else:
            return binary_search(arr, low +1, mid, x)
    else:
        return GitWrapperException("iligal arguments passed, the low argument higher then high argument")

def get_file_extention(file_path):
    _, file_ext = os.path.splitext(file_path)
    return file_ext



class GitWrapper(object):
    def __init__(self, folder):
        if os.path.exists(folder) is False:
            raise GitWrapperException("Folder path are not valid")
        self.repo = Repo(folder)
        self.heads = self.repo.heads
        self.commit_list = []

    def get_affected_files(self, commit):
        return [f for f in self.repo.commit(commit).stats.files]

    def get_affected_code_files(self, commit):
        source_file_list = []
        for file in self.get_affected_files(commit):
            if get_file_extension(file).lower() in CODE_FILE_EXTENTIONS:
                source_file_list.append(file)
        return source_file_list

    def get_full_commits_list(self):
        if len(self.commit_list) == 0:
            for c in self.repo.iter_commits():
                self.commit_list.append(str(c))
            self.commit_list.sort()
        return self.commit_list

    def is_commit_existing(self, commit):
        lst = self.get_full_commits_list()
        index = binary_search(lst, 0, len(lst)-1, commit )
        if index is not None:
            return True
        return False

if __name__ == '__main__':
    raise GitWrapperException("This library cannot be run standalone")