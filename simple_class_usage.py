
# instance = class(...)
colors = list()   #  list colors = new list();

colors.append("blue")
colors.append("purple")
print(f"{colors = }")

x = 5    #   int x = new int(5);
m = "monkey"  

class Animal:
    def run(self, speed):  #  self == this
        print(f"running...{speed}")

a = Animal()
a.run("fast")  # Animal.run(a, "fast")
aa = Animal()
aa.run("slow") # Animal.run(aa, "slow")

class Dog(Animal):
    pass

d1 = Dog()
d1.run("full tilt boogie")
Dog.run(d1, "very slowly")

