class Transformer:
    def voltage_ratio(self):
        return 0
class StepUpTransformer(Transformer):
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary
    def voltage_ratio(self):
        return self.secondary / self.primary
class StepDownTransformer(Transformer):
    def __init__(self, primary, secondary):
        self.primary = primary
        self.secondary = secondary
    def voltage_ratio(self):
        return self.secondary / self.primary
vp = float(input("Enter Primary Voltage/Turns: "))
vs = float(input("Enter Secondary Voltage/Turns: "))
if vs > vp:
    t = StepUpTransformer(vp, vs)
    print("Transformer Type: Step-Up Transformer")
else:
    t = StepDownTransformer(vp, vs)
    print("Transformer Type: Step-Down Transformer")
print("Voltage Ratio:", round(t.voltage_ratio(), 2))
