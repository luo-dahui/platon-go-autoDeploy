'''
@Author: xiaoming
@Date: 2019-01-23 15:29:46
@LastEditors: xiaoming
@LastEditTime: 2019-01-24 10:35:24
@Description: 执行部署
'''
from optparse import OptionParser

from deploy.common import log
from deploy.deploy import AutoDeployPlaton
from deploy.common.download_packge import download_platon
from deploy.common.abspath import abspath
from conf import setting as conf


def parse_options():
    parser = OptionParser('deploy-PlatON')
    parser.add_option(
        '-C', '--config',
        dest='config',
        default='./deploy/node/test_node.yml',
        help='节点配置文件路径,默认为项目目录的./deploy/node/test_node.yml'
    )
    parser.add_option(
        '-S', '--stop',
        dest='stop',
        default=False,
        help='关闭指定配置文件的所有节点'
    )
    parser.add_option(
        '-U', '--url',
        dest='url',
        default=None,
        help='下载包url，不存在时，使用./deploy/rely/bin/platon中的原platon文件'
    )
    parser.add_option(
        '-T', '--type',
        dest='type',
        default=None,
        help='部署类型,默认不需要初始化,类似testnet'
    )
    parser.add_option(
        '-I', '--init',
        dest='init',
        default=True,
        help='是否需要初始化部署，默认需要'
    )
    parser.add_option(
        '-P', '--path',
        dest='path',
        default=None,
        help='部署目录'
    )
    parser.add_option(
        '-L', '--loglevel',
        dest='loglevel',
        default=4,
        help='日志级别'
    )
    opts, _ = parser.parse_args()
    return opts


def run():
    opt = parse_options()
    config_yml = opt.config
    node_yml = abspath(config_yml)
    t = opt.type
    url = opt.url
    init = opt.init
    p = opt.path
    stop = opt.stop
    conf.LOG_LEVEL = opt.loglevel
    if p:
        conf.DEPLOY_PATH = p
    auto = AutoDeployPlaton(net_type=t)
    if stop:
        auto.kill_of_yaml(node_yml)
        exit(1)
    if url:
        try:
            log.info("下载platon文件中...")
            download_platon(url)
        except Exception as e:
            log.error(e)
            raise e
    
    if t or not init:
        auto.deploy_default_yml(node_yml)
    else:
        auto.start_all_node(node_yml)

if __name__ == "__main__":
    run()
