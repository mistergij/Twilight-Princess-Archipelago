import os

from dotenv import load_dotenv


class Global:
    def __init__(self):
        self.outputPath = None
        self.rootPath = None
        self.seedHashSecret = None
        self.imageVersion = None
        self.gitCommit = None
        
    def Global(self):
        envFileDir = self.__InitEnv()
        
        isProduction = os.getenv('TPRGEN_ENV') == "production"
        
        self.rootPath = self.__ResolvePath(
            envFileDir,
            os.getenv("TPRGEN_GENERATOR_ROOT")
        )
        self.outputPath = self.__ResolvePath(
            self.rootPath,
            os.getenv("TPRGEN_VOLUME_ROOT")
        )
        
        if isProduction:
            text = open("/run/secrets/seedhash_secret",mode='r',encoding='utf-8').read().strip()
            self.seedHashSecret = bytearray(text, 'utf-8')
        else:
            self.seedHashSecret = bytearray("seedHashSecret", 'utf-8')
            
        self.imageVersion = os.getenv("IMAGE_VERSION")
        if isProduction and (len(self.imageVersion) == 0 or self.imageVersion == None):
            raise Exception("Did not find IMAGE_VERSION in environment variables.")
        
        gitCommit = os.getenv("GIT_COMMIT")
        if isProduction and os.getenv("GIT_COMMIT") == None:
            raise Exception("Did not find GIT_COMMIT in environment variables.")
        
        os.mkdir(self.outputPath)
    
    def Init(self):
        pass
    
    def CombineOutputPath(self, paths):
        return os.path.join(self.outputPath, *paths)
    
    def CombineRootPath(self, paths):
        return os.path.join(self.rootPath, *paths)
        
    def __InitEnv(self):
        path = __path__
        
        desiredFilename = '.env.development'
        if os.getenv('TPRGEN_ENV') == "production":
            desiredFilename = '/env_config'
        
        while True:
            path = os.getcwd()
            if path == None:
                raise Exception("Unable to find environment config.")
            
            outputConfigPath = os.path.join(path, desiredFilename)
            if os.path.exists(outputConfigPath):
                load_dotenv(outputConfigPath)
                return path
            
    def __ResolvePath(self, path1, path2):
        path2 = os.path.abspath(path2)
        return os.path.join(path1, path2)