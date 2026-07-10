# Network Troubleshooting Assistant

## 概要

Network Troubleshooting Assistant は、Ciscoネットワーク環境における障害解析を支援するStreamlitベースのWebアプリケーションです。

ネットワーク障害発生時に、症状に応じた確認コマンドを提示し、ユーザーが入力した `ping`、`traceroute`、Cisco `show` コマンドの実行結果を解析することで、障害原因の推定と復旧方法の提案を行います。

本システムでは、あらかじめ登録された正常なネットワーク構成情報とコマンド実行結果を比較し、問題箇所をOSI参照モデルのLayer1（物理層）、Layer2（データリンク層）、Layer3（ネットワーク層）に分類して診断します。


## 主な機能

- 発生しているネットワーク障害の種類を選択
- 障害内容に応じた原因候補の提示
- 確認すべきCiscoコマンドの案内
- showコマンド実行結果の解析
- L1 / L2 / L3 に基づく障害分類
- VLAN、Trunk、Interface、Routing、OSPF障害の検出
- 障害原因に応じた復旧コマンドの提案


## 対応する障害例

### 同一VLAN間で通信できない

確認項目：

- Interface状態
- VLAN割当
- Trunk設定

使用コマンド例：

- show interfaces status
- show vlan
- show interfaces switchport


### 遠隔ネットワークへpingできない

確認項目：

- Interface状態
- Routing設定
- 経路情報

使用コマンド例：

- show ip interface brief
- show ip route


### OSPF Neighborが形成されない

確認項目：

- OSPF設定
- Area設定
- Neighbor状態

使用コマンド例：

- show ip ospf neighbor
- show running-config


## システム構成
