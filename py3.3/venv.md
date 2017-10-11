# Python的venv模块

Python3.3版本开始才有此模块

此模块类似于virtualenv，用于创建单独的Python环境

# 用法

`python -m venv -h`

可以看到

```shell 

Creates virtual Python environments in one or more target directories.

positional arguments:
  ENV_DIR               A directory to create the environment in.

optional arguments:
  -h, --help            show this help message and exit
  --system-site-packages
                        Give the virtual environment access to the system
                        site-packages dir.
  --symlinks            Try to use symlinks rather than copies, when symlinks
                        are not the default for the platform.
  --copies              Try to use copies rather than symlinks, even when
                        symlinks are the default for the platform.
  --clear               Delete the contents of the environment directory if it
                        already exists, before environment creation.
  --upgrade             Upgrade the environment directory to use this version
                        of Python, assuming Python has been upgraded in-place.
  --without-pip         Skips installing or upgrading pip in the virtual
                        environment (pip is bootstrapped by default)
  --prompt PROMPT       Provides an alternative prompt prefix for this
                        environment.

```

## 新建个环境

python -m venv test

## 激活环境

Windows:
`test/Scripts/activate.bat`

Linux:
`source test/Scripts/activate`

## 退出环境

Windows:
`test/Scripts/deactivate.bat`

Linux:
`exit`