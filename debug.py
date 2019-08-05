import paramiko
import os
from deploy.deploy import AutoDeployPlaton
from deploy.common.load_file import get_node_list
from deploy.common.connect import connect_web3


def connect_linux(ip="10.10.8.16", username='juzhen', password='123456'):
    t = paramiko.Transport((ip, 22))
    t.connect(username=username, password=password)
    ssh = paramiko.SSHClient()
    ssh._transport = t
    sftp = paramiko.SFTPClient.from_transport(t)
    return ssh, sftp, t


def run_ssh(ssh, cmd, password=None):
    try:
        stdin, stdout, _ = ssh.exec_command("source /etc/profile;%s" % cmd)
        if password:
            stdin.write(password+"\n")
        stdout_list = stdout.readlines()
        if len(stdout_list):
            print(stdout_list)
    except Exception as e:
        raise e
    return stdout_list


def pull(ssh, path="/home/juzhen/go/src/github.com/PlatONnetwork/PlatON-Go/", branch="feature-test"):
    cmd = "cd {};git checkout {};git pull origin {}".format(
        path, branch, branch)
    run_ssh(ssh, cmd)


def build(ssh, path="/home/juzhen/go/src/github.com/PlatONnetwork/PlatON-Go/", branch="feature-test"):
    cmd = "cd {};git checkout {};make platon".format(path, branch)
    run_ssh(ssh, cmd)


def download(sftp, path="/home/juzhen/go/src/github.com/PlatONnetwork/PlatON-Go/"):
    bin_path = "deploy/rely/bin/platon"
    os.remove(bin_path)
    path = os.path.join(path, "build/bin/platon")
    sftp.get(path, bin_path)


def clean(ssh, path="/home/juzhen/go/src/github.com/PlatONnetwork/PlatON-Go/", branch="feature-test"):
    cmd = "cd {};git checkout {};make clean".format(path, branch)
    run_ssh(ssh, cmd)


def main():
    ssh, sftp, t = connect_linux()
    print("更新代码.....")
    pull(ssh)
    print("编译.....")
    build(ssh)
    print("下载二进制到本地...")
    download(sftp)
    print("清空编译信息.....")
    clean(ssh)
    t.close()


def deploy(node_file):
    auto = AutoDeployPlaton()
    auto.deploy_default_yml(node_file)


def monitor(node_file):
    node_list, _ = get_node_list(node_file)
    w3_list = [connect_web3(node["url"]) for node in node_list]
    node_id = [node["id"] for node in node_list]
    import time
    z = 1
    while True:
        time.sleep(10)
        i = 0
        for w3 in w3_list:
            print("节点{},块高:{}".format(node_id[i], w3.eth.blockNumber))
            i = +1
        print("第{}窗口期共识结束..........".format(z))
        z += 1


if __name__ == "__main__":
    main()
    node_file = "deploy/node/test_node.yml"
    deploy(node_file)
    monitor(node_file)
