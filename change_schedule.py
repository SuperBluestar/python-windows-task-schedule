"""
Python script to interact with existing Windows Task Scheduler tasks.
CLI usage:
    python windows_task_scheduler.py {enable|disable|run} -t "TaskName"
import usage:
    import windows_task_scheduler as wts
    wts.enable_task(task_name='TaskName')
    wts.disable_task(task_name='TaskName')
    wts.run_task(task_name='TaskName')
There are many more possibilities; at the command prompt, type 'schtasks.exe /?' or e.g. 'schtasks.exe /Change /?' for details.
"""

import logging
import argparse
import subprocess


logger = logging.getLogger(__name__)


def get_parser():
    # Parse inputs
    parser = argparse.ArgumentParser(
        description="Provide task name", add_help=False)

    parser.add_argument("-t", "--task", dest="task_name",
                        required=False, help="Task name (in Windows Task Scheduler)")

    # Choose functionality
    subparsers = parser.add_subparsers()

    parser_enable = subparsers.add_parser(
        "enable", parents=[parser], help="Enable the task")
    parser_enable.set_defaults(func=enable_task)

    parser_disable = subparsers.add_parser(
        "disable", parents=[parser], help="Disable the task")
    parser_disable.set_defaults(func=disable_task)

    parser_run = subparsers.add_parser(
        "run", parents=[parser], help="Run the task")
    parser_run.set_defaults(func=run_task)

    return parser


def enable_task(args=None, task_name=None):
    """ Enable existing Windows Task Scheduler task.
    """
    if args is not None:
        task_name = args.task_name

    p = subprocess.Popen(['schtasks.exe', '/Change', '/TN', task_name,
                          '/ENABLE'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logger.info("Enabled task: {0}".format(task_name))
    return


def disable_task(args=None, task_name=None):
    """ Disable existing Windows Task Scheduler task.
    """
    if args is not None:
        task_name = args.task_name

    p = subprocess.Popen(['schtasks.exe', '/Change', '/TN', task_name,
                          '/DISABLE'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logger.info("Disabled task: {0}".format(task_name))
    return


def run_task(args=None, task_name=None):
    """ Run existing Windows Task Scheduler task.
    """
    if args is not None:
        task_name = args.task_name

    p = subprocess.Popen(['schtasks.exe', '/Run', '/TN', task_name],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logger.info("Run task: {0}".format(task_name))
    return


def main(args=None):
    logger.info("\n" + "=" * 72 + "\n{0} begun ...".format(__name__))

    # Handle arguments
    if args is None:
        args = get_parser().parse_args()
        args.func(args)
    else:
        # Use externally-provided arguments
        if args.disable_flag:
            disable_task(task_name=args.task_name)
        elif args.enable_flag:
            enable_task(task_name=args.task_name)
        elif args.run_flag:
            run_task(task_name=args.task_name)


if __name__ == '__main__':
    main()

# End


