class Converter:
    def GcByte(x):
        """Returns x as a byte array
        
        Parameters:
        x (int): The number you want to convert
        
        Returns:
        The inserted value as a byte array"""
        return x
    
    def GcBytesBigEndian64(self, x):
        """Returns x as 64-bit BigEndian (GC).
        
        Parameters:
        x (int): The number you want to convert.
        
        Returns:
        The inserted value as a 64-bit Big Endian byte. 
        """
        return x.to_bytes(8, byteorder='big')
    
    def GcBytesBigEndian32(self, x):
        """Returns x as 32-bit BigEndian (GC).
        
        Parameters:
        x (int): The number you want to convert.
        
        Returns:
        The inserted value as a 32-bit Big Endian byte.
        """
        return x.to_bytes(4, byteorder='big')
    
    def GcBytesBigEndian16(self, x):
        """Returns x as 16-bit BigEndian (GC).
        
        Parameters:
        x (int): The number you want to convert.
        
        Returns:
        The inserted value as a 16-bit Big Endian byte.
        """
        return x.to_bytes(2, byteorder='big')
    
    def GcBytesBigEndian32Signed(self, x):
        """Returns x as 32-bit Signed BigEndian (GC).
        
        Parameters:
        x (int): The number you want to convert.
        
        Returns:
        The inserted value as a 32-bit Signed Big Endian byte.
        """
        return x.to_bytes(4, byteorder='big', signed=True)
    
    def GcBytesBigEndian16Signed(self, x):
        """Returns x as 16-bit Signed BigEndian (GC).
        
        Parameters:
        x (int): The number you want to convert.
        
        Returns:
        The inserted value as a 16-bit Signed Big Endian byte.
        """
        return x.to_bytes(2, byteorder='big', signed=True)
    
    def StringBytes(self, text, desiredLength=-1, region='E'):
        """Get bytes (without null terminator).
        
        Parameters:
        text: the ASCII text you want to convert.
        desiredLength: The length of the string in bytes. If not specified, returned array will match the length of the provided text.
        region: The language region of the text you want to convert. CURRENTLY UNUSED.
        
        Returns:
        Array of bytes processed.
        """
        textData = []
        if (desiredLength == 0 or text == None):
            return bytes(0)
        
        if (desiredLength < 0):
            desiredLength = len(text)
        
        if (len(text) > desiredLength):
            for i in range(desiredLength+1):
                textData.append(ord(text[i]))
        else:
            for i in text:
                textData.append(ord(i))
        
        while len(textData) < desiredLength:
            textData.append(0)
            
        return textData
    
    def MessageStringBytes(self, text, desiredLength=0, region="E"):
        textData = []
        for i in range(len(text)):
            textData.append(ord(text[i]))
        
        while len(textData) < desiredLength:
            textData.append(0)
        
        return textData
    
    def StringBytes(self, text):
        return ord(text)