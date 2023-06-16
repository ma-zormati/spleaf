from mininet.topo import Topo

class SpineLeaf ( Topo ):
    "Spine Leaf Topology S2 L4 H4/L"

    def build(self):
        #Initialize topology
        switchesSpine=[]
        switchesLeaf=[]
        hosts=[]
        s = 2
        l = 4
        hpl = 4
        #Switches
        for i in range (s):
            nm="SS{}".format(i+1)
            switchesSpine.append(self.addSwitch(nm))

        for i in range (l):
            nm = "SL{}".format(i + 1)
            switchesLeaf.append(self.addSwitch(nm))

        #Hosts
        for i in range (l*hpl):
            nm = "H{}".format(i + 1)
            hosts.append(self.addHost(nm))

        #Links
        for leaf in range(l):
            for spine in range(s):
                self.addLink(switchesSpine[spine], switchesLeaf[leaf])

        leaf = 0
        for host in range (l*hpl):
            self.addLink(switchesLeaf[leaf], hosts[host])
            if ((host+1)%hpl)==0:
                leaf+=1


topos = {'spineleaf': (lambda : SpineLeaf())}
