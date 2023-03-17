
class Iptx:

    def __init__(self, ip):
        self.ip = str(ip)

  # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def ipdict(self): return self.ip.split(".")

  # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def ipwxyz(self):
        return {"w": self.ipdict()[0],
                "x": self.ipdict()[1],
                "y": self.ipdict()[2],
                "z": self.ipdict()[3]}

  # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def cti(self): return int(self.ipwxyz()["w"])

  # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def showIp(self):
        return f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.{self.ipwxyz()["y"]}.{self.ipwxyz()["z"]}'

  # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def binaryIp(self, ip):
        # bnGenerator -> Binary Number Generator
        return '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])

  # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def classIp(self):
        if (1 <= self.cti() <= 126):
            return list(["[ A ]", "255.0.0.0"])
        elif (128 <= self.cti() <= 191):
            return list(["[ B ]", "255.255.0.0"])
        elif (192 <= self.cti() <= 223):
            return list(["[ C ]", "255.255.255.0"])

  # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def subnetMaskIp(self):
        match self.classIp()[0]:
            case "[ A ]": return "255.0.0.0"
            case "[ B ]": return "255.255.0.0"
            case _: return "255.255.255.0"

  # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def hostIp(self):
        match self.classIp()[0]:
            case "[ A ]": return f'0.{self.ipwxyz()["x"]}.{self.ipwxyz()["y"]}.{self.ipwxyz()["z"]}'
            case "[ B ]": return f'0.0.{self.ipwxyz()["y"]}.{self.ipwxyz()["z"]}'
            case _: return f'0.0.0.{self.ipwxyz()["z"]}'

   # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def networkIp(self):
        match self.classIp()[0]:
            case "[ A ]": return f'{self.ipwxyz()["w"]}.0.0.0'
            case "[ B ]": return f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.0.0'
            case _: return f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.{self.ipwxyz()["y"]}.0'

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def broadcastIp(self):
        match self.classIp()[0]:
            case "[ A ]": return f'{self.ipwxyz()["w"]}.255.255.255'
            case "[ B ]": return f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.255.255'
            case _: return f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.{self.ipwxyz()["y"]}.255'

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def minimumIp(self):
        match self.classIp()[0]:
            case "[ A ]": return f'{self.ipwxyz()["w"]}.0.0.1'
            case "[ B ]": return f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.0.1'
            case _: return f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.{self.ipwxyz()["y"]}.1'

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def maximumIp(self):
        match self.classIp()[0]:
            case "[ A ]": return f'{self.ipwxyz()["w"]}.255.255.254'
            case "[ B ]": return f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.255.254'
            case _: return f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.{self.ipwxyz()["y"]}.254'

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def subnetsIp(self, nos):
        # nos -> Number of Subnets
        n = int(0)
        binplus = dict({2: 128, 4: 64, 8: 32, 16: 16, 32: 8, 64: 4, 128: 2})
        ipsubnetlist = list([])
        match self.classIp()[0]:
            case "[ A ]":
                ipsubnetlist = list([])
                for i in range(0, 255, binplus[nos]):
                    ipsubnetlist.append(f'{self.ipwxyz()["w"]}.{n+i}.0.0')
            case "[ B ]":
                ipsubnetlist = list([])
                for i in range(0, 255, binplus[nos]):
                    ipsubnetlist.append(
                        f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.{n+i}.0')
            case _:
                ipsubnetlist = list([])
                for i in range(0, 255, binplus[nos]):
                    ipsubnetlist.append(
                        f'{self.ipwxyz()["w"]}.{self.ipwxyz()["x"]}.{self.ipwxyz()["y"]}.{n+i}')

        return list(ipsubnetlist)

    # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
    def subnetsBinaryIp(self, nos):
        ipbl = list([])  # Ip binary Subnet List
        for e in self.subnetsIp(nos):
            ipbl.append(self.binaryIp(e))
        return ipbl
