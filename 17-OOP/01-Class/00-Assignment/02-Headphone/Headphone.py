'''
Headphone

attributes
brand              : str
model              : str
connectivityType   : str 
includedComponents : list[str]
uses               : list[str]
chargingTime       : str
compatibleDevices  : dir[str]
weight             : str
batteryLife        : str

'''

class Headphone :
    def __init__(self,
                brand : str,
                model : str,
                connectivityType : str,
                includedComponents : list[str],
                uses : list[str],
                chargingTime : str,
                compatibleDevices : list[str],
                weight : str,
                batteryLife : str) :
        self.brand = brand
        self.model = model
        self.connectivityType = connectivityType
        self.includedComponents = includedComponents
        self.uses = uses
        self.chargingTime = chargingTime
        self.compatibleDevices = compatibleDevices
        self.weight = weight
        self.batteryLife = batteryLife
    
    def __str__(self) :
        return f'''brand              : {self.brand}
model              : {self.model}
connectivityType   : {self.connectivityType} 
includedComponents : {self.includedComponents}
uses               : {self.uses}
chargingTime       : {self.chargingTime}
compatibleDevices  : {self.compatibleDevices}
weight             : {self.weight}
batteryLife        : {self.batteryLife}'''
    
H = Headphone(
    "boAt",
    "Rockerz",
    "Bluetooth",
    ["Cable", "Earmuffs", "Neckband", "User Manual"],
    ["Entertainment", "Travel"],
    "50 Minutes",
    ["Smartphones", "Tablets", "Laptops", "Desktops", "Music Production Equipment", "Gaming Consoles"],
    "30g",
    "40 hrs"
)

print(H)