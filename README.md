# 使用supervisor部署PlatON
### 环境准备
+ 下载python3.6以及以上版本，配置好pip
+ pip install -r requirements.txt

### 配置节点文件
配置文件请放置在deploy/node 目录下
```yaml
collusion: #共识节点列表
- host: 10.10.8.16 #ip必填
  port: 16789 #非必填，默认为16789，一台机器部署多个节点时必填，且不可重复
  rpcport: 6789 #非必填，默认为6789，一台机器部署多个节点时必填，且不可重复
  username: juzhen # 节点机器用户 必填
  password: '123456' # 节点机器密码 必填
  id: 22802ac12697f3ba8...724df621596579cf640658bd74ea97c429 #节点公钥，非必填
  nodekey: 73fc348dd...c33efc33fb4e52ff9c9cc # 节点私钥,非必填
  url: http://10.10.8.16:6789 #连接url，非必填，建议不填
- host: 10.10.8.16
  port: 16788
  rpcport: 6788
  username: juzhen
  password: '123456'
  id: 6c74c4c83f55a07b7949869dbeb90415a32674c085711f21f9f1b707cb9eef41703404f5edc280b78061a3fc0bb09223c79e4c5214ae39cbd3f0414e82af6b55
  nodekey: 3a40872b61d57baf773e5baad16d8d76edd725513cc4c6c171ef5702ad65797f
  url: http://10.10.8.16:6788
- host: 10.10.8.16
  port: 16787
  rpcport: 6787
  username: juzhen
  password: '123456'
  id: bed8c7c573a3179301a0e0c1253bc46ce88f9ae1b835eddc1ef7c5fd54088c8db5cf12dd90c487adc352104f1c495281c67e88e47ee2782bdac7b9cd1514eeaf
  nodekey: c1da5ce934499df868c037eb53e011d20cd13464aeda092fc4cb7efe7d1fabf6
  url: http://10.10.8.16:6787
- host: 10.10.8.16
  port: 16786
  rpcport: 6786
  username: juzhen
  password: '123456'
  id: 4db405aa44f107c0187732b3d3ed4edb16769b6be9b657b0f6c07af0fdb2c1628cd97b53869e9d1fd7b290d07973a7086d8edb0ce8502c06b5d6a0ed12b180e9
  nodekey: 6edae1e9a1ef7c83138c55229d843059dc59fd87fbd2977ba172fcb9f834ff96
  url: http://10.10.8.16:6786
nocollusion: #非共识节点列表
- host: 10.10.8.16
  port: 16785
  rpcport: 6785
  username: juzhen
  password: '123456'
  id: 534f6ce13bd49d690354dc43883809fbd21250de887d1e7e99961ef8bcd10eb5e7aa8d1d7bfe13cf04a854e5e746ad35fe4bed41aea13ad11e34a795257bd8ff
  nodekey: d2c3e9cdbbf4d029c53a022fd6f596c6471df45fbcd8c6ceb35e512001fdf621
  url: http://10.10.8.16:6785
- host: 10.10.8.16
  port: 16784
  rpcport: 6784
  username: juzhen
  password: '123456'
  id: ccfbc546913428003121bc88053f1c68ee65c1362cc9bf517a7b00a32d11f8c2e12cd73a2a130f44d3cd2374b2ead02b0806ffd2eaaa4545d2ab7ccd614764da
  nodekey: 4953bbf6d40c654f3a8c21af3cd1278f7faf613df9fd5750d8e4ac842728c80f
  url: http://10.10.8.16:6784

```
### 运行
+ 运行前请手动关闭原有不使用supervisor部署的节点
+ cmd


```js
python run.py -h #查看使用说明
// 部署方式1
python run.py --url="down_package_platon_url" --config="节点配置文件路径" # 部署节点
// 部署方式2
python run.py  --config="节点配置文件路径" #先把二进制platon放置在deploy/rely/bin目录下
```
