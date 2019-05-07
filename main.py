class MyOpen:
    def __init__(self, file_path,mode):
        self.filepath = file_path
        self.mode = mode
    
    def rd (self):
        return open(self,filepath.mode).read()
    
    def write(self, cnt):
        self.file = open(self,filepath).write(cnt)
    
    def __exit__(self,args, **kwargs):
        self.file.close()
        
    def __enter__(self):
        self.file = open(self.file)

        #Ucbucag

  def __init__(self, a, b, c):
        self._guard(a, b, c)
        self._lengths = (a, b, c)

    @staticmethod
    def __guard__(a_b, b_c, c_a):
        small, middle, large = [side for side in sorted([a_b, b_c, c_a])]
        if small + middle < large:
            raise TypeError('Ucbucagin berabersizliyini pozur')
        if small <= 0: 
            raise TypeError("Ucbucagın hec bir və ya menfi olculuyu yoxdu")

    def knd(self):
        a_b, b_c, c_a = self._lengths
        if a_b == b_c == c_a:
            knd = 'beraberdir'
        elif a_b == b_c or b_c == c_a or c_a == a_b:
            knd = 'qeyri beraber'
        return kind