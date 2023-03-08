import threading

# Arreglo de ejemplo
myArray = [1, 2, 2, 5, 4, 6, 7, 8, 8, 8]

class LongestSequenceThread(threading.Thread):
    def _init_(self, threadID, name, array):
        threading.Thread._init_(self)
        self.threadID = threadID
        self.name = name
        self.array = array
        
    def run(self):
        longest = 1
        number = self.array[0]
        current = 1
        for i in range(1, len(self.array)):
            if self.array[i] == self.array[i-1]:
                current += 1
            else:
                if current > longest:
                    longest = current
                    number = self.array[i-1]
                current = 1
        if current > longest:
            longest = current
            number = self.array[-1]
        print("Longest: {} Number: {}".format(longest, number))

# Crear e iniciar el thread
thread = LongestSequenceThread(1, "LongestSequenceThread", myArray)
thread.start()