
class CorruptedCoordinateFileError(Exception):
    
    def _init_(self, message):
        super(CorruptedCoordinateFileError, self).__init__(message)
        
