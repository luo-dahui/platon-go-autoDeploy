import os

# 日志级别
LOG_LEVEL = 4

# 项目基本路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 节点配置文件路径
NODE_YML = os.path.abspath(os.path.join(BASE_DIR, "deploy/node/test_node.yml"))

# vc节点配置文件路径
VC_NODE_YML = os.path.abspath(os.path.join(BASE_DIR, "deploy/node/vc_node.yml"))

# Alice节点配置文件路径
ALICE_NODE_YML = os.path.abspath(os.path.join(BASE_DIR, "deploy/node/alice.yml"))

# Bob节点配置文件路径
BOB_NODE_YML = os.path.abspath(os.path.join(BASE_DIR, "deploy/node/bob.yml"))

CONFIG_FILE = os.path.abspath(os.path.join(BASE_DIR, "deploy/rely/config.json"))

# 节点创世文件默认保存位置
GENESIS_TMP = os.path.abspath(os.path.join(BASE_DIR, "deploy/rely/tmp/genesis.json"))

# 节点创世文件共存位置
GENESIS_TMP_OTHER = os.path.abspath(os.path.join(BASE_DIR, "deploy/rely/tmp/genesis_other/genesis.json"))

# 节点创世文件模板
GENESIS_TEMPLATE = os.path.abspath(os.path.join(BASE_DIR, "deploy/rely/template/genesis.json"))

# 部署目录
DEPLOY_PATH = r"./platon_test"

# 生成节点互连文件路径
STATIC_NODE_FILE = os.path.abspath(os.path.join(BASE_DIR, 'deploy/rely/tmp/static-nodes.json'))

# 节点私钥目录
NODEKEY = os.path.abspath(os.path.join(BASE_DIR, 'deploy/rely/tmp/nodekey'))

# 创世文件中写入有大量余额的账户
ADDRESS = "0x493301712671ada506ba6ca7891f436d29185821"

# 钱包文件路径
KEYSTORE = os.path.abspath(os.path.join(BASE_DIR,
                                        'deploy/rely/keystore/UTC--2018-10-04T09-02-39.439063439Z--493301712671ada506ba6ca7891f436d29185821'))

KEYSTORE2 = os.path.abspath(os.path.join(BASE_DIR,
                                            'deploy/rely/keystore/UTC--2018-10-20T08-44-32.680205800Z--c1f330b214668beac2e6418dd651b09c759a4bf5'))
# 该钱包的私钥
PRIVATE_KEY = '0xa11859ce23effc663a9460e332ca09bd812acc390497f8dc7542b6938e13f8d7'

# 钱包密码
PASSWORD = "88888888"

# 默认的部署cbft文件路径
CBFT = os.path.abspath(os.path.join(BASE_DIR, "deploy/rely/cbft.json"))

# 修改cbft后保存的文件路径
CBFT_TMP = os.path.abspath(os.path.join(BASE_DIR, 'deploy/rely/tmp/cbft.json'))

# cbft模板路径
CBFT_TEMPLATE = os.path.abspath(os.path.join(BASE_DIR, "deploy/rely/template/cbft.json"))

# platon bin文件保存路径
PLATON_BIN = os.path.abspath(os.path.join(BASE_DIR, 'deploy/rely/bin/platon'))

# platon 二进制文件保存目录
PLATON_DIR = os.path.abspath(os.path.join(BASE_DIR, 'deploy/rely/bin'))

# mpclib
MPCLIB = os.path.abspath(os.path.join(BASE_DIR, "deploy/rely/mpclib/mpclib.tar.gz"))

SPLIT_LOG_SCRIPT = os.path.abspath(os.path.join(BASE_DIR, "deploy/rely/script/split_log.py"))

SUP_TEMPLATE = os.path.abspath(os.path.join(BASE_DIR, "deploy/rely/template/supervisor.conf"))
SUP_TMP = os.path.abspath(os.path.join(BASE_DIR, "deploy/rely/tmp/supervisor/"))
