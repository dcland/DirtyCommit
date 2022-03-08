
class GeneralException(Exception):
    pass 

class GitWrapperException(GeneralException):
    pass 

class DirtyCommitException(GeneralException):
    pass 