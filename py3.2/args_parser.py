# -*- coding:UTF-8 -*-
import argparse
__author__ = u"linyuchen"
__doc__ = u"""
新增命令行解析模块argparse
"""

parser = argparse.ArgumentParser(
            description='命令行帮助',         # main description for help
            epilog='帮助到此结束')  # displayed after help

parser.add_argument('action',                       # argument name
                    choices=['deploy', 'start', 'stop'],  # three allowed values
                    help='action on each target')         # help msg

parser.add_argument('targets',
                    metavar='HOSTNAME',                   # var name used in help msg
                    nargs='+',                            # require one or more targets
                    help='url for target machines')       # help msg explanation

parser.add_argument('-u', '--user',                 # -u or --user option
                    required=True,                        # make it a required argument
                    help='login as user')


# 添加子参数
subparsers = parser.add_subparsers()

parser_l = subparsers.add_parser('launch', help='Launch Control')   # first subgroup
parser_l.add_argument('-m', '--missiles', help="missiles: boolean", action='store_true')

print(parser.parse_args("deploy http://asdf -u me launch -m".split()))
print(parser.parse_args("deploy http://asdf -u me launch -h".split()))
print(parser.parse_args("-h".split()))
