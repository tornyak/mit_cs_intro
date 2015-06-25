__author__ = 'etkvadi'

import os
import fileinput
import re

'''
Parse DEPLOYMENT.working file, modify it based on cloud configuration.
'''
def deployment_ready_clean(fn):

    fo = open(fn, "rw+")
    lines = fo.readlines()
    fo.close()

    fo = open("DEPLOYMENT.tmp", "w")

    rstate = lines[1].rsplit(" ",1)[1]
    rstate=rstate.rstrip()
    create_p_backup=1

    for e in lines:
        if "mtas-platform" in e:
            create_p_backup=0
            break

    writeflag=1

    for e in lines:
        if "cluster.conf: This is a template" in e:
            writeflag = 0
            fo.write("# cluster.conf for MTASv\n")
        elif "End of file" in e:
            writeflag = 1
        elif "evip version" in e:
            e = re.sub(r'<evip version=\"1.0\"/>', '# evip.xml for MTASv', e)
        elif "disk_device_path=" in e:
            e = re.sub(r'sdb', 'vda', e)
        if writeflag != 0:
            fo.write(e)
        if " PL_MMAS" in e and create_p_backup==1:
            fo.write("AIT-BRF-CREATE-BACKUP:mtas-platform-"+rstate+"\n")
        if "PR_CDFRT" in e:
            fo.write("AIT-BRF-CREATE-BACKUP:mtas-installed\n")


    fo.close()




'''
merge evip.xml and cluster.conf to DEPLOYMENT.tmp, rename it as DEPLOYMENT.ready
'''
def merge_evip_cluster_conf(nodename,pl,dir):
    cluster = open("/local/mtas_conf/"+nodename+"_cloud_cluster.conf.2SC"+pl+"PL")
    evip = open("/local/mtas_conf/"+nodename+"_cloud_evipcfg.xml.2SC"+pl+"PL")
    conf1 = cluster.read().splitlines()
    conf2 = evip.read().splitlines()

    for e in fileinput.input(r'DEPLOYMENT.tmp', inplace=1):
        print e,
        if "cluster.conf for MTASv" in e:
            for e in conf1:
                print e
        elif "evip.xml for MTASv" in e:
            for e in conf2:
                print e

    fo= open("DEPLOYMENT.tmp", "rw+")
    lines = fo.readlines()
    fo.close()

    fo = open("DEPLOYMENT.ready", "w")
    for e in lines:
        if not "evip.xml for MTASv" in e:
            fo.write(e)
    fo.close()


    cluster.close()
    evip.close()

    os.remove("DEPLOYMENT.tmp")
