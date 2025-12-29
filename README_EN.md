# System Date Increaser

## What's this?

This is a small program that can quickly update the date of the Windows system. It can be used to quickly claim the rewards of single-player games with auto-play elements without the need to frequently adjust the system date or time.

## Which games can be played with this program?

Including but not limited to: 

- Plant vs. Zombies (Accelerates the growth of plants in Zen Garden, grants rewards such as watering, fertilizing, and selling plants)
- Escape From Duckov (Quickly acquires mining rewards, refreshes various store items)
- Various single-player auto-play (Idle) games

<!--The reason why I developed this program was that while playing a game called "Hadean Tactics", I discovered that there was a treasure chest in the tomb that could only be claimed once a day. After claiming it, there was a countdown of about 1 day before one could claim it again. In order to quickly obtain the rewards and achieve the full collection achievement, I developed this program.-->

## Usage

1. If your operating system is Windows 11, right - click on the system time in the lower - right corner of the menu bar and select "Adjust date and time". Then, **turn off the "Set time automatically" option**.
If you are using other Windows systems, open the Control Panel, search for "Date and time", click on the "Internet Time" tab, and then select "Change settings". **Uncheck the "Synchronize with an Internet time server" option**.
This step is to prevent the system from automatically connecting to the Internet to update the system time.
2. **If there are no specific requirements for the time increment per operation, directly download the System_Date_Increaser.exe file and skip to Step 3.**
If you want to modify the time increment per operation, you need to download the System_Date_Increaser.py file and follow these steps:
 - **Modify the part of the code that calculates the target time, i.e., the parameters of `datetime.timedelta()`**
Examples:
**Change to increment by 12 hours at a time**
The `hours` parameter of `timedelta` can specify the number of hours. Modify the part of the code that calculates `tomorrow` as follows:
```python
# Calculate the time 12 hours later
tomorrow = now + datetime.timedelta(hours = 12)  # Key modification: hours = 12
```
**Change to increment by 1 week at a time**
The `weeks` parameter of `timedelta` can specify the number of weeks (1 week = 7 days). Modify it as follows:
```python
# Calculate the time 1 week later
tomorrow = now + datetime.timedelta(weeks = 1)  # Key modification: weeks = 1
```
**Notes**:
 - The time units supported by `timedelta` include `weeks`, `days`, `hours`, `minutes`, `seconds`, etc., which can be combined according to requirements (e.g., `timedelta(days = 3, hours = 2)` represents 3 days and 2 hours).
 - It is recommended to synchronously modify the button text on the interface (e.g., "Increase by 1 day") after the modification (modify the `text` parameter of `Button` in the `create_widgets` method) to avoid ambiguity.
 - **Install pyinstaller**
Ensure that pyinstaller is installed. If not, use the pip command to install it:
```bash
pip install pyinstaller
```
 - **Compile into an executable file**
Switch to the directory where the program is located in the command line and execute the following command:
```bash
pyinstaller --onefile --name "System_Date_Increaser" System_Date_Increaser.py
```
Explanation of command parameters:
 - `--onefile`: Package all files into a single.exe file (for easy distribution).

 - `--name "System_Date_Increaser"`: Specify the name of the generated executable file.

 - System_Date_Increaser.py: Your Python source code file.

 - **Locate the generated file**
    After compilation, a `dist` folder will be generated in the current directory. The executable file (System_Date_Increaser.exe) is located in this folder.

  **Notes**:

    1. Since the program involves modifying the system time, the generated.exe file **must be run as an administrator**; otherwise, the modification will fail.
    2. The generated.exe file may be falsely reported by some antivirus software, which is a normal phenomenon.
    3. If you need to hide the console window (only display the GUI interface), you can add the `--noconsole` parameter:

```bash
pyinstaller --onefile --noconsole --name "System_Date_Increaser" System_Date_Increaser.py
```
3. **Close the game program, then open System_Date_Increaser.exe, click the button, and open the game program again to obtain the idle rewards.**