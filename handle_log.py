import os
import shutil
import tarfile
import time
from optparse import OptionParser

from deploy.common.connect import connect_linux, run_ssh
from deploy.common.load_file import get_node_list
from deploy.deploy import run_thread

TMP_LOG = "./tmp_log"
LOG_PATH = "./bug_log"


def check_path():
    if not os.path.exists(TMP_LOG):
        os.mkdir(TMP_LOG)
    else:
        shutil.rmtree(TMP_LOG)
        os.mkdir(TMP_LOG)
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)


def download(node, deploy_path, abs_log_path=""):
    ip = node["host"]
    port = node["port"]
    ssh, sftp, t = connect_linux(
        ip=ip, username=node["username"], password=node["password"])
    if not abs_log_path:
        log_path = "{}/node-{}".format(deploy_path, port)
        run_ssh(ssh, "cd {};tar zcvf log.tar.gz ./log".format(log_path))
        sftp.get("{}/log.tar.gz".format(log_path),
                 "{}/{}_{}.tar.gz".format(TMP_LOG, ip, port))
        run_ssh(ssh, "cd {};rm -rf ./log.tar.gz".format(log_path))
    else:
        run_ssh(ssh, "tar zcvf log.tar.gz {}".format(abs_log_path))
        sftp.get("./log.tar.gz", "{}/{}_{}.tar.gz".format(TMP_LOG, ip, port))
        run_ssh(ssh, "rm -rf ./log.tar.gz")
    t.close()


def save():
    print("开始压缩.....")
    t = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
    tar = tarfile.open("{}/{}_log.tar.gz".format(LOG_PATH, t), "w:gz")
    tar.add(TMP_LOG)
    tar.close()
    print("压缩完成")
    print("开始删除缓存.....")
    shutil.rmtree(TMP_LOG)
    print("删除缓存完成")


def parse_options():
    parser = OptionParser('PlatONTest')

    parser.add_option(
        '-N', '--node',
        dest='node',
        default="./deploy/node/test_node.yml",
        help='节点配置文件'
    )

    parser.add_option(
        '-D', '--deploy_path',
        dest='deploy_path',
        default="./platon_test",
        help='节点部署目录'
    )

    parser.add_option(
        '-L', '--log',
        dest='log',
        default="",
        help='日志绝对路径'
    )

    opts, _ = parser.parse_args()
    return opts


def main():
    opt = parse_options()
    node_yml = opt.node
    deploy_path = opt.deploy_path
    abs_log_path = opt.log
    node_list1, node_list2 = get_node_list(node_yml)
    node_list = node_list1 + node_list2
    check_path()
    print("校验目录完成，开始下载......")
    # for node in node_list:
    #     download(node, deploy_path=deploy_path, abs_log_path=abs_log_path)
    run_thread(node_list, download, deploy_path, abs_log_path)
    print("日志下载完成")
    save()


if __name__ == "__main__":
    main()
