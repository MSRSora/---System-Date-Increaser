# 系统日期增加器 - System Date Increaser

## 这是什么？

这是一个可以快速增加Windows系统日期的小程序，可用于快速刷取含挂机要素的单机游戏的奖励，而无需频繁调整系统日期或时间。

## 哪些游戏可以用这个程序？

包括但不限于：

- 植物大战僵尸（加速禅境花园的植物成长、获取浇水/施肥/售卖植物等奖励）
- 逃离鸭科夫（快速获取挖矿奖励、刷新各类商店物品）
- 各类单机挂机（闲置）游戏

<!--笔者开发这个程序的起因，是在游玩一款名为《冥狱战术（Hadean Tactics）》的游戏时，发现墓穴中有一个每天只能领取一次的宝箱，领取后需等待约1天的倒计时，而后才能再次领取。为了快速获取奖励以达成全收集成就，因此开发了该程序。-->

## 使用方法 

1. 如果您的系统是Windows 11，右键点击菜单栏右下角的系统时间 - 调整日期和时间，**将“自动设置时间”选项关闭**。

   如果是其他Windows系统，打开控制面板，搜索“日期和时间”，点击“Internet 时间”选项卡 - 更改设置，**取消勾选“与 Internet 时间服务器同步”**。

   这一步是为了防止系统自动联网更新系统时间。

2. **如果对单次增加的时间没有要求，直接下载System_Date_Increaser.exe文件，然后跳到第3步。**

   如果想要修改单次增加的时间，则需下载System_Date_Increaser.py文件，然后按以下步骤执行：

   - **修改代码中计算目标时间的部分，即`datetime.timedelta()`的参数**

     示例：

     **改为一次增加 12 小时**

     `timedelta`的`hours`参数可指定小时数，将代码中计算`tomorrow`的部分修改为：

     ```python
     # 计算12小时后的时间
     tomorrow = now + datetime.timedelta(hours=12)  # 关键修改：hours=12
     ```

     **改为一次增加 1 周**

     `timedelta`的`weeks`参数可指定周数（1 周 = 7 天），修改为：

     ```python
     # 计算1周后的时间
     tomorrow = now + datetime.timedelta(weeks=1)  # 关键修改：weeks=1
     ```

     **注意事项**：

     - `timedelta`支持的时间单位：`weeks`（周）、`days`（天）、`hours`（小时）、`minutes`（分钟）、`seconds`（秒）等，可根据需求组合（如`timedelta(days=3, hours=2)`表示 3 天 2 小时）。
     - 修改后界面的按钮文字（如 “增加 1 天”）也建议同步修改（在`create_widgets`方法中修改`Button`的`text`参数），避免歧义。

   - **安装 pyinstaller**

     确保已安装 pyinstaller，如果没有安装，使用 pip 命令安装：

     ```bash
     pip install pyinstaller
     ```

   - **编译为可执行文件**

     在命令行中切换到程序所在的目录，执行以下命令：

     ```bash
     pyinstaller --onefile --name "System_Date_Increaser" System_Date_Increaser.py
     ```

     命令参数说明：

     - `--onefile`：将所有文件打包成单个.exe 文件（方便分发）
     - `--name "System_Date_Increaser"`：指定生成的可执行文件名称
     - System_Date_Increaser.py：你的 Python 源代码文件

   - **查找生成的文件**

     编译完成后，会在当前目录生成`dist`文件夹，可执行文件（System_Date_Increaser.exe）就位于该文件夹中。

     **注意事项**：

     1. 由于程序涉及修改系统时间，运行生成的.exe 文件时**必须以管理员身份**运行，否则会修改失败

     2. 生成的.exe 文件可能会被部分杀毒软件误报，属于正常现象

     3. 如果需要隐藏控制台窗口（仅显示 GUI 界面），可以添加`--noconsole`参数：

        ```bash
        pyinstaller --onefile --noconsole --name "System_Date_Increaser" System_Date_Increaser.py
        ```

3. **关闭游戏程序，然后打开System_Date_Increaser.exe，点击按钮，再次打开游戏程序即可获取挂机奖励。**
