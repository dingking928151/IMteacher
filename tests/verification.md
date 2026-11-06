# 首版验证与安装结果

日期：2026-11-05，用户时区 Asia/Shanghai。

## 执行结果

- 四技能均通过skill-creator的quick_validate（Python以UTF-8模式执行）。最初默认GBK读取UTF-8文件失败，改用 `python -X utf8` 后通过；未修改全局编码配置。
- 项目validate_bundle检查四个规范名称、发现描述、本地引用、共享约定字节一致及原IMteacher八份参考文件保留：通过。
- entry_eval完成入口5、规划6、督学5、教学6，共22个场景演练；Claude另做2个混合/续课书面推演。发现的冲突已修正文与引用，并由entry_eval窄范围复核；最后一处保底措辞残留已修。
- install.ps1完成WhatIf与静态审阅，然后在最终D盘项目中实际执行。四技能×三个runtime目录复制成功，脚本逐文件核对SHA256，执行返回0。
- Claude四场字幕实物已核查；没有核查视频画面。字幕时间范围不被当作连续观看证明。

## 安装范围

项目：`D:\AI\Projects\Active\im-skills`

运行时：当前用户 `.codex\skills`、`.claude\skills`、`.agents\skills`；各含using-im、implanner、imteacher、imsupervisor。

备份及清单：`D:\AI\Projects\Active\im-skills\backups\20261105-231558-dc4e8609`。

没有删除旧目录、改用户课程档案、提交或推送。C盘最初工作目录保留为本轮暂存历史；今后维护D盘项目为准。

## 限制

结构检查不证明教学效果；单代理场景演练不等于五次独立重复抽样，未做长期使用实验或并发写入测试。安装文件更新不证明已经运行的会话自动刷新；新会话需读取新技能。
